from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def index(request):
    return render(request, "index.html")

urlpatterns = [
    path("", include("blog.urls")),
    path("admin/", admin.site.urls),
]
