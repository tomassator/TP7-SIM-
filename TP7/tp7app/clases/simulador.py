from tp7app.clases import zapatero
from tp7app.clases import variables
from tp7app.clases import eventos
from tp7app.clases import generadorVariables
from tp7app.clases import zapatos
from tp7app.clases import clientes
from tp7app.clases import rungeKutta
from tp7app.clases import variables as v


class Simulador:

    def __init__(self, iteraciones, ver_desde, mediaL, rep_i, rep_s, ate_i, ate_s):
        self.evento = None
        self.reloj = None
        self.iteracion = 0
        self.ver_desde = ver_desde  # Desde que fila se va a ver el vector
        self.iteraciones = iteraciones

        # Tiempos para cambio de eventos
        self.proxima_llegada = None
        self.fin_atencion_cliente = None
        self.fin_reparacion = None
        self.llegada_interrupcion = None
        self.fin_interrupcion = None

        # MediasDistribuciones
        self.media_llegadas = mediaL
        self.reparacion_inf = rep_i
        self.reparacion_sup = rep_s
        self.atencion_inf = ate_i
        self.atencion_sup = ate_s

        # Tiempos entre eventos
        self.tiempo_entre_llegadas = None
        self.tiempo_reparacion = None
        self.tiempo_atencion = None
        self.tiempo_entre_interrupciones = None
        self.tiempo_interrupcion = None
        self.tiempo_secado = 0.192  # Este tiempo se le suma al tiempo de reparacion y es calculado a traves de un runge kutta de 4to orden. Se lo inicializa en 0.40 para probar

        # variablesEstadisticas

        self.ac_zapatos_terminados = 0
        self.ac_clientes_abandonan = 0
        self.ac_pedidos_efectuados = 0
        self.ac_retiros_efectuados = 0

        # Banderas

        self.bandera_inicializacion = True
        self.bandera_zapateria_abierta = True
        self.bandera_eliminar_cliente_abandono = False

        # Objetos
        self.zapatero = zapatero.Zapatero()
        self.obj_evento = eventos.Evento()

        # Randoms que se utilizaron en los calculos
        self.rnd_llegadas = None
        self.rnd_atencion = None
        self.rnd_accion_cliente = None
        self.rnd_reparacion = None

        #Acumuladores para identificar id de zapatos y clientes que ingresan, zapatos disponibles en el momento
        self.nro_zapato = 0
        self.nro_cliente = 0
        self.zapatos_disponibles_retiro = 10

        #OBJETOS TEMPORALES QUE SE VAN A MOSTRAR EN LAS ITERACIONES DETERMINADAS
        self.clientes_actuales = []
        self.zapatos_actuales = []
        self.zapato_a_reparar = None
        self.cliente_abandono = None

        #Otros atributos que se deben mostrar en el vector
        self.accion_cliente = None
        self.clientes = []
        self.zapatos = []

        #atributos para mostrar en pantalla
        self.estados_c = []
        self.estados_z = []

    # Funcion que efectua la simulacion
    # LA SIMULACION ARRANCA A LAS 8AM ES DECIR ARRANCA ATENDIENDO
    def simular(self):
        self.vector_resultado = []

        for i in range(0, self.iteraciones):

            #Seteamos a valor default las variables que se ejecutan una sola linea y no se arrastran
            self.accion_cliente = v.fuera_sistema
            self.rnd_accion_cliente = v.fuera_sistema
            self.rnd_llegadas = v.fuera_sistema
            self.tiempo_entre_llegadas = v.fuera_sistema
            self.rnd_reparacion = v.fuera_sistema
            self.tiempo_reparacion = v.fuera_sistema
            self.rnd_atencion = v.fuera_sistema
            self.tiempo_atencion = v.fuera_sistema
            self.tiempo_interrupcion = v.fuera_sistema
            self.tiempo_entre_interrupciones = v.fuera_sistema


            if not self.bandera_inicializacion:

                self.iteracion += 1    #Incrementamos la iteracion
                #Determinamos el proximo evento
                proximo_evento = self.obj_evento.determinarSigEvento(self.proxima_llegada, self.fin_atencion_cliente, self.fin_reparacion, self.llegada_interrupcion, self.fin_interrupcion)
                #Sacamos la accion del cliente


                #Checkeamos si en la iteracion anterior algun cliente abandono
                if self.bandera_eliminar_cliente_abandono:
                    self.clientes.remove(self.cliente_abandono)
                    self.bandera_eliminar_cliente_abandono = False

                #EVENTO LLEGADA CLIENTES
                ####
                ####
                if proximo_evento == v.eventoLlegadaClientes:

                    # Incrementamos el numero de cliente y posteriormente creamos el objeto cliente y le asinamos su numero
                    self.nro_cliente += 1
                    cliente_llega = clientes.Clientes()
                    cliente_llega.set_nro(self.nro_cliente)

                    #Actualizamos el reloj y evento
                    self.evento = v.eventoLlegadaClientes + "(" + str(self.nro_cliente) + ")"
                    self.reloj = self.proxima_llegada
                    #Calculamos la proxima llegada
                    self.rnd_llegadas, self.tiempo_entre_llegadas = generadorVariables.rnd_exponencial(self.media_llegadas)
                    self.proxima_llegada = round(self.tiempo_entre_llegadas + self.reloj,3)

                    #agregamos al cliente a un arreglo para tenerlo en el sistemas hasta que se vaya
                    self.clientes.append(cliente_llega)
                    self.rnd_accion_cliente, self.accion_cliente = cliente_llega.determinar_accion()


                    #SI VIENE A BUSCAR ZAPATOS Y NO HAY SE RETIRA
                    if self.accion_cliente == v.retirar and self.zapatos_disponibles_retiro == 0:
                        self.cliente_abandono = cliente_llega
                        self.cliente_abandono.set_estado(v.abandono_sin_zapato)
                        self.bandera_eliminar_cliente_abandono = True
                        self.ac_clientes_abandonan += 1




                    #Verificamos que el zapatero este libre y a su vez que no haya cola de clientes
                    elif ((self.zapatero.estado == v.libre) or (self.zapatero.estado == v.reparando)) and len(self.zapatero.colaClientes) == 0:

                        #Si el cliente viene a retirar le reservamos el zapato
                        if self.accion_cliente == v.retirar:
                            self.zapatos_disponibles_retiro -= 1

                        #Determinamos el fin de atencion del cliente
                        self.rnd_atencion, self.tiempo_atencion = generadorVariables.rnd_uniforme(self.atencion_inf, self.atencion_sup)  #Le mandamos los limites del intervalo
                        self.fin_atencion_cliente = round(self.reloj + self.tiempo_atencion,3)

                        # DEJAMOS EN ESPERA LA REPARACION QUE SE ESTABA EFECTUANDO EN ESE MOMENTO
                        if self.zapatero.estado == v.reparando:
                            self.zapatero.set_tiempo_reparacion(self.fin_reparacion - self.reloj)
                            self.zapato_a_reparar.set_estado(v.esperando_reanudacion_reparacion)
                            self.fin_reparacion = round(
                                self.fin_atencion_cliente + self.zapatero.get_tiempo_reparacion(), 3)

                        # Determinamos el nuevo estado del zapatero
                        self.zapatero.determinar_estado_llegada(self.accion_cliente)
                        # Determinamos el estado del cliente
                        cliente_llega.determinar_estado_atencion(self.accion_cliente)

                        #FALTA LA ACCION DE CUANDO LLEGA UN CLIENTE Y UN ZAPATO SE ESTA REPARANDO.
                        #FALTA LA ACCION DEL CLIENTE QUE SE VA POR NO HABER ZAPATOS
                        #REVISAR LA ACCION ANTERIOR PARA CADA EVENTO
                    #Si va a cola...
                    else:
                        # Si el cliente viene a retirar le reservamos el zapato
                        if self.accion_cliente == v.retirar:
                            self.zapatos_disponibles_retiro -= 1

                        self.zapatero.colaClientes.append(cliente_llega)
                        cliente_llega.determinar_estado_cola(self.accion_cliente)

