from tp7app.clases import variables as v
from tp7app.clases import zapatos
from tp7app.clases import clientes

class Zapatero:

    def __init__(self):
        self.colaPedidos = []
        self.colaRetiros = []
        self.colaZapatos = []
        self.estado = v.libre
        self.tiempo_restante_reparacion = 0


    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def get_cola_pedidos(self):
        return self.colaPedidos

    def get_cola_retiros(self):
        return self.colaRetiros

    def get_cola_zapatos(self):
        return self.colaZapatos

    def get_long_cola_retiros(self):
        return len(self.colaRetiros)

    def get_long_cola_pedidos(self):
        return len(self.colaPedidos)

    def get_long_cola_zapatos(self):
        return len(self.colaZapatos)

    def get_tiempo_reparacion(self):
        return self.tiempo_restante_reparacion


    def agregar_cola_pedido(self, pedido):
        self.colaPedidos.append(pedido)

    def sacar_cola_pedido(self, pedido):
        self.colaPedidos.append(pedido)

    def agregar_cola_retiro(self, retiro):
        self.colaRetiros.append(retiro)

    def sacar_cola_retiro(self, retiro):
        self.colaRetiros.remove(retiro)

    def agregar_cola_zapato(self, zapato):
        self.colaZapatos.remove(zapato)

    def sacar_cola_zapato(self, zapato):
        self.colaZapatos.remove(zapato)