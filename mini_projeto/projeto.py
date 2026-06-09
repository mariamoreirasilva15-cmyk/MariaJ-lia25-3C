# ========================================================
# --- CLASSE MAE: GRETCHEN ---
# ========================================================
class Funcionario:
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome          
        self.matricula = matricula  
        self._salario_base = salario_base 


# ========================================================
# --- CLASSES FILHAS DA GRETCHEN ---
# ========================================================

class CLT(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        # O super() puxa o DNA da mae
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        if self._salario_base < 0:
            print("Erro: Salario nao pode ser negativo!")
            return 0.0
        return self._salario_base

    def exibir(self):
        print(f"Nome : {self.nome} | Matricula : {self.matricula} | Tipo : CLT | Salario : R$ {self.calcular_salario():.2f}")


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_base, total_vendas):
        super().__init__(nome, matricula, salario_base)
        self.total_vendas = total_vendas

    def calcular_salario(self):
        if self._salario_base < 0:
            print("Erro: Salario nao pode ser negativo!")
            return 0.0
        # Fixo + comissao de vendas
        return self._salario_base + (self.total_vendas * 0.10)

    def exibir(self):
        print(f"Nome : {self.nome} | Matricula : {self.matricula} | Tipo : Vendedor | Salario : R$ {self.calcular_salario():.2f}")


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)
        self.bonus = 1500.00 

    def calcular_salario(self):
        if self._salario_base < 0:
            print("Erro: Salario nao pode ser negativo!")
            return 0.0
        return self._salario_base + self.bonus

    def exibir(self):
        print(f"Nome : {self.nome} | Matricula : {self.matricula} | Tipo : Gerente | Salario : R$ {self.calcular_salario():.2f}")


# ========================================================
# --- CONGA LA CONGA (PROGRAMA PRINCIPAL) ---
# ========================================================

# Criando as artistas na folha de pagamento
func1 = CLT("Addison Rae", "001", 3500.00)
func2 = Vendedor("Lana Del Rey", "002", 2500.00, 15000.00) 
func3 = Gerente("Sabrina Carpenter", "003", 6000.00) 

# Colocando na lista
lista = [func1, func2, func3]

print("--- FOLHA DE PAGAMENTO: CONGA LA CONGA ---")
# O grande show do for loop
for f in lista:
    f.exibir()