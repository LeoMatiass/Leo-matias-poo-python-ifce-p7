pilha = []
for x in range(1, 6):
    pilha.insert(0, x)
for x in range(5, 1, -1):
    print(pilha)
    pilha.pop(0)
print(pilha)