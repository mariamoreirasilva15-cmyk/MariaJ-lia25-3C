class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome  
        self.__preco = preco  
    def get_nome(self):
        return self.__nome
    def get_preco(self):
        return self.__preco
    def set_nome(self, novo_nome):
        self.__nome = novo_nome
    def set_preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print("Erro: Preço não pode ser negativo")
p = Produto("Celular", 1500.0)
p.set_preco(-20)
p.set_preco(1400.0)
print(p.get_nome())
print(p.get_preco())