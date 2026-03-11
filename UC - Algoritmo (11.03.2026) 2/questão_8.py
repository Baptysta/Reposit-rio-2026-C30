compra = float(input("Digite o valor da sua compra"))

desconto_5 = compra * 0.05
desconto_10 = compra * 0.10
desconto_15 = compra * 0.15

if compra < 100:
    print(f"Sua compra é de: {compra}. Você não possui desconto")
elif compra >= 100 and compra < 500:
    print(f"Sua compra é de: {compra} .Você tem 5% de desconto e sua compra fica no valor de: ", compra - desconto_5)
elif compra >= 500 and compra < 1000:
    print(f"Sua compra é de: {compra}. Você tem 10% de desconto e sua compra fica no valor de: ", compra - desconto_10)
else:
    print(f"Sua compra é de: {compra}. Você tem 15% de desconto e sua compra fica no valor de: ", compra - desconto_15)