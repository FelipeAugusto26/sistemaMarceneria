from django.urls import path
from .views import autenticar

urlpatterns= [
    path('', autenticar, name='entrar')
]