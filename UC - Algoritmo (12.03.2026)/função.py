print("Python é fácil")
print("Python é fácil")
print("Python é fácil")

def exibirMensagem():
    print("Olá, mundx!")

exibirMensagem()

def saudar(nome):
    print(f"Olá, {nome}!")

saudar("Ana")
saudar("Bruno")

def exibirMensagem(nome, mensagem):
    print((f"{mensagem}, {nome}"))

exibirMensagem("Ana", "Bom dia")

exibirMensagem(nome = "Bruno", mensagem = "Novidades no brincando com Rosa")

def calculadoraMedia(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

resultado = calculadoraMedia(8.0, 9.0)
print(f"Média: {resultado}")





