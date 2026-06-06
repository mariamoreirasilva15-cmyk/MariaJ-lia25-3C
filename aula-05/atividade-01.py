class Animal:
    def __init__(self, nome):
        self.nome = nome
    def comer(self):
        print(f"{self.nome} está comendo")
class Cachorro(Animal):
    def latir(self):
        print("Au Au!")
meu_dog = Cachorro("fuleco")
meu_dog.comer()
meu_dog.latir()