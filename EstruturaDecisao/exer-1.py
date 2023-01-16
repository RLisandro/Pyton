"""1.Faça um Programa que peça dois números e imprima o maior deles. """
n1 = int(input("Digite o primeiro número: "))
n2 = int (input("Digite o segundo número: "))
if n1 > n2:    
    print(f"O número N1 {n1} é maior que o número  N2 {n2}.")
if n2 > n1:    
    print(f"O número N2 {n2} é maior que o número  N1 {n1}.")
if n1 == n2:   
    print("Os dois números são iguais.")
    