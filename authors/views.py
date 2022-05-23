from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import RegisterForm

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
    }
    return render(request, 'authors/pages/register_view.html', context=context)


def view_register_create(request):
    if not request.POST:
        raise Http404

    POST = request.POST
    request.session['register_form_data'] = POST

    form = RegisterForm(POST)

    if form.is_valid():
        # salva form
        form.save()

        # pegar dados antes de salvar
        # data = form.save(commit=False)

        messages.success(request, 'Your user is created, please log in.')

        del(request.session['register_form_data'])
        del(request.session['number'])

    return redirect('authors:register')
