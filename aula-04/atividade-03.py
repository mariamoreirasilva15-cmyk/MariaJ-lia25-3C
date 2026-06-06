class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0 
    def get_saldo(self):
        return self.__saldo
    def depositar(self, valor):
        if valor > 0:
            self.__saldo = self.__saldo + valor
        else:
            print("Erro: Deposite um valor positivo")
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo = self.__saldo - valor
        else:
            print("Erro: Saldo insuficiente")
    def extrato(self):
        print(self.__titular)
        print(self.__saldo)
conta = ContaBancaria("gretchen")
conta.depositar(100)
conta.sacar(30)
conta.extrato()
