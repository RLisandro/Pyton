"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""
def linha():
    print("-" * 50)
linha()
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
linha()
if n3 < n2 and n2 < n1:
    linha()
    print(f"Ordem decrescente n3: {n3} , n2: {n2} e n1: {n1}")
if n2 < n1 and n1 < n3:
    linha()
    print(f"Ordem decrescente n3: {n3} , n1: {n1} e n2: {n2}")

if n1 < n2 and n2 < n3:
    linha()
    print(f"Ordem decrescente n3: {n3} , n2: {n2} e n1: {n1}")
# Refazer 
