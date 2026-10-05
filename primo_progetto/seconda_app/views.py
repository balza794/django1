from django.shortcuts import render

# Create your views here.
def es_if(request):
    #https://www.decodejava.com/django-template-if-tag.htm
    #Creating a dictionary of key-value pairs

    dic = { 'var1' : 200,
    'var2' : 200,
    'var3' : 300}

    #Calling the render() method to render the request from es_if.html page by using the dictionary, dic
    return render(request, "seconda_app/es_if.html", dic)

def if_else_elif(request):
    dic = { 'var1' : 200,
    'var2' : 200,
    'var3' : 300}

    return render(request, "seconda_app/if_else_elif.html", dic)
