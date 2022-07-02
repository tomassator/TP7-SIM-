from django.shortcuts import render
from tp7app.clases import simulador

# Create your views here.

def prueba(request):

    return render(request, "prueba.html")

def inicio(request):


    return render(request, "inicio.html")




def resoluciontp7(request):

    if request.method == "GET":

        cantidadIteraciones = request.GET["cantIteraciones"]
        verDesde = request.GET["desde"]
        mediaLlegadas = request.GET["mediaLlegadas"]
        eiReparaciones = request.GET["reparacionInferior"]
        esReparaciones = request.GET["reparacionSuperior"]
        eiAtencion = request.GET["atencionInferior"]              #Ei/Es hacen referencia a extremo inferior y superior respectivamente
        esAtencion= request.GET["atencionSuperior"]

        #Creamos el objeto que va a simular
        simulacion = simulador.Simulador( int(cantidadIteraciones), int(verDesde), float(mediaLlegadas), float(eiReparaciones)
                                         , float(esReparaciones), float(eiAtencion), float(esAtencion))

        vam = simulacion.simular()   # VAM --> Vector a mostrar



        return render(request, "resoluciontp7.html", {"vector": vam, "clientes":simulacion.clientes_actuales, "zapatos": simulacion.zapatos_actuales, "verdesde":int(verDesde)})