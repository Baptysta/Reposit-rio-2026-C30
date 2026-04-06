import random

inteiro = random.randint(1, 100)
tentavivas = 0
acertou = False

while not acertou:
    try:
        numero = int(input("Digite um número:"))
        tentavivas += 1

        if numero == inteiro:
            print("Acertou")
            acertou = True
        elif numero < inteiro:
            print("Muito baixo")
        else:
            print("Muito alto")
        
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
print(f"Você acertou com {tentavivas} tentativas")



