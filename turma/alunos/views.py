import cProfile
from distutils.log import error
from multiprocessing import context
from django.shortcuts import render
from .models import Aluno
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime


# Create your views here.
def index(request):
    consulta = request.GET.get("consulta")
    delete = request.POST.get("delete")
    edit_value = request.POST.get("edit")

    if delete:
        Aluno.objects.filter(id=delete).delete()
        
    if edit_value:
        return render(request, 'alunos/edit.html', {    
            "aluno": Aluno.objects.filter(id=edit_value).get()
        })


    if consulta:
        alunos = Aluno.objects.filter(nome__iregex=consulta)
    else:
        alunos = Aluno.objects.all()

    return render(request, "alunos/index.html", {
        "alunos": alunos,
        "consulta": consulta
    })


def cadastro(request):
    context = {"errormsg": None}

    if request.method == "POST":
        nome = request.POST["txtNome"].strip()
        cpf = request.POST["txtCpf"].strip()
        dtnasc = request.POST["dtNascimento"]
        email = request.POST["txtEmail"].strip()
        
        if nome and cpf and dtnasc and email:
            Aluno.objects.create(nome=nome, cpf=cpf, dtnasc=dtnasc, email=email)
            return HttpResponseRedirect(reverse("index"))
        else:
            context = {"errormsg": "Insira valores válidos!"}

    return render(request, "alunos/cadastro.html", context)


def edit(request, id):
    aluno = Aluno.objects.filter(id=id)
    if request.method == "POST":
        nome = request.POST.get("txtNome")
        cpf = request.POST.get("txtCpf")
        dtnasc = request.POST.get("dtNascimento")
        email = request.POST.get("txtEmail")

        if nome and cpf and dtnasc and email:
            aluno.update(nome=nome, cpf=cpf, dtnasc=dtnasc, email=email)
            return HttpResponseRedirect(reverse("index"))

    return render(request, "alunos/edit.html", {
        "aluno": aluno.get(),
    })
    