from django.shortcuts import render

from django.http import HttpResponse
import datetime

# Create your views here.

def display(request):
    return HttpResponse("<h1>Hola mundo!</h1>")

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Fecha y hora actual: </b>" + str(dt)
    return HttpResponse(s)


def Formulario(request):
    b ="<h1>Bienvenido</h1> <br>"
    f ="<p1>Usuario</p1> <br>"
    c ="<input></input> <br>"
    g ="<p1>Contraseña</p1> <br>"
    l ="<input></input><br> <br>"
    p ="<button>ingresar</button>"
    a = [b,f,c,g,l,p]
    return HttpResponse(a)
