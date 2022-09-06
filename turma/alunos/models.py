from django.db import models

# Create your models here.
class Turma(models.Model):
    codigo = models.CharField(max_length=4)

    def __str__(self):
        return f"Turma: {self.codigo}"

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField(max_length=11)
    # dtnasc = models.DateField()
    matricula = models.IntegerField(max_length=6)
    # turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    def __str__(self):
        return f"Aluno: {self.nome}, CPF: {self.cpf}, Matricula: {self.matricula}"


