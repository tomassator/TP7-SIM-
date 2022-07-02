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


        #REFORMATEAMOS PARA PODER MOSTRAR LOS ESTADOS DE LOS OBJETOS
        vector_estados_cliente = []
        #VEMOS CUANTOS CLIENTES HAY QUE MOSTRAR EN EL VECTOR (LOS CLIENTES QUE INGRESARON A LA SIMULACION DURANTE EL INTERVALO PEDIDO)
        longitud_clientes = len(simulacion.clientes_actuales)
        #CREAMOS UN VECTOR QUE TENGA TANTOS ESTADOS PARA TODOS LOS CLIENTES
        for i in range(0, len(simulacion.vector_resultado)):
            vector_estados_cliente.append(["-"]*longitud_clientes)


        #ASIGNAMOS DE FORMA MATRICIAL LOS ESTADOS
        nro_fila = -1
        #RECORREMOS CADA FILA DEL VECTOR RESULTADO
        for fila in simulacion.vector_resultado:
            nro_fila += 1
            nro_estado = -1
            #RECORREMOS CADA ESTADO DE LA ITERACION INDICADA
            for estado in fila[26]:
                nro_estado += 1
                #ASIGNAMOS EL ESTADO CORRESPONDIENTE, LOS CLIENTES QUE AUN NO APARECIERON YA TIENEN ASIGNADO EL "-" QUE ASIGNAMOS EN LA CREACION DE ESTE VECTOR
                vector_estados_cliente[nro_fila][nro_estado]=estado
            #REFORMATEAMOS ESE VECTOR PARA QUE SE MUESTRE CORRECTAMENTE
            fila[26] = vector_estados_cliente[nro_fila]












        return render(request, "resoluciontp7.html", {"vector": vam, "clientes":simulacion.clientes_actuales, "zapatos": simulacion.zapatos_actuales, "verdesde":int(verDesde)})