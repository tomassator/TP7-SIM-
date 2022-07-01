from tp7app.clases import variables as v

class Zapato:

    def __init__(self):
        self.estado = v.fuera_sistema
        self.nro = 0



    def get_estado(self):
        return self.estado


    def set_estado(self, estado):
        self.estado = estado

    def set_nro(self, nro):
        self.nro = nro

    def get_nro(self):
        return self.nro