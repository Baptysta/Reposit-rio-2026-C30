senha = input("Crie uma senha: ")

tamanho = len(senha)

if tamanho > 8:
    print("Senha validada")
else:
    print("Digite uma senha com no minimo 8 digitos")