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
        self.tiempo_secado = 0.40  # Este tiempo se le suma al tiempo de reparacion y es calculado a traves de un runge kutta de 4to orden. Se lo inicializa en 0.40 para probar

        # variablesEstadisticas

        self.ac_zapatos_terminados = 0
        self.ac_clientes_abandonan = 0
        self.ac_pedidos_efectuados = 0
        self.ac_retiros_efectuados = 0

        # Banderas

        self.bandera_inicializacion = True

        # Objetos
        self.zapatero = zapatero.Zapatero()
        self.obj_evento = eventos.Evento()

        # Randoms que se utilizaron en los calculos
        self.rnd_llegadas = None
        self.rnd_atencion = None
        self.rnd_accion_cliente = None
        self.rnd_reparacion = None

        #Acumuladores para identificar id de zapatos y clientes que ingresan
        self.nro_zapato = 0
        self.nro_cliente = 0

        #Otros atributos que se deben mostrar en el vector
        self.accion_cliente = None
        self.clientes = []
        self.zapatos = []

    # Funcion que efectua la simulacion
    # LA SIMULACION ARRANCA A LAS 8AM ES DECIR ARRANCA ATENDIENDO
    def simular(self):

        vector_resultado = []

        for i in range(0, self.iteraciones):


            if not self.bandera_inicializacion:

                self.iteracion += 1    #Incrementamos la iteracion
                pass






            else:
                # SE SETEAN TODOS LOS VALORES DE INICIALIZACION
                self.reloj = 0
                self.bandera_inicializacion = False
                self.evento = self.obj_evento.eventoInicializacion
                # Seteamos los 10 zapatos iniciales
                for i in range(0, 10):
                    self.nro_zapato += 1

                    zapato = zapatos.Zapato()
                    zapato.set_estado(v.reparados)
                    zapato.set_nro(self.nro_zapato)
                    self.zapatos.append(zapato)
                # Determinamos tiempo entre llegadas
                self.tiempo_entre_llegadas = generadorVariables.rnd_exponencial(self.media_llegadas)
                # Determinamos proxima llegada
                self.proxima_llegada = self.tiempo_entre_llegadas + self.reloj
                # Determinamos la llegada interrupcion
                self.llegada_interrupcion = 8  # A las 8 horas de arrancada la simulacion deja de recibir pedidos
                # Inicializamos las variables estadisticas
                self.ac_zapatos_terminados = 10
                self.ac_clientes_abandonan = 0
                self.ac_pedidos_efectuados = 0
                self.ac_retiros_efectuados = 0




            #AGREGAMOS LA FILA AL VECTOR
            if (self.ver_desde <= self.iteracion <= self.ver_desde + 400) or (self.iteracion == self.iteraciones - 1):
                vector_resultado.append([self.evento,                                   #0
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
                                         self.zapatero.get_long_cola_retiros(),         #19
                                         self.zapatero.get_long_cola_pedidos(),         #20
                                         self.zapatero.get_long_cola_zapatos(),         #21
                                         self.zapatero.get_tiempo_reparacion(),         #22
                                         self.ac_zapatos_terminados,                    #23
                                         self.ac_clientes_abandonan,                    #24
                                         self.ac_pedidos_efectuados,                    #25
                                         self.ac_retiros_efectuados,                    #26
                                         self.clientes,                                 #27   Modificar para que en el arreglo se muestren los que se tienen que mostrar. Hacer una snapshot en cada iteracion
                                         self.zapatos,                                  #28  Idem que anterior
                                         self.iteracion,                                #29
                                        ])

        return vector_resultado