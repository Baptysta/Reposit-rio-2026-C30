idade = int(input("Digite sua idade"))

if idade < 12:
    print("Sua categoria é infantil")
elif idade >= 12 and idade < 18:
    print("Sua categoria é juvenil")
elif idade >= 18 and idade < 60:
    print("Sua categoria é adulto")
else: 
    print("Sua categoria é sênior")
    
