from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class principalView(TemplateView):
    template_name = 'categorias.html'

class productosView(TemplateView):
    template_name = 'productos.html'