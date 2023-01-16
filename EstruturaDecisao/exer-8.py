"""Faça um programa que pergunte o preço de três produtos e informe
qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato."""
def linha():
    print("-" * 50)
linha()
produto1 = input("Digite o nome do produto: ").title()
valor1 = float(input("Digite o primeiro valor: R$  "))
produto2 = input("Digite o nome do produto: ").title()
valor2 = float(input("Digite o segundo valor:R$   "))
produto3 = input("Digite o nome do produto: ").title()
valor3 = float(input("Digite o terceiro valor:R$  "))
linha()
if valor1 < valor2 and valor1 < valor3:
    linha()
    print(f"O valor do produto 1:  R$ {valor1} {produto1} é o mais barato. ")
if valor2 < valor1 and valor2 < valor3:
    linha()
    print(f"O valor do produto 2:  R$ {valor2} {produto2} é o mais barato. ")
if valor3 < valor1 and valor3 < valor2:
    linha()
    print(f"O valor do produto 3:  R$ {valor3} {produto3} é o mais barato. ")
