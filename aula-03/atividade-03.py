class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0 
    def acelerar(self):
        self.velocidade = self.velocidade + 10
    def frear(self):
        self.velocidade = self.velocidade - 10
        if self.velocidade < 0:
            self.velocidade = 0
meu_carro = Carro("New Beetle", "Volkswagen")
meu_carro.acelerar()
meu_carro.acelerar()
meu_carro.acelerar()
meu_carro.frear()
print(meu_carro.velocidade)