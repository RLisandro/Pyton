"""Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
> A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
> A mensagem "Reprovado", se a média for menor do que sete;
> A mensagem "Aprovado com Distinção", se a média for igual a dez.  """
print("-"*56)
print("Digite somente notas 0 - 10!")
print("-"*56)
nota1 = float(input("Digite a primira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2 ) / 2
if media >= 7 and media < 11:
            print(f"Aprovado com média: {media} pontos.")
if media > 10:
    print(f"Você digitou números superiores a 10 pontos!\n "
          f"ATENÇÂO")
if media < 7:
            print(f"Reprovado com média: {media} pontos. ")
if media == 10:
            print(f"Aprovado com Distinção sua média é: {media} pontos")
