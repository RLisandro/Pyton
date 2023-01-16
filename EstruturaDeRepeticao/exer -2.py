"""  2.	Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome
do usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""
print("------------------------------------------------")
while True:
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    if senha == nome:
        print(f"Sua senha {senha} é igual ao nome {nome}.")
    else:
        print("Senha e nome cadastrados com sucesso!")
        break
