""" 13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa
um algoritmo que calcule seu peso ideal.
Para mulheres: (62.1*h) - 44.7
   """
print("------------------------------------------------------------------------")
alturah = float(input("Digite sua altura - Homem: "))
alturam = float(input("Digite sua altura - Mulheres: "))
pesoh = (72.7 * alturah) - 58
pesom = (62.1 * alturam) - 44.7
print(f"Segunda sua ,homem,  altura {alturah} o peso ideal : {pesoh:,.2f} Kg")
print(f"Segundo sua , mulher, altura {alturam} o peso ideal: {pesom:,.2f} Kg")