""" Faça um programa que lê as duas notas parciais obtidas por um 
aluno numa disciplina ao longo de um semestre, e calcule a sua média. A
atribuição de conceitos obedece à tabela abaixo:
> Média de Aproveitamento                          Conceito
> Entre 9.0 e 10.0                                              A
> Entre 7.5 e 9.0                                                B
> Entre 6.0 e 7.5                                                C
> Entre 4.0 e 6.0                                                D
> Entre 4.0 e zero                                              E
O algoritmo deve mostrar na tela as notas, a média, o conceito 
correspondente e a mensagem “APROVADO” se o conceito for A,
B ou C ou “REPROVADO” se o conceito for D ou E.  """
print("___________________________________________________________________\n")
nota1 = float(input("\n\tDigite a primeira nota de geografia: "))
nota2 = float(input("\n\tDigite a segunda nota de geografia: "))
media = (nota1 + nota2)  / 2
print("___________________________________________________________________\n")
if media == 9 or 10 :
    print("\n\tMédia de Aproveitamento    \t\t Conceito")
    print(f"\n\t{media}   \t\t\t\t \t A \n\n\t APROVADO")
if media == 7 or 9:
    print("\n\tMédia de Aproveitamento    \t\t Conceito")
    print(f"\n\t{media}   \t\t\t\t \t A \n\n\t APROVADO")
if media == 6 or 7.5:
    print("\n\tMédia de Aproveitamento    \t\t Conceito")
    print(f"\n\t{media}   \t\t\t\t \t A \n\n\t APROVADO")
if media == 4 or 6:
  print("\n\tMédia de Aproveitamento    \t\t Conceito")
  print(f"\n\t{media}   \t\t\t\t \t A \n\n\t REPROVADO")
if media == 4 or 0:
     print("\n\tMédia de Aproveitamento    \t\t Conceito")
     print(f"\n\t{media}   \t\t\t\t \t A \n\n\t REPROVADO")
