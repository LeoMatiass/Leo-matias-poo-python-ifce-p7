from conta import *
class conta_popanca(conta):
    def __init__(self,numero,saldo,rendimento):
        super().__init__(numero,saldo)
        self._rendimento = rendimento
    def getRendimento(self):
        return self._rendimento
    def setRendimento(self,rendimento):
        self._rendimento = rendimento
    def aplicaRendimento(self):
        self._saldo += self._saldo * self._rendimento