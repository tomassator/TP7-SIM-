from tp7app.clases import variables as v
from tp7app.clases import zapatos
from tp7app.clases import clientes

class Zapatero:

    def __init__(self):
        self.colaClientes = []
        self.colaZapatos = []
        self.estado = v.libre
        self.tiempo_restante_reparacion = 0


    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def get_cola_Clientes(self):
        return self.colaClientes


    def get_cola_zapatos(self):
        return self.colaZapatos

    def get_long_cola_clientes(self):
        return len(self.colaClientes)


    def get_long_cola_zapatos(self):
        return len(self.colaZapatos)

    def get_tiempo_reparacion(self):
        return self.tiempo_restante_reparacion

    def set_tiempo_reparacion(self, tiempo):
        self.tiempo_restante_reparacion = tiempo


    def agregar_cola_clientes(self, pedido):
        self.colaClientes.append(pedido)

    def sacar_cola_clientes(self, pedido):
        self.colaClientes.remove(pedido)


    def agregar_cola_zapato(self, zapato):
        self.colaZapatos.remove(zapato)

    def sacar_cola_zapato(self, zapato):
        self.colaZapatos.remove(zapato)


    #Funcion que determina el estado del zapatero en la llegada de un nuevo cliente que va a ser atendido
    def determinar_estado_llegada(self, accion_cliente):
        if accion_cliente == v.retirar:
            self.set_estado(v.atendiendo_retiro)
        else:
            self.set_estado(v.atendiendo_pedido)

