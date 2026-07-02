from django.shortcuts import render
from app.models import Tarefas
from datetime import date


def index(request):
    return render(request, "index.html")

def usuarios(request):

    context = {
        "hoje": date.today(),
        "licoes": Tarefas.object.all()

    }
    return render(request, "usuarios.html", context)
