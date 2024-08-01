from django.urls import path
from .views import obter_intervalos

urlpatterns = [
    path('intervalos/', obter_intervalos, name='obter_intervalos'),
]
