class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    def __str__(self):
        return f"Titular da conta: {self.titular} | Saldo: {self.saldo}"

    def ativar_conta(self):
        self._ativo = True

conta1 = ContaBancaria("Samuel Ribeiro", 500)
conta2 = ContaBancaria("Brunna Muller", 10000)

print(conta1)
print(conta2)
conta2.ativar_conta()
print(f"Conta ativa? {conta2._ativo}")