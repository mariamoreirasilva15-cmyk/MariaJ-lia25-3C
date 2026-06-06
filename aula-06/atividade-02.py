class Instrumento:
    def tocar(self):
        print("Som de instrumento")

class Violao(Instrumento):
    def tocar(self):
        print("Blém blém")

class Bateria(Instrumento):
    def tocar(self):
        print("Tum dum tás")

class Piano(Instrumento):
    def tocar(self):
        print("Plim plim")

instrumentos = [Violao(), Bateria(), Piano()]
for i in instrumentos:
    i.tocar()
    