class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir(self):
        print(self.nome)
        print(self.salario)

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def salario_total(self):
        return self.salario + self.bonus

g = Bureau = Gerente("Rodrigo apresentador", 5000, 1500)
g.exibir()
print(g.salario_total()) 