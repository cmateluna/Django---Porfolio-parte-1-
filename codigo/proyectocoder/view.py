from datetime import datetime
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template import Template, Context, loader

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

    nom = "Nicolas"
    ap = "Perez"

    listaDeNotas = [2,2,3,7,2,5]

    diccionario = {"nombre":nom, "apellido":ap, "hoy":datetime.now(), "notas":listaDeNotas} # Para enviar el contexto

    # miHtml= open("C:/CoderHouse/Django-Porfolio(parte1)/Django---Porfolio-parte-1-/codigo/proyectocoder/plantillas/template1.html")

    # plantilla = Template(miHtml.read()) # Se carga en memoria nuestro documento, template1.html
    #                                     # importar template y contex, con: from django.template import Template, Context  

    # miHtml.close() # Cerramos el archivo

    # miContexto = Context(diccionario) # Le doy al contexto mi nombre y apellido

    # documento = plantilla.render(miContexto) # Aca renderizamos la plantilla en documento

    plantilla = loader.get_template("template1.html")

    documento = plantilla.render(diccionario) 

    return HttpResponse(documento)      