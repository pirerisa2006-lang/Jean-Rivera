from django.shortcuts import render
from portfolio.models import Project
from .models import Persona


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def portfolio(request):
    return render(request, 'portfolio/portfolio.html')


def personas(request):
    lista_personas = Persona.objects.all()
    return render(request, 'personas/personas.html', context={'personas': lista_personas})
