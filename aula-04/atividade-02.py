class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
    def get_nome(self):
        return self.__nome
    def set_nome(self, novo_nome):
        if novo_nome != "": 
            self.__nome = novo_nome
        else:
            print("Erro: nome nao pode ser vazio")
    def get_idade(self):
        return self.__idade
    def set_idada(self, nova_idade):
        if nova_idade >= 0 and nova_idade <= 120:
            self.__idade = nova_idade
        else:
            print("Erro: idade invalida")
    def apresentar(self):
        print(self.__nome)
        print(self.__idade)
alguem = Pessoa("mana sama", 2000)
alguem.set_nome("") 
alguem.apresentar() 