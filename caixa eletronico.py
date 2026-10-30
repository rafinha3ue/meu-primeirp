saldo = float(input("qual e seu saldo:"))
saque = float(input("informe o valor do saque:"))

if saldo == 0:
    print("conta zerada")
elif saldo >= saque:
    print("saque aprovado")
else:
    print("saldo negado")