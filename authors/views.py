from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, RegisterForm

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

    if form.is_valid():
        authenticeted_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticeted_user is not None:
            messages.success(request, 'You are logged in.')
            login(request, authenticeted_user)
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
