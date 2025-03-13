from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

# cria uma vie para redenrizzar a pagina inicial
# e faz uma herança de templateView

class PaginaInicial(TemplateView):
    template_name = "index.html"