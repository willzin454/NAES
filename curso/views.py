from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso
from .forms import CursoForm


# LISTAR
def lista_cursos(request):
    cursos = Curso.objects.all()

    return render(request, "curso/cursos.html", {"cursos": cursos})


# CRIAR
def criar_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("lista_cursos")

    else:
        form = CursoForm()

    return render(request, "curso/form_curso.html", {"form": form})


# EDITAR
def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)

    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)

        if form.is_valid():
            form.save()
            return redirect("lista_cursos")

    else:
        form = CursoForm(instance=curso)

    return render(request, "curso/form_curso.html", {"form": form})


# EXCLUIR
def excluir_curso(request, id):

    curso = get_object_or_404(Curso, id=id)

    if request.method == "POST":

        curso.delete()

        return redirect("lista_cursos")

    return render(request, "curso/confirmar_exclusao.html", {"curso": curso})


# DETALHAR
def detalhar_curso(request, id):

    curso = get_object_or_404(Curso, id=id)

    return render(request, "curso/detalhe_curso.html", {"curso": curso})
