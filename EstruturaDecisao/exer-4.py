"""  4.Faça um Programa que verifique se uma letra digitada é vogal ou consoante.  """
vogal = ['a','e','i','o','u','A', 'E','I','O','U']
v = input("Digite uma letra para saber se  é uma vogal ou consoante ou [0] para finalizar: ").title()
if v in vogal:
        print(f"A letra {v } é uma vogal.")
else:
        print(f"A letra {v} é uma consoante.")
 


 