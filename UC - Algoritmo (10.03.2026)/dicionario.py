matricula = 2026001
nome1 = "Ana Silva"
Telephone= "987890269"

aluno = {
    "matricula": 2026001,
    "nome": "Ana Silva",
    "Telephone": "987890269"
}

print(aluno)

contato = {
    "@camilaqueiroz": "Camila Queiroz",
    "@brunamarquezine": "Bruna Marquezine",
    "@sheronmenezes": "Sheron Menezes",
    "@paolaoliveira": "Paola Oliveira"
}

print(contato)
print(type(contato))

print(contato["@camilaqueiroz"])

print(contato.get("@paolaoliveira"))
print(contato.get("@inexistente"))
print(contato.get("@inexistente", "Não encontrado"))

contato["@giovanna"] = "Giovanna"
print("Após add: ", contato)

contato["@paolaoliveira"] = "Paola Oliveira"
print("Após add: ", contato)

contato.update({
    "@brunamarquezine": "Bruna Marquezine",
    "@camilaqueiroz": "Camila Q."
})

print("Após atualização: ", contato)

removido = contato.pop("@paolaoliveira")
print(f"Removido: {removido}")
print("Após o pop: ", contato)

del contato["@camilaqueiroz"]
print("Após o del: ", contato)

copia = dict(contato)
contato.clear()
print("Após clear: ", contato)
print("Cópia: ", copia)