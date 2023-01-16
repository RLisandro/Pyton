"""  Faça um Programa que leia um número e exiba o dia correspondente da semana. 
1-Domingo, 2- Segunda, etc., se digitar outro valor deve
aparecer valor inválido"""
def linha():
    print("-"*50)
linha()
semana = int(input(f"\n1-  2 - 3 -  4 - 5 - 6 - 7"
        f"\n\tDigite um número para saber o dia da semana correspondente:  "))
if semana == 1:
    linha()
    print(f"Você digitou o número {semana} que corresponde a Domingo. ")
elif semana == 2:
    linha()
    print(f"Você digitou o número {semana} que corresponde a Segunda - Feira. ")
elif semana == 3:
    linha()
    print(f"Você digitou {semana} que corresponde a Terça - Feira. ")
elif semana  == 4:
    linha()
    print(f"Você digitou {semana} que corresponde a Quarta - Feira.")
elif semana == 5:
    linha()
    print(f"Você digitou {semana} que corresponde a Quinta - Feira.")
elif semana == 6:
    linha()
    print(f"Você digitou {semana} que corresponde a Sexta - Feira.")
elif semana == 7:
    linha()
    print(f"Você digitou {semana} que corresponde a Sábado.")