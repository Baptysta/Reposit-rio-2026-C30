def media_total(numeroA, numeroB):
    n1 = float(input("Digite um numero A:"))
    n2 = float(input("Digite um numero B:"))
    total = 0
    notas = [n1,n2]
    for num in notas:
        total += num
        media = n1 + n2 / 2
        maior = max(notas)
        menor = min(notas)

    return total, media, maior, menor
resultado = media_total()

media_total (resultado)







    