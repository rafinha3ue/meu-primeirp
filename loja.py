preco = float(input("dijite o valor do produto:"))
if preco >=100:
    desconto = preco * 0.10
    print(preco -desconto )
elif preco < 100:
    desconto = preco *0.05
    print(preco -desconto)
