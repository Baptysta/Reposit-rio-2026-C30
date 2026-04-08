n = int(input("Quantas pessoas foram infectadas: "))
r = int(input("Digite o fator reprodutivo: "))
p = int(input("Digite o número alvo de pessoas infectadas: "))

dias = 0
infectados = n
total = n

while total < p:
    dias += 1 
    novos = infectados * r
    total += novos
    infectados = novos

print(f"Número de dias é igual a {dias}")




