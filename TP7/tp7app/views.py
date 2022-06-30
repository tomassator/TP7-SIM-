from django.shortcuts import render

# Create your views here.



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



    return render(request, "resoluciontp7.html")