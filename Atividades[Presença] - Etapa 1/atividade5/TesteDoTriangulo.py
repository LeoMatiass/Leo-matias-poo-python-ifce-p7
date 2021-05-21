from VerificaçãoDoTriangulo import verificar
print('escreva 3 lados de um triângulo e eu falarei se esses lados formam um triângulo')
lado1 = int(input("primeiro lado do triângulo é: "))
lado2 = int(input("segundo lado do triângulo é: "))
lado3 = int(input("terceiro lado do triângulo é: "))
VerificaçãoDoTriangulo = verificar(lado1, lado2, lado3)
print("------------------------------------------")
if VerificaçãoDoTriangulo:
    print('os lados formam um triângulo')
else:
    print('os lados não formam um triângulo')
