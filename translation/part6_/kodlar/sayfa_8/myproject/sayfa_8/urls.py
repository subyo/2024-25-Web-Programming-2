
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ana sayfaya yönlendirme
]

from django.shortcuts import render

def index(request):
    return render(request, 'sayfa_8/index.html')
