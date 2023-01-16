"""Faça um Programa que leia três números e mostre o maior e o menor deles."""
def linha():
    print("-" * 50)
linha()
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
linha()
if n1 > n2 and n1 > n3:
    linha()
    print(f"O número n1: {n1} é maior que n2: {n2} e n3: {n3}. ")
if n2 > n1 and n2 > n3:
    linha()
    print(f"O número n2: {n2} é maior que n1: {n1} e n3: {n3}. ")
if n3 > n1 and n3 > n2:
    linha()
    print(f"O número n3: {n3} é maior que n1: {n1} e n2: {n2}. ")
if n1 < n2 and n1 < n3:
    linha()
    print(f"O número n1: {n1} é menor que n2: {n2} e n3: {n3}. ")
if n2 < n1 and n2 < n3:
    linha()
    print(f"O número n2: {n2} é menor que n1: {n1} e n3: {n3}. ")
if n3 < n1 and n3 < n2:
    linha()
    print(f"O número n3: {n3} é menor que n1: {n1} e n2: {n2}. ")