#################EVENTO FIN DE ATENCION DE CLIENTES##################################################################
                #####
                #####
                elif proximo_evento == v.eventoFinAtencionCliente:
                    #Vemos que vino a hacer el cliente
                    cliente_fuera = self.clientes.pop(0)

                    # Seteamos el reloj y evento
                    self.evento = v.eventoFinAtencionCliente + "(" + str(cliente_fuera.nro) +")"
                    self.reloj = self.fin_atencion_cliente

                    if cliente_fuera.estado == v.siendo_at_pedido:
                        #Acumulamos var estadistica
                        self.ac_pedidos_efectuados += 1
                        self.nro_zapato +=1
                        #Agregamos su pedido reparacion de zapatos
                        zapato_nuevo = zapatos.Zapato()
                        zapato_nuevo.set_nro(self.nro_zapato)
                        zapato_nuevo.set_estado(v.esperando_reparo)
                        self.zapatos.append(zapato_nuevo)
                        self.zapatero.colaZapatos.append(zapato_nuevo)


                    elif cliente_fuera.estado == v.siendo_at_retiro:
                        # Acumulamos var estadistica
                        self.ac_retiros_efectuados += 1
                        # Se retira un zapato

                        self.zapatos.pop(0)




                    # ¿Hay gente en cola?

                    if len(self.zapatero.colaClientes) != 0:
                        cliente_entra = self.zapatero.colaClientes.pop(0)
                        #Vemos que esperaba el cliente que estaba en cola y seteamos su respectivo estado, lo mismo para el zapatero
                        if cliente_entra.estado == v.esperando_retiro:
                            cliente_entra.set_estado(v.siendo_at_retiro)
                            self.zapatero.set_estado(v.atendiendo_retiro)
                        elif cliente_entra.estado == v.esperando_pedido:
                            cliente_entra.set_estado(v.siendo_at_pedido)
                            self.zapatero.set_estado(v.atendiendo_pedido)

                        #Calculamos el fin de atencion
                        self.rnd_atencion, self.tiempo_atencion = generadorVariables.rnd_uniforme(self.atencion_inf, self.atencion_sup)
                        self.fin_atencion_cliente = round(self.reloj + self.tiempo_atencion,3)

                        #Si entra un nuevo cliente y habia un zapato esperando su reperacion debe actualizarse su fin de reparacion
                        if self.zapato_a_reparar != None:
                            self.fin_reparacion = self.fin_atencion_cliente + self.zapatero.get_tiempo_reparacion()


                    #Si hay zapatos en cola o habia algun zapato reparandose.....
                    elif len(self.zapatero.colaZapatos) != 0 or (self.zapato_a_reparar != None):
                        #Seteamos el fin de atencion y nuevo estado de zapatero
                        self.zapatero.set_estado(v.reparando)
                        self.fin_atencion_cliente = v.fuera_sistema
                        #Vemos si habia algun zapato en reparacion y le devolvemos su estado y seteamos el tiempo restante de separacion
                        if self.zapato_a_reparar != None:
                            self.zapato_a_reparar.set_estado(v.siendo_reparados)
                            self.zapatero.set_tiempo_reparacion(0)
                        else:
                            # Calculo de fin de reparacion
                            # Sacamos zapato de cola y le asignamos estado de reparando
                            self.zapato_a_reparar = self.zapatero.colaZapatos.pop(0)
                            self.zapato_a_reparar.set_estado(v.siendo_reparados)
                            self.rnd_reparacion, self.tiempo_reparacion = generadorVariables.rnd_uniforme(
                                self.reparacion_inf, self.reparacion_sup)
                            self.fin_reparacion = round(self.reloj + self.tiempo_reparacion + self.tiempo_secado,3)


                    #Si no hay gente en cola tanto clientes como de zapatos....
                    else:
                        self.zapatero.set_estado(v.libre)
                        self.fin_atencion_cliente = v.fuera_sistema
                        self.zapato_a_reparar = None



