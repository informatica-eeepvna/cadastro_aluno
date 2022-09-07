from django.db import models
import datetime

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.BigIntegerField()
    dtnasc = models.DateField(default=datetime.date.today)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nome}"


