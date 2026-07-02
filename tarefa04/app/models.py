from django.db import models

class Tarefas(models.Model):
    nome = models.CharField(max_length=30)
    status = models.BooleanField()
    prazo = models.DateField()

class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"

def __str__(self):
        return self.nome
        
