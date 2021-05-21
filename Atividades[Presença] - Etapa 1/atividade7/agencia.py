from cliente import *
class agencia:
    def __init__(self,num_agencia=1):
        self._num_agencia = num_agencia
        self._clientes = []
    def addCliente(self,cliente):
        self._clientes.append(cliente)
    def buscaCliente(self,cpf):
        busca = ""
        for i in self._clientes:
            if i.getCPF() == cpf:
                busca += "Cliente:" + i.getNome() + "\nCPF:" + i.getCPF()
                return busca
            else:
                return False
