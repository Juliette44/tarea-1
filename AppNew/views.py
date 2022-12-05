from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import Template, Context, loader

def Persona(request):
    duenios= duenio(nombre="Juli", apellido="Demata", edad= "18", email= "dema.julita@gmail.com")
    duenios.save()
    duenios_texto= (f"Duenio guardado con el nombre de: {duenios.nombre}, apellido: {duenios.apellido}, edad: {duenios.edad} y email: {duenios.email}")
    return HttpResponse(duenios_texto)

def Mascota(request):
    mas= mascota(nombre= "Azzy", tipo="Perro")
    mas.save()
    mas_texto= (f"La mascota se guardo perfectamente con el nombre de: {mas.nombre}, y el tipo: {mas.tipo}")
    return HttpResponse(mas_texto)

def Paseo(request):
    pas= paseo(ultimo_paseo= "2022-12-2", realizado= True , nombre_del_paseo= "Parque")
    pas.save()
    pas_texto=(f"Se guardo exitosamente el paseo {pas.nombre_del_paseo}, realizado {pas.realizado} el dia {pas.ultimo_paseo}")
    return HttpResponse(pas_texto)

def Html(request):

    diccionario={"nombre":"Juli", "apellido": "Demata", "edad": 18, "lista": [4,3,4,6,8,10,5]}
    
    template= loader.get_template("Text.html")

    documento=template.render(diccionario)
    return HttpResponse(documento)
