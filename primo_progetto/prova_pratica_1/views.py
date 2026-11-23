from django.shortcuts import render
import random

def index(request):
    return render(request,"prova_pratica_1/index.html")

def somma(request):
    var1 = var2 = 0
    var1 = random.randint(1,10)
    var2 = random.randint(1,10)
    somma = var1 + var2
    dic = {"var1" : var1 , "var2" : var2 , "somma" : somma} 
    return render(request,"prova_pratica_1/somma.html",dic )

def media(request):
    numeri = []
    for i in range(30):
        numeri.append(random.randint(1,10))
    media = 0
    somma = 0
    for i in range(30):
        somma += numeri[i]
    media = round(somma/30, 2)
    dic = {"media" : media}
    return render(request,"prova_pratica_1/media.html",dic)

def voti(request):
    dic = {"studenti" : 8 , "studente2" : "Alessio", "voto2" : 9}
    return render(request,"prova_pratica_1/voti.html",dic)