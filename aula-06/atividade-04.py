class Pagamento:
    def processar(self, valor):
        return valor

class Dinheiro(Pagamento):
    def processar(self, valor):
        desconto = valor * 0.05
        return valor - desconto

class Cartao(Pagamento):
    def processar(self, valor):
        juros = valor * 0.02
        return valor + juros

class Pix(Pagamento):
    def processar(self, valor):
        return valor

formas = [Dinheiro(), Cartao(), Pix()]
for f in formas:
    print(f.processar(100.0))
