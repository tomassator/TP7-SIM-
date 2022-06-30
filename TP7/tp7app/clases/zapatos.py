from tp7app.clases import variables as v

class Zapato:

    def __init__(self):
        self.estado = v.fuera_sistema




    def get_estado(self):
        return self.estado


    def set_estado(self, estado):
        self.estado = estado