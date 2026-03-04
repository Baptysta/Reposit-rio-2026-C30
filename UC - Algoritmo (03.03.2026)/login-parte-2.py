senha = "123456"
tentativa = 3
nome = input("Digite seu nome: ")

while tentativa > 0:
    senha_usuario = input("Digite sua senha: ")

if senha_usuario == senha:
    print(f"Olá,{nome}, seja bem-vindo ao nosso banco!")
else:
    tentativa -= 1
    if tentativa == 2:
        print("Sua senha está incorreta, você possui mais 2 tentativas.")
    elif tentativa == 1:
        print("Sua senha está incorreta, você possui apenas 1 tentativa.")
    else:
        print("Sua senha foi bloqueada!")


