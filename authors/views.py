from django.http import Http404
from django.shortcuts import render

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

    form = RegisterForm()

    context = {
        'title': 'Register',
        'form': form,
    }
    return render(request, 'authors/pages/register_view.html', context=context)


def view_register_create(request):
    if not request.POST:
        raise Http404

    form = RegisterForm(request.POST)

    return render(request, 'authors/pages/register_view.html', context={
        'form': form,
    })
