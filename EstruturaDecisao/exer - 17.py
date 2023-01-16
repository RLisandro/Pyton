"""Faça um Programa que peça um número correspondente a um
determinado ano e em seguida informe se este ano é ou não bissexto.     """
print("-------------------------------------------------------------------------------------------------------------\n\t")
ano = int(input("Digite o ano para saber se é  bissexto: "))
if ano % 4 == 0:
    print(f"O ano {ano} é bissexto")
if ano % 400 == 0:
    print(f"O ano {ano} é bissexto")
if ano % 100 == 0:
    print(f"O ano {ano}  não é bissexto")
print("")
    
    


    
    
    
