def calcular_media():
    notas = []

    try:
        for i in range (1, 4):
            entrada = float(input(f"Digite a nota {i}: "))
            notas.append(entrada)

        media = sum(notas) / len(notas)

        print(f"A média final do aluno é: {media:.2f}")

    except ValueError:
        print("Erro: As notas devem ser numéricas.")

calcular_media()


def total_compra():
    try:
        preco1 = float(input("Digite o preço do primeiro produto: "))
        preco2 = float(input("Digite o preço do segundo produto: "))

        total = preco1 + preco2

        print(f"Total da compra: R$ {total:.2f}")

    except ValueError:
        print("Erro: os preços devem ser números!")

total_compra()

