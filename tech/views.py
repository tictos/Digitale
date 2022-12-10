from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render (request, 'tech/index.html')


def service(request):
    Maq = Maquette.objects.all()
    return render(request, 'tech/produit.html', {'maquette': Maq})


def apropos(request):
    return render(request, 'tech/apropos.html')

def contact(request):
    return render(request, 'tech/contact.html')

def detail(request):
    return render(request, 'tech/detail.html')