#################EVENTO FIN DE ATENCION DE REPARACION##################################################################
                #####
                #####
                elif proximo_evento == v.eventoFinReparacion:
                    #seteamos reloj y evento
                    self.evento = v.eventoFinReparacion + "(" + str(self.zapato_a_reparar.nro) + ")"
                    self.reloj = self.fin_reparacion
                    self.zapatero.set_tiempo_reparacion(0)

                    #Acumulamos var estadistica
                    self.ac_zapatos_terminados += 1
                    self.zapatos_disponibles_retiro += 1
                    #Seteamos estado del zapato
                    self.zapato_a_reparar.set_estado(v.reparados)

                    #Vemos si hay zapatos en cola para reparar
                    if len(self.zapatero.colaZapatos) != 0:
                        #Obtenemos el nuevo zapato a reparar
                        self.zapato_a_reparar = self.zapatero.colaZapatos.pop(0)
                        #seteamos el estado de el zapato que sale de la cola
                        self.zapato_a_reparar.set_estado(v.siendo_reparados)
                        #calculamos el fin de reparacion
                        self.rnd_reparacion, self.tiempo_reparacion = generadorVariables.rnd_uniforme(self.reparacion_inf, self.reparacion_sup)
                        self.fin_reparacion = round(self.reloj + self.tiempo_secado + self.tiempo_reparacion,3)

                    #Si no hay zapatos en cola
                    else:
                        #seteamos estado del zapatero
                        self.zapatero.set_estado(v.libre)
                        self.fin_reparacion = v.fuera_sistema
                        self.zapato_a_reparar = None







