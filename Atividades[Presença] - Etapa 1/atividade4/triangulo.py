lado1 = int(input("primeiro lado do triangulo é: "))
lado2 = int(input("segundo lado do triangulo é: "))
lado3 = int(input("terceiro lado do triangulo é: "))
print("---------------------------------")
if (lado1 > (lado2+lado3)):   
    print('esses lados não formam triangulo')
if lado1 == lado2 and lado2 == lado3:
    print('O triângulo é equilátero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('O triângulo é isósceles')
else:
    print('O triângulo é escaleno')