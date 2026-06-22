from django.db import models

class Tarefas(models.Model):
    nome = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    prazo = models.CharField(max_length=30)
