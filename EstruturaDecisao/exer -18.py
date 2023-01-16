"""Faça um Programa que peça uma data no formato dd/mm/aaaa e 
determine se a mesma é uma data válida.    """
def linha():
    print("-"*50)
linha()
dia = int(input("Digite o dia do ano : "))
mes = int(input("Digite o mês do ano: "))
ano = int(input("Digite o ano: "))
if dia > 31:
    linha()
    print(f"Você digitou {dia} dia inválido.")
if mes > 12:
    linha()
    print(f"Você digitou {mes} dia inválido.")
if ano % 4 == 0:
    linha()
    print(f"O ano {ano } é ano bissexto")
if dia < 32 and mes < 13:
    linha()
    print (f"Data: {dia} / {mes} / {ano} ")
