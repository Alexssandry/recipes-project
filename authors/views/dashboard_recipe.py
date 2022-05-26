from authors.forms import AuthorRecipeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from recipes.models import Recipe


@method_decorator(
    login_required(login_url='authors:login', redirect_field_name='next'),
    name='dispatch'
)
class DashboardRecipe(View):
    def get_recipe(self, id):
        recipe = None
        if id:
            recipe = Recipe.objects.filter(
                is_published=False,
                author=self.request.user,
                pk=id,
            ).first()

            if not recipe:
                raise Http404

        return recipe

    def render_recipe(self, form):
        context = {
            'title': 'Dashboard Recipe Edit',
            'form': form,
            'form_action': ''
        }
        return render(
            self.request,
            'authors/pages/dashboard_recipe.html',
            context=context
        )

    def get(self, *args, **kwargs):
        recipe = self.get_recipe(kwargs.get('id'))
        form = AuthorRecipeForm(instance=recipe)
        return self.render_recipe(form)

    def post(self, request, id):
        recipe = self.get_recipe(id)

        form = AuthorRecipeForm(
            data=request.POST or None,
            files=request.FILES or None,
            instance=recipe,
        )

        if form.is_valid():
            # Agora, o form é válido e posso tentar salvar
            recipe = form.save(commit=False)

            recipe.author = request.user
            recipe.preparation_steps_in_html = False
            recipe.is_published = False

            recipe.save()

            messages.success(request, 'Sua receita foi salva com sucesso!')

            return redirect(
                reverse('authors:dashboard_recipe_edit', args=(id,)))

        return self.render_recipe(form)


@method_decorator(
    login_required(login_url='authors:login', redirect_field_name='next'),
    name='dispatch'
)
class DashboardRecipeNew(View):
    def get_return(self, request, form):
        return render(
            request,
            'authors/pages/dashboard_create_recipe.html',
            context={
                'title': 'Create a new recipe',
                'form': form,
                'form_action': reverse('authors:dashboard_create_new_recipe')
            }
        )

    def get(self, request):
        new_recipe_form_data = request.session.get(
            'new_recipe_form_data', None)
        form = AuthorRecipeForm(data=new_recipe_form_data)
        return self.get_return(request, form)

    def post(self, request):
        request.session['new_recipe_form_data'] = request.POST
        form = AuthorRecipeForm(
            data=request.POST,
            files=request.FILES
        )

        if form.is_valid():
            data_form = form.save(commit=False)
            data_form.author = request.user
            data_form.is_published = False
            data_form.preparation_steps_in_html = False
            data_form.save()
            messages.success(request, 'Recipe criada com sucesso!')

            del(request.session['new_recipe_form_data'])
            return redirect(reverse('authors:dashboard'))
        else:
            messages.error(request, 'Não foi possivel criar a sua recipe.')
            return redirect(reverse('authors:dashboard_new_recipe'))


@method_decorator(
    login_required(login_url='authors:login', redirect_field_name='next'),
    name='dispatch'
)
class DashboardRecipeDelete(View):
    def get_recipe(self, id):
        recipe = Recipe.objects.filter(
            is_published=False,
            author=self.request.user,
            pk=id,
        )
        return recipe

    def post(self, *args, **kwargs):
        id = self.request.POST.get('id')
        recipe = self.get_recipe(id)
        if not recipe:
            raise Http404

        recipe.delete()
        messages.success(self.request, 'Deleted successfully!')
        return redirect(reverse('authors:dashboard'))
