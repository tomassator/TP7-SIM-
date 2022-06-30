
class Evento:

    def __init__(self):
        self.eventoInicializacion = "inicializacion"
        self.eventoLlegadaClientes = "llegada_cliente"
        self.eventoFinAtencionCliente = "fin_atencion_cliente"
        self.eventoFinReparacion = "fin_reparacion"
        self.eventoLlegadaInterrupcion = "llegada_interrupcion_pedidos"
        self.eventoFinInterrupcion = "fin_interrupcion"
        self.banderaPrimeraIteracion = True



    # Los parametros son todos los tiempos que indican cuando va a ocurrir un evento
    # Devuelve el nombre de el tiempo que se va a ejecutar primero
    def determinarSigEvento(self, tiempoL, tiempoFAC, tiempoFR, tiempoI, tiempoFI):


        if not self.banderaPrimeraIteracion:
            evento = self.eventoLlegadaClientes
            minimo = tiempoL

            try:
                if tiempoFAC < minimo:
                    minimo = tiempoFAC
                    evento = self.eventoFinAtencionCliente
            except:
                pass

            try:
                if tiempoI < minimo:
                    minimo = tiempoI
                    evento = self.eventoLlegadaInterrupcion
            except:
                pass

            try:
                if tiempoFR < minimo:
                    minimo = tiempoFR
                    evento = self.eventoFinReparacion
            except:
                pass

            try:
                if tiempoFI < minimo:
                    minimo = tiempoFI
                    evento = self.eventoFinInterrupcion
            except:
                pass

            return evento


        else:
            return self.eventoLlegadaClientes
