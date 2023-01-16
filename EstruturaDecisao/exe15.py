#Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso  os lados formem um triângulo, se o mesmo é:
# equilátero, isósceles ou escaleno
def linha():
    print("-"*60)
linha()
lado1 = int(input("Digite o primero lado do triângulo:  "))
lado2 = int(input("Digite o segundo lado do triângulo:  "))
lado3 = int(input("Digite o terceiro lado do triângulo:  "))
linha()
if (lado1 + lado2) > lado3 or (lado2 + lado3) > lado1 or (lado3 + lado1) > lado2:
    linha()
    print( f"Os números digitados foram:\n lado1-  {lado1} , lado2-  {lado2} , lado3-  {lado3}: Triângulo")
if lado1 == lado2 and lado2 == lado3 and lado3 == lado1:
    linha()
    print(f"Os números digitados foram: \nlado1-  {lado1} , lado2-  {lado2} , lado3-  {lado3}: Triângulo Equilátero")
if lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    linha()
    print( f"Os números digitados foram: \nlado1-  {lado1} ,lado2-  {lado2} ,lado3-  {lado3}: Trângulo Isósceles " )
