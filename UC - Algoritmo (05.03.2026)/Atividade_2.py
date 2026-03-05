import random

numeros = [91, 34, 67, 15, 82]
print("lista original:",numeros)

numeros.sort()
print("Apos sort():",numeros)


numeros.sort(reverse=True)
print("Apos sort():",numeros)

numeros3 = [6, 7, 8, 9, 10]
print("lista 2 original:",numeros3)

random.shuffle(numeros3)
print("lista embaralhada:",numeros3)
