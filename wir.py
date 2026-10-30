saldo = 100
saque = int(input("informe o valor q deseja saquar:"))
if saldo >= saque:
    print("pode saque")
elif saque <= -0:
    print("nao pode saque")
else:
    print("nao pode saquar:")