from datetime import datetime
from pipes import Template
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):    
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :")

def diaDeHoy(request):

    dia = datetime.now()
    documentoDeTexto = f"Hoy es dia: <br> {dia}"
    return HttpResponse(documentoDeTexto)    

def miNombreEs(self, nombre):

    documentDeTexto = f"Mi nombre es: <br><br> {nombre}"

    return HttpResponse(documentDeTexto)

def probandoTemplate(self):

    miHtml= open("C:/CoderHouse/Django-Porfolio(parte1)/Django---Porfolio-parte-1-/codigo/proyectocoder/plantillas/template1.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)


        