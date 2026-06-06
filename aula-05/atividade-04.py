class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        print(f"Aluno: {self.nome} | Idade: {self.idade} | Matrícula: {self.matricula}")

class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def presentar(self):
        print(f"Prof: {self.nome} | Idade: {self.idade} | Salário: {self.salario}")

a1 = Aluno("Blair Waldorf", 22, "10000")
p1 = Professor("Chuck Bass", 22, 90000)

lista_pessoas = [a1, p1]
for pessoa in lista_pessoas:
    pessoa.apresentar()