from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Articolo, Giornalista

'''
def homr(request):
    return HttpResponse("<h1>Homepage news! </h1>")

def home(request) :

    a = ""
    g = ""
    for art in Articolo.objects.all():
        a += (art.titolo + "<br>")

    for gio in Giornalista.objects.all():
        g += (gio.nome + "<br>")
    response = "Articoli :< br>" + a + "<br>Giornalisti :< br>" + g

    return HttpResponse("<h1>" + response + "</h1>")

def home (request):
    a = []
    g = []
    for art in Articolo.objects.all():
        a.append(art.titolo)

    for gio in Giornalista.objects.all():
        g. append (gio. nome)

    response = str(a) + "<br>" + str(g)
    print(response)

    return HttpResponse("<h1>" + response + "</h1>")
'''
def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "news/homepage.html", context)

def articoloDetailView(request, pk):
    articolo = Articolo.objects.get(pk=pk)
    context = {"articolo": articolo}
    return render(request, "news/articolo_detail.html", context)

def lista_articoli(request, pk=None):
    # 2. Interrogazione al database (Query):
    # Filtriamo il modello Articolo prendendo solo quelli il cui campo 'giornalista'
    # corrisponde al giornalista appena recuperato.
    if pk is None:
        articoli = Articolo.objects.all()
        giornalista = None
    else:
        giornalista = get_object_or_404(Giornalista, pk=pk)
        articoli = Articolo.objects.filter(giornalista = giornalista)
    
    # In alternativa, se nel modello Articolo la ForeignKey ha un related_name o usiamo la query inversa:
    # articoli = giornalista.articolo_set.all() # oppure giornalista.articoli.all()

    # 3. Prepariamo il contesto da passare al template HTML
    context = {
        'giornalista': giornalista,
        'articoli': articoli,
    }
    
    # 4. Renderizziamo la pagina passando la richiesta, il percorso del template e il contesto
    return render(request, 'news/lista_Articoli.html', context)