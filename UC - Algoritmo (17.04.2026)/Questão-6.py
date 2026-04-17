def temperaturas():
    temp = []

    try:
        for i in range (1, 8):
            entrada = float(input(f"Digite a temperatura {i}: "))
            temp.append(entrada)

        media = sum(temp) / len(temp)

        print(media)

    except ValueError:
        print("Erro: As temperaturas devem ser numéricas.")

temperaturas()