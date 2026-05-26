from django.shortcuts import render


def index(request):
    return render(request, "app/index.html")

def usuarios(request):
    
    lista_usuario = [
        {"Nome": "Iñaki Godoy", "Idade": 19, "Matricula": 20231181110019, "Cidade": "Cidade do México"},
        {"Nome": "Emily Rudd", "Idade": 19, "Matricula": 20231181110045, "Cidade": "Spring Valley"},
        {"Nome": "Jacob Gibson", "Idade": 19, "Matricula": 20231181110025, "Cidade": "Denver"},
        {"Nome": "Taz Skylar", "Idade": 19, "Matricula": 20231181110015, "Cidade": "Tenerife"},
        {"Nome": "Mackenyu", "Idade": 19, "Matricula": 20231181110020, "Cidade": "Little Tokyo"},
    ]

    context = {
        "/usuarios": lista_usuario,
    }
    return render(request, "app/usuarios.html", context)