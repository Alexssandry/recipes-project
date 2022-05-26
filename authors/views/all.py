from authors.forms import (AuthorRecipeForm, LoginForm,  # noqa: F401
                           RegisterForm)
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from recipes.models import Recipe

# Create your views here.


def view_register(request):
    # DUAS FORMAS DE FAZER A MESMA COISA
    request.session['number'] = request.session.get('number') or 0
    request.session['number'] += 1

    # if request.session.get('number'):
    #     request.session['number'] += 1
    # else:
    #     request.session['number'] = 1
    # FIM DUAS FORMAS DE FAZER A MESMA COISA

    register_form_data = request.session.get('register_form_data', None)

    form = RegisterForm(register_form_data)

    context = {
        'title': 'Register',
        'form': form,
        'form_action': reverse('authors:register_create')
    }
    return render(request, 'authors/pages/register_view.html', context=context)


def view_register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST

    form = RegisterForm(POST)

    if form.is_valid():
        # salva form porem a senha fica sem criptografia
        # form.save()

        # pegar dados antes de salvar
        data_form = form.save(commit=False)
        data_form.set_password(data_form.password)
        data_form.save()

        messages.success(request, 'Your user is created, please log in.')

        del(request.session['register_form_data'])
        del(request.session['number'])

    return redirect('authors:login')


def view_login(request):
    request.session['number'] = request.session.get('number') or 0
    request.session['number'] += 1

    form = LoginForm()

    context = {
        'title': 'Login',
        'form': form,
        'form_action': reverse('authors:login_create'),
    }
    return render(request, 'authors/pages/login.html', context=context)


def view_login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    login_url = reverse('authors:login')
    dashboard_url = reverse('authors:dashboard')

    if form.is_valid():
        authenticeted_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticeted_user is not None:
            messages.success(request, 'You are logged in.')
            login(request, authenticeted_user)
            return redirect(dashboard_url)
        else:
            messages.error(request, 'Invalid credentials.')
    else:
        messages.error(request, 'Invalid username or password.')

    return redirect(login_url)


@login_required(login_url='authors:login', redirect_field_name='next')
def view_logout(request):
    if not request.POST:
        return redirect(reverse('authors:login'))

    if request.POST.get('username') != request.user.username:
        print('invalid username', request.POST, request.user.username)
        return redirect(reverse('authors:login'))

    logout(request)
    return redirect(reverse('authors:login'))


@login_required(login_url='authors:login', redirect_field_name='next')
def view_dashboard(request):
    recipes = Recipe.objects.filter(
        is_published=False,
        author=request.user,
    )

    context = {
        'title': 'Dashboard',
        'recipes': recipes,
    }
    return render(request, 'authors/pages/dashboard.html', context=context)


# @login_required(login_url='authors:login', redirect_field_name='next')
# def view_dashboard_recipe_edit(request, id):
#     recipe = Recipe.objects.filter(
#         is_published=False,
#         author=request.user,
#         pk=id,
#     ).first()

#     if not recipe:
#         raise Http404

#     form = AuthorRecipeForm(
#         data=request.POST or None,
#         files=request.FILES or None,
#         instance=recipe,
#     )

#     if form.is_valid():
#         # Agora, o form é válido e posso tentar salvar
#         recipe = form.save(commit=False)

#         recipe.author = request.user
#         recipe.preparation_steps_in_html = False
#         recipe.is_published = False

#         recipe.save()

#         messages.success(request, 'Sua receita foi salva com sucesso!')

#         return redirect(reverse('authors:dashboard_recipe_edit', args=(id,)))

#     context = {
#         'title': 'Dashboard Recipe Edit',
#         'form': form,
#         'form_action': ''
#     }
#     return render(
#         request,
#         'authors/pages/dashboard_recipe.html',
#         context=context
#     )


# @login_required(login_url='authors:login', redirect_field_name='next')
# def view_dashboard_new_recipe(request):
#     new_recipe_form_data = request.session.get('new_recipe_form_data', None)

#     form = AuthorRecipeForm(new_recipe_form_data)

#     context = {
#         'title': 'Create Recipe',
#         'form': form,
#         'form_action': reverse('authors:dashboard_create_new_recipe')
#     }
#     return render(
#         request,
#         'authors/pages/dashboard_create_recipe.html',
#         context=context
#     )


# @login_required(login_url='authors:login', redirect_field_name='next')
# def view_dashboard_create_new_recipe(request):
#     if not request.POST:
#         raise Http404

#     POST = request.POST
#     request.session['new_recipe_form_data'] = POST

#     form = AuthorRecipeForm(
#         data=POST,
#         files=request.FILES
#     )

#     # cria um slug provisorio
#     # recipe_last_id = int(Recipe.objects.all().last().id)

#     if form.is_valid():
#         data_form = form.save(commit=False)
#         data_form.author = request.user
#         data_form.is_published = False
#         data_form.preparation_steps_in_html = False
#         # data_form.slug = 'new-recipe-teste-{0}'.format(recipe_last_id + 1)
#         data_form.save()
#         messages.success(request, 'Recipe foi criada com sucesso!')

#         del(request.session['new_recipe_form_data'])
#     else:
#         messages.error(request, 'Não foi possivel criar sua recipe')

#     return redirect('authors:dashboard')


# @login_required(login_url='authors:login', redirect_field_name='next')
# def view_dashboard_recipe_delete(request):
#     if not request.POST:
#         raise Http404

#     id = request.POST.get('id')
#     recipe = Recipe.objects.filter(
#         is_published=False,
#         author=request.user,
#         pk=id,
#     ).first()

#     if not recipe:
#         raise Http404

#     recipe.delete()
#     messages.success(request, 'Deleted successfully!')

#     return redirect(reverse('authors:dashboard'))
