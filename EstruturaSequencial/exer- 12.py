""" 12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
calcule seu peso ideal. """
print("--------------------------------------------------------------------------")
altura = float(input("Digite a sua altura: "))
peso = (72.7 * altura) - 58
print(f"Segundo sua altura {altura} seu peso é: {peso:,.2f} Kg")
# :,.2f = Dois números após a vírgula. 