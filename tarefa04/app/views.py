from django.shortcuts import render

from datetime import date


def index(request):
    return render(request, "index.html")

def usuarios(request):

    context = {
        "hoje": date.today(),

    }
    return render(request, "usuarios.html", context)
