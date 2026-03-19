pontos = float(input("Digite quantos pontos você tem:"))
derrota = int(input("Dgite quantas derrotas você teve:"))
def rank_jogador(pontos, derrotas):
    pontuacao = pontos - (derrotas * 10)
    
    if pontuacao < 100:
        print("Seu grau é bronze")
    elif pontuacao < 300:
        print("Seu grau é prata")
    elif pontuacao < 600:
        print("Seu grau é ouro")
    elif pontuacao >= 600:
        print("Seu grau é diamante")
    elif pontuacao < 0:
        print("Você foi banido")
    else:
        return "tente outra vez"
    
    rank_jogador(pontos, derrotas)