from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso

# LISTAR
def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, "curso/cursos.html", {"cursos": cursos})

# CRIAR
def criar_curso(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")

        Curso.objects.create(nome=nome, descricao=descricao)
        return redirect("lista_cursos")

    return render(request, "curso/form_curso.html")

# EDITAR
def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)

    if request.method == "POST":
        curso.nome = request.POST.get("nome")
        curso.descricao = request.POST.get("descricao")
        curso.save()
        return redirect("lista_cursos")

    return render(request, "curso/form_curso.html", {"curso": curso})

# EXCLUIR
def excluir_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    curso.delete()
    return redirect("lista_cursos")