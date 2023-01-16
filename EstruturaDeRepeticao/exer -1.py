"""  1.	Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o
usuário informe um valor válido."""
print("----------------------------------------------")
while True:
    nota = float(input("Digite sua nota: "))
    if nota <  0 or  nota > 10:
        print(f"Sua nota é {nota} Inválida.\n Somente números entre 0 e 10.")
    else:
        print(f"Sua nota é {nota}. Valor Válido!")
        break
        