from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def lemax(request):
    return render(request, 'lemax.html')

def arbol(request):
    return render(request, 'arbol.html')

def puntasArbol(request):
    return render(request, 'puntasArbol.html')

def guirnaldas(request):
    return render(request, 'guirnaldas.html')

def belenes(request):
    return render(request, 'belenes.html')

def belenesclasicos(request):
    return render(request, 'belenesclasicos.html')

def lluville(request):
    return render(request, 'lluville.html')

def bolas(request):
    return render(request, 'bolas.html')

def luces(request):
    return render(request, 'luces.html')

def guirnaldaled(request):
    return render(request, 'guirnaldaled.html')

def cortinaled(request):
    return render(request, 'cortinaled.html')

def colecciones(request):
    return render(request, 'colecciones.html')
