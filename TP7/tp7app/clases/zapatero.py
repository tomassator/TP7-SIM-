from tp7app.clases import variables as v

class Zapatero:

    def __init__(self):
        self.colaPedidos = []
        self.colaRetiros = []
        self.zapatos = []
        self.estado = v.libre


    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def get_cola_pedidos(self):
        return self.colaPedidos

    def get_cola_retiros(self):
        return self.colaRetiros

    def get_zapatos(self):
        return self.zapatos



    def agregar_cola_pedido(self, pedido):
        self.colaPedidos.append(pedido)

    def sacar_cola_pedido(self, pedido):
        self.colaPedidos.append(pedido)

    def agregar_cola_retiro(self, retiro):
        self.colaRetiros.append(retiro)

    def sacar_cola_retiro(self, retiro):
        self.colaRetiros.remove(retiro)

    def agregar_zapato(self, zapato):
        self.zapatos.remove(zapato)

    def sacar_zapato(self, zapato):
        self.zapatos.remove(zapato)