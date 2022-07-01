from tp7app.clases import variables as v
import random

class Clientes:

    def __init__(self):
        self.nro = 0
        self.estado = v.fuera_sistema

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

    def set_nro(self, nro):
        self.nro = nro

    def get_nro(self):
        return self.nro


    #Determina que accion va a ejecutar el cliente
    def determinar_accion(self):
        a = random.random()
        if a < 0.49:
            return round(a,3), v.retirar
        else:
            return round(a,3), v.pedido

    #Determinar estado del cliente cuando esta siendo atendido
    def determinar_estado_atencion(self, accion):
        if accion == v.pedido:
            self.set_estado(v.siendo_at_pedido)
        else:
            self.set_estado(v.siendo_at_retiro)

    def determinar_estado_cola(self, accion):
        if accion == v.pedido:
            self.set_estado(v.esperando_pedido)
        else:
            self.set_estado(v.esperando_retiro)

