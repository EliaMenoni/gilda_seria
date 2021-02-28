from django.shortcuts import render
from .models import *

# Create your views here.
def home_articoli(request):
  return render(request, 'articoli/articoli.html', {})

def dettagli_articolo(request, titolo_articolo):
  return render(request, 'articoli/articoli.html', {})