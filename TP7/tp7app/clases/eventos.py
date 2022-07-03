from tp7app.clases import variables as v

class Evento:

    def __init__(self):
        self.eventoInicializacion = v.eventoInicializacion
        self.eventoLlegadaClientes = v.eventoLlegadaClientes
        self.eventoFinAtencionCliente = v.eventoFinAtencionCliente
        self.eventoFinReparacion = v.eventoFinReparacion
        self.eventoLlegadaInterrupcion = v.eventoLlegadaInterrupcion
        self.eventoFinInterrupcion = v.eventoFinInterrupcion
        self.banderaPrimeraIteracion = True



    # Los parametros son todos los tiempos que indican cuando va a ocurrir un evento
    # Devuelve el nombre de el tiempo que se va a ejecutar primero
    def determinarSigEvento(self, tiempoL, tiempoFAC, tiempoFR, tiempoI, tiempoFI):


        if not self.banderaPrimeraIteracion:
            minimo = 100000000000

            try:
                if tiempoL < minimo:
                    minimo = tiempoL
                    evento = self.eventoLlegadaClientes
            except:
                pass
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
            self.banderaPrimeraIteracion = False
            return self.eventoLlegadaClientes
