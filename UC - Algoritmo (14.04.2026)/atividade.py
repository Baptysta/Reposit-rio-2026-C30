def soma(a, b):
    try:
        return a + b
    except TypeError:
        print("Entrada inválida")
        return 0
    resp1 = soma(10, 30)
    print(f"resultado: {resp1}")
    
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print(f"Erro: Não é possível dividir por zero")
        return 0
print("Entrada inválida")
    
    