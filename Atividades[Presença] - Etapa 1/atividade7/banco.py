from agencia import *
from cliente import *
from conta import *
from conta_corrente import *
from conta_popanca import *
conta = conta()
cliente = cliente()
ag = agencia()
while True:
    print("1 - Cadastra Cliente \n2 - Cadastrar Nova conta a cliente já existente \n3 - Acessar conta de cliente \n4 - Sair do sistema")
    n = int(input())
    if n == 1:
        conta.setNumero(int(input("Numero da conta:")))
        cliente.setNome(input("Nome do cliente:"))
        cliente.setCPF(input("CPF do cliente:"))
        ag.addCliente(cliente)
        cliente.addConta(conta)
    elif n == 2:
        busca = ag.buscaCliente(input("Informe CPF do cliente:"))
        if busca:
            print("1 - Conta corrente: \n2 - Conta poupança:")
            n = int(input())
            if n == 1:
                busca = cliente.buscaContas(input("Numero da conta:"))
                if busca:
                    numero = busca
                    limite = int(input("Limite da conta:"))
                    conta_corrente = conta_corrente(numero, conta.getSaldo(), limite)

            elif n == 2:
                rendimento = conta_popanca.setRendimento(0.03)  # Rendimento padrão da conta poupança
                conta_popanca = conta_corrente(conta.getNumero(), conta.getSaldo(), rendimento)
            else:
                print("Conta informada não existe")
        else:
            print("Cliente não possui conta no banco")
    elif n == 3:
        busca = cliente.buscaContas(int(input("Numero da conta:")))
        if busca:
            print("1 - Sacar \n2 - Depositar \n3 - Realizar transferencia \n4 - Saldo")
            n = int(input())
            if n == 1:
                conta.sacar(float(input("Valor do saque:")))
            elif n == 2:
                conta.despositar(float(input("Valor do deposito:")))
            elif n == 3:
                numero = int(input("Numero da conta para transferencia:"))
                valor = float(input("Valor da transferencia:"))
                conta.transferencia(valor,numero)
            elif n == 4:
                print("Saldo:",conta.getSaldo())
        else:
            print("Conta informada não existe")
    elif n == 4:
        break
    else:
        print("Valor invalido")