from django. urls import path
from .views import home, articoloDetailView, lista_articoli
app_name = "news"

urlpatterns =[
    path("", home, name="homeview"),
    path("articoli/<int:pk>", articoloDetailView, name="lista_articoli"),
    path("lista_articoli/", lista_articoli, name="articoloDetailView"),
    path("lista_articoli/<int:pk>", articoloDetailView, name="lista_articoli_giornalista")
]   