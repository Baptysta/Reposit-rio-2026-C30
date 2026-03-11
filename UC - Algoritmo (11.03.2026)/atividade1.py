aluno = {}

aluno["nome"] = input("Qual o nome do aluno: ")
aluno["nota1"] = input("Qual a nota 1 do aluno: ")
aluno["nota2"] = input("Qual a nota 2 do aluno: ")

media = (aluno["nota1"] + aluno["nota2"]) / 2

if media >= 7:
    print("passou")
elif media >= 5:
    print("média")
else:
    print("reprovou")

print("Nome: ", aluno["nome"])
print("Nota 1 do aluno: ", aluno["nota1"])
print("Nota 2 do aluno: ", aluno["nota2"])
print(f"A média do aluno é: {media}")


