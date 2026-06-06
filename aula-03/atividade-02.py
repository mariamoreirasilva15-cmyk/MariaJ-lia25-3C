class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def desconto(self, porcentagem):
        valor_desconto = self.preco * (porcentagem / 100)
        return self.preco - valor_desconto
p = Produto("mp3.2000", 100.0)
print(p.desconto(10))