"""Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a
mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""
def linha():
    print("-"*50)
linha()
turno = input(f"\n>M-Matutino\n>V-Vespertino\n>N- Noturno"
              f"\n\tEm qual turno você estuda?  ").title()
if turno == 'M':
    linha()
    print("Bom Dia! Estudante!")
if turno == 'V':
    linha()
    print("Boa Tarde! Estudante!")
if turno == 'N':
    linha()
    print("Boa Noite! Estudante!")
