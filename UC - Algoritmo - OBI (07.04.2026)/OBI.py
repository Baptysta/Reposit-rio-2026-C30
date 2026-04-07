P = int(input("Digite a quantidade de pães"))
D = int(input("Digite a quantidade de pães doces"))
B = int(input("Digite a quantidade de bólos"))

total = P * 1 + D * 2 + B * 3

if total >= 150:
    print("B")
elif total >= 120:
    print("D")
elif total >= 100:
    print("P")
else:
    print("N")
