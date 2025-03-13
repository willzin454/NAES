from django.urls import path

#importar views

from .views import PaginaInicial

urlpatterns = [
    path("", PaginaInicial.as_view(), name = "index"),
]
