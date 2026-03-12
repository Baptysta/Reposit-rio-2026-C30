valorporhora = float(input("Digite o valor por hora"))
hora = float(input("Digite as horas trabalhadas"))

def calcularSalario(valorpohora, hora):
    salario = valorporhora * hora
    return salario

resultado = calcularSalario(valorporhora, hora)
print(f"Seu salário é: {resultado}")


