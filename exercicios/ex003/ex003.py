class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depositos
    """

    def __init__(self, id, titular, saldo = 0):
        self.id = id
        self.titular = titular
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}")

    def __str__(self):
        return f"Conta Bancaria do numero {self.id} que tem o titular {self.titular} e saldo de R${self.saldo:,.2f} de saldo"

    def deposito(self, valor):
        self.saldo += valor
        print(f"Deposito de R${valor:,.2f} \033[32mautorizado\033[0m na conta {self.id}")

    def saque(self, valor):
        if self.saldo < valor:
            print(f"Saque \033[31mNEGADO\033[0m de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")

c1 = ContaBancaria(123, 'Mateus', 250)
c1.deposito(300)
c1.saque(100)
c1.saque(500)
print(c1)