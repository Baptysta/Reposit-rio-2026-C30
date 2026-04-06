import random

def jogar():
    # Sorteia um número entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    # Loop principal do jogo
    while not acertou:
        try:
            # Solicita o palpite do usuário
            palpite = int(input("Digite o seu palpite: "))
            tentativas += 1

            # Verifica o palpite
            if palpite == numero_secreto:
                print(f"Parabéns! Você acertou em {tentativas} tentativas!")
                acertou = True
            elif palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            else:
                print("Muito alto! Tente novamente.")
        
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    jogar()
