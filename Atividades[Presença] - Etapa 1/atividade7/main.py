from conta import *
cliente = conta()
print(cliente.getSaldo())
cliente.despositar(250)
print(cliente.getSaldo())
cliente.sacar(200)
print(cliente.getSaldo())