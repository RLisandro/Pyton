"""3.	Faça um programa que leia e valide as seguintes informações:
a.	Nome: maior que 3 caracteres;
b.	Idade: entre 0 e 150;
c.	Salário: maior que zero;
d.	Sexo: 'f' ou 'm';
e.	Estado Civil: 's', 'c', 'v', 'd';"""
print("\n-----------------------------------------------------")
while True:
    nome = input("Digite seu nome seu : ").title()
    idade = int(input("Digite sua idade: "))
    salario = float(input("Digite sua salário: "))
    sexo = input("Digite (F)-Feminino, (M)-Masculino (H) - Homossexual: ").title()
    estciv = input("Digite seu estado civil (S)- Solteiro (C) - Casado (V) - Viúvo (D)- Divorciado:  ").title()
    sair = input("Para sair do sistema aperte 0 - zero ou Enter para continuar!: ").title()
    if sair == '0':
        break 
    if  (len(nome)) > 3 :
        print( )
    if   (len(nome)) < 3 :
        print("Somente nome com mais de 3 caracteres! ")
    if idade > 0 or   idade < 151 :
        print( )
    if salario > 0 :
        print( )
    if sexo == 'M':
        print(  )
    elif sexo == 'F':
        print( )
    if sexo == 'H':
        print( )
    if estciv == 'S':
        print( )
    if estciv == 'C':
        print( )
    if estciv == 'V':
         print( )
    if estciv == 'D':
        print( )
print(f"\n\tSeu cadastrado:\n\tNome: {nome}\n\tIdade: {idade} anos\n\t"
          f"Salário: R$ {salario}\n\tSexo: {sexo}\n\tEstado Civil: {estciv}\n\t")
            
        