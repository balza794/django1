from django.urls import path
from prima_app.views import homepage, welcome, lista, chi_siamo, variabili

app_name = "prima_app"
urlpatterns = [
    path('', homepage, name='homepage'),  #apici vuoti servono per visualizzare la pagina predefenita
    path('welcome', welcome, name='welcome'),
    path('lista', lista, name='lista'),
    path('chi_siamo', chi_siamo, name='chi_siamo'),
    path('variabili', variabili, name='variabili'),
]
