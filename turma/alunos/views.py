from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    nome = request.POST.get("txtNome")
    cpf = request.POST.get("txtCpf")

    aluno = models.Aluno()
    return render(request, "alunos/cadastro.html")
