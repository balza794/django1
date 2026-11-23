from django.urls import path
from .views import home,articoloDetailView,giornalistaDetailView,lista_articoli,query_base

app_name = "news"

urlpatterns = [
    path("", home, name="index"),
    path("lista_articoli/", lista_articoli, name="lista_articoli"),
    path("lista_articoli/<int:pk>/", lista_articoli, name="lista_articoli_giornalista"),
    path("articoli/<int:pk>/", articoloDetailView, name="articolo_detail"),
    path("giornalisti/<int:pk>/", giornalistaDetailView, name="giornalista_detail"),
    path("query/", query_base, name="queryBase"),
]