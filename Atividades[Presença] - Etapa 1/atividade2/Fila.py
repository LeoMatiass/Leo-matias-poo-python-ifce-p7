fila = []
print('------------------------------------------------')
for y in range (1, 5):
    print(f'A {y}a pessoa chegou na fila.')
    fila.append(y)
print('------------------------------------------------')
print(f'\nTemos {len(fila)} pessoas na fila.')
print(f'{fila}\n')
print('------------------------------------------------')
for y in range(1, 3):
    print(f'Pessoa número {y} saiu da fila')
    fila.pop(0)
print('------------------------------------------------')
print(f'Só {len(fila)} pessoas estão na fila.')
print(f'{fila}\n')
print('------------------------------------------------')