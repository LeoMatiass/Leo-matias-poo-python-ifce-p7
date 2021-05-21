from conta import *
class conta_corrente(conta):
    def __init__(self,numero,saldo,limite):
        super().__init__(numero,saldo)
        self._limite = limite
    def getLimite(self):
        return self._limite
    def setLimite(self,limite):
        self._limite = limite
    def sacar(self,valor):
        if valor < self.getSaldo() + self.getLimite():
            self._saldo -= valor
            return True
        else:
            return False