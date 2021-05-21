class conta:
    def __init__(self,numero = 0, saldo = 0):
        self._numero = numero
        self._saldo = saldo
    def setNumero(self,numero):
        self._numero = numero
    def getNumero(self):
        return self._numero
    def getSaldo(self):
        return self._saldo
    def sacar(self,saque):
        if self._saldo >= saque:
            self._saldo -= saque
            return True
        else:
            return False
    def despositar(self,deposito):
        self._saldo += deposito
    def transferencia(self,valor,numero_conta):
        if self._saldo > valor:
            self._saldo -= valor