#INICIALIZACION
            else:
                self.bandera_inicializacion = False
                # SE SETEAN TODOS LOS VALORES DE INICIALIZACION
                self.reloj = 0
                self.evento = self.obj_evento.eventoInicializacion
                # Seteamos los 10 zapatos iniciales
                for i in range(0, 10):
                    self.nro_zapato += 1

                    zapato = zapatos.Zapato()
                    zapato.set_estado(v.reparados)
                    zapato.set_nro(self.nro_zapato)
                    self.zapatos.append(zapato)
                # Determinamos tiempo entre llegadas
                self.rnd_llegadas, self.tiempo_entre_llegadas = generadorVariables.rnd_exponencial(self.media_llegadas)
                # Determinamos proxima llegada
                self.proxima_llegada = self.tiempo_entre_llegadas + self.reloj
                # Determinamos la llegada interrupcion
                self.llegada_interrupcion = None  # A las 8 horas de arrancada la simulacion deja de recibir pedidos #SE SETEA EN NONE POR CUESTIONES DE PRUEBA
                # Inicializamos las variables estadisticas
                self.ac_zapatos_terminados = 10
                self.ac_clientes_abandonan = 0
                self.ac_pedidos_efectuados = 0
                self.ac_retiros_efectuados = 0

                #seteamos estados
                self.fin_reparacion = v.fuera_sistema
                self.fin_atencion_cliente = v.fuera_sistema
                self.fin_interrupcion = v.fuera_sistema #En el vector se ve como apertura del local




            #AGREGAMOS LA FILA AL VECTOR
            if (self.ver_desde <= self.iteracion <= self.ver_desde + 400) or (self.iteracion == self.iteraciones - 1):

                #Capturamos los datos de los clientes
                for cli in self.clientes:
                    if not self.clientes_actuales.__contains__(cli.nro):
                        self.clientes_actuales.append(cli.nro)

                self.estados_c = ["-"]*len(self.clientes_actuales)
                for cli in self.clientes:
                    indice = self.clientes_actuales.index(cli.nro)
                    self.estados_c[indice] = cli.estado

                #Capturamos los datos de los zapatos
                for zap in self.zapatos:
                    if not self.zapatos_actuales.__contains__(zap.nro):
                        self.zapatos_actuales.append(zap.nro)

                self.estados_z = ["-"]*len(self.zapatos_actuales)
                for zap in self.zapatos:
                    indice = self.zapatos_actuales.index(zap.nro)
                    self.estados_z[indice] = zap.estado




                self.vector_resultado.append([self.evento,                                   #0
                                         self.reloj,                                    #1
                                         self.rnd_llegadas,                             #2
                                         self.tiempo_entre_llegadas,                    #3
                                         self.proxima_llegada,                          #4
                                         self.rnd_accion_cliente,                       #5
                                         self.accion_cliente,                           #6
                                         self.rnd_atencion,                             #7
                                         self.tiempo_atencion,                          #8
                                         self.fin_atencion_cliente,                     #9
                                         self.tiempo_secado,                            #10
                                         self.rnd_reparacion,                           #11
                                         self.tiempo_reparacion,                        #12
                                         self.fin_reparacion,                           #13
                                         self.tiempo_entre_interrupciones,              #14
                                         self.llegada_interrupcion,                     #15
                                         self.tiempo_interrupcion,                      #16
                                         self.fin_interrupcion,                         #17
                                         self.zapatero.get_estado(),                    #18
                                         self.zapatero.get_long_cola_clientes(),        #19
                                         self.zapatero.get_long_cola_zapatos(),         #20
                                         self.zapatero.get_tiempo_reparacion(),         #21
                                         self.ac_zapatos_terminados,                    #22
                                         self.ac_clientes_abandonan,                    #23
                                         self.ac_pedidos_efectuados,                    #24
                                         self.ac_retiros_efectuados,                    #25
                                         self.estados_c,                                 #26   Modificar para que en el arreglo se muestren los que se tienen que mostrar. Hacer una snapshot en cada iteracion
                                         self.estados_z,                                  #27  Idem que anterior
                                         self.iteracion,                                #28
                                         self.zapatos_disponibles_retiro,               #29
                                        ])

        return self.vector_resultado