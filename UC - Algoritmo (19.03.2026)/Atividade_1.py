saldo = 3769,78
saque = float(input("Digite o quanto você quer sacar:"))
def saldo_final(saldo, saque):
    if saque > saldo:
        print("Saldo insuficiente")
    elif saque <= saldo:
        if saque > 1000:
            (saque * 0.02) - saque
        else:
            
