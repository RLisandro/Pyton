"""Faça um programa que recebe o salário de um colaborador e o reajuste 
segundo o seguinte critério, baseado no salário atual- R$ 200,00 :

a - salários até R$ 280,00 (incluindo) : aumento de 20%
b- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
c- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
d- salários de R$ 1500,00 em diante : aumento de 5%
Após o aumento ser realizado, informe na tela:
e -  salário antes do reajuste;
f -  percentual de aumento aplicado;
g -  valor do aumento;
h -  novo salário, após o aumento """
def linha():
    print("-"*60)  
linha()
salarioatual = 200
salario = float(input("Digite valor do seu salário:R$  "))
if salario < salarioatual:
    linha()
    print("Sua informação está abaixo do salário base. ") 
if salario >= salarioatual and salario <= 280:
    reajuste1 =(salario * 20 / 100)  + salario 
    linha()
    print(f" Seu salário é : R$ {salario} \nVocê teve um aumento de 20%. "
    f"Seu salário atual é de: R$ {reajuste1} ")
if salario >= 280  and salario <=700: 
    reajuste2 = (salario * 15 / 100) + salario 
    linha()
    print(f" Seu salário é : R$ {salario} \nVocê teve um aumento de 15%. "
    f"Seu salário atual é de: R$ {reajuste2} ")
    linha()
if salario >= 700 and salario <=1500:
    reajuste3 = (salario * 10 /100) + salario
    linha()
    print(f" Seu salário é : R$ {salario} \nVocê teve um aumento de 10%. "
    f"Seu salário atual é de: R$ {reajuste3} ")
    linha()
if salario >1500:
     reajuste4 = (salario * 5 /100) + salario
     linha()
     print(f"\n Seu salário é : R$ {salario}\n\nVocê teve um aumento de 5%.\n "
     f"\nSeu salário atual é de: R$ {reajuste4} ")
    