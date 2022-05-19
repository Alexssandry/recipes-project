from django.shortcuts import render

# Create your views here.


def view_register(request):
    return render(request, 'authors/pages/register_view.html')
