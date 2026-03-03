n1=int(input("Digite um número"))

if n1<0:
    print("Número inválido")
elif n1 %2 ==0:
    quadrado=n1*n1
    print(f"Seu número é par sendo o quadrado {quadrado}")
else:
    cubo=n1*n1*n1
    print(f"Seu número é ímpar sendo seu cubo {cubo}")
