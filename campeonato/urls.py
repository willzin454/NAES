from django.urls import path
from . import views

urlpatterns = [
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/novo/', views.criar_curso, name='criar_curso'),
    path('cursos/editar/<int:id>/', views.editar_curso, name='editar_curso'),
    path('cursos/excluir/<int:id>/', views.excluir_curso, name='excluir_curso'),
]