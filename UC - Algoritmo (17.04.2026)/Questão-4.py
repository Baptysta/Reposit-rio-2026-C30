#4. Crie uma função que receba o peso e altura de uma pessoa (para academia) e categorize o IMC: magro (24.9). Use if-else e try-except para entradas inválidas.


peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura"))

try:
    total = peso / (altura ** 2)

    if total < 24.9:
        print("você está acima do peso")
    else:
        print("Você está magro")
        
except TypeError:
    print("Digite um valor válido")