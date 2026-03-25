def calculadora():

    while True:
        print("DIgite 1 para adição")
        print("DIgite 2 para subtração")
        print("DIgite 3 para multiplicação")
        print("DIgite 4 para divisão")
        print("DIgite 0 para sair")

        opicao = int(input("Digite sua opção:"))

        a = float(input("Digite numero A:"))
        b = float(input("Digite numero B:"))

        match opicao:
            case 0:
                print("Sair")
            case 1:
                print(f"O resultado é {a + b}")
            case 2:
                print(f"O resultado é {a - b}")
            case 3:
                print(f"O resultado é {a * b}")
            case 4:
                print(f"O resultado é {a / b}")
            case _:
                print("Opição inválida")

calculadora ()
