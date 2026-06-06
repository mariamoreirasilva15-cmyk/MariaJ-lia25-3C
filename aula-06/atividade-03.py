class Forma:
    def area(self):
        return 0

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

minhas_formas = [Triangulo(4, 5), Quadrado(6)]

for f in minhas_formas:
    print(f.area())
   