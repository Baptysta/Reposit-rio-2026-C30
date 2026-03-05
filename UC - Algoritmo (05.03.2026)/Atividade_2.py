numeros = [91, 34, 67, 15, 82]
print("Lista original: ", numeros)

numeros.sort()
print("Após sort()", numeros)

numeros.sort(reverse=True)
print("Após sort(): ", numeros)

numeros3 = [6, 7, 8, 9, 10]
print("Lista 2 original: ", numeros3)

random.shuffle(numeros)