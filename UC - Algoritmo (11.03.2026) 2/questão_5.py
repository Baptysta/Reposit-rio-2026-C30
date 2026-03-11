nome = input("Digite o nome do aluno: ")
matricula = int(input("Digite a matricula do aluno: "))
notaA = float(input("Digite a nota A do aluno: "))
notaB = float(input("Digite a nota B do aluno: "))

media = (notaA + notaB) / 2

print(f"O nome do aluno é: ", nome)
print(f"A matricula do aluno é: ", matricula)
print(f"A média do aluno é: ", media)