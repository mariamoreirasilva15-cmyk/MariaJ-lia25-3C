class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo = self.saldo + valor
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
        else:
            print("Saldo insuficiente")
    def extrato(self):
        print(self.titular)
        print(self.saldo)
conta = ContaBancaria("kelly key", 50.0)
conta.depositar(30.0)
conta.sacar(20.0)
conta.extrato()