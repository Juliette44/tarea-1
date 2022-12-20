from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import Template, Context, loader
from  AppNew.forms import *

def persona(request):
    
    return render(request, "AppNew/persona.html")

def mascota(request):
    
    return render(request, "AppNew/mascota.html")

def chequeo(request):

    return render(request, "AppNew/chequeo.html")

def html(request):

    return render(request, "AppNew/inicio.html")

def mascotaFormulario(request):

    if request.method=="POST":
        formulario_mascotas = FormularioMascota(request.POST)

        if formulario_mascotas.is_valid():
            info= formulario_mascotas.cleaned_data
            nombre= info['nombre']
            tipo= info['tipo']
            mascotas= Mascota(nombre=nombre, tipo=tipo)
            mascotas.save()
            return render(request, "AppNew/inicio.html", {"mensaje" : "Mascota guardada correctamente"})

    else:
        formulario_de_mascota = FormularioMascota ()
        context = {
            'formulario_mascotas' : formulario_de_mascota
        }
        return render(request, "AppNew/mascotaFormulario.html", context=context)

def busquedaMascota(request):
    return render(request, "AppNew/busquedaMascota.html")

def buscar(request):

        if request.GET['nombre']:

            nombre= request.GET['nombre']
            tipo= Mascota.objects.filter(nombre__icontains=nombre)
            return render(request, "AppNew/resultadosBusqueda.html", {"nombre": nombre, "tipo": tipo})
        
        else:

            respuesta= "No pusiste nada"

            return HttpResponse (respuesta)    