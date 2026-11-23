from django.urls import path
from prova_pratica_1.views import index, somma, media, voti

app_name = "prova_pratica_1"
urlpatterns = [
    path('', index, name='index'),  #apici vuoti servono per visualizzare la pagina predefenita
    path('somma', somma, name='somma'),
    path('media', media, name='media'),
    path('voti', voti, name='voti'),
]
