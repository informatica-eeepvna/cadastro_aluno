from django.shortcuts import render
from .models import Aluno


# Create your views here.
def index(request):
    alunos = Aluno.objects.all()
    return render(request, "alunos/index.html", {
        "alunos": alunos
    })


def cadastro(request):
    return render(request, "alunos/cadastro.html")
