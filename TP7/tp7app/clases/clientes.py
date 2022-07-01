from tp7app.clases import variables as v

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
