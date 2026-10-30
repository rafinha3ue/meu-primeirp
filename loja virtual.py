print("======================")
print("       RF STOR        ")
print("======================")
print("1 - camisa - 41,99")
print("2 - calca jeans - r$ 119.19")
print ("3 - tenis - R$ 199.99")
print("==========================")

opcao = input("dijite o numero q vc escolher:")

print("voce escolheu o produto :" , opcao)

if opcao == "1":
    print(" voce escolheu camisa, 41,99 :")
elif opcao == "2":
    print("voce escolheu calca jeans, 119.19")
elif opcao == "3":
    print("voce escolheu tenis, 199.99")
else :
    print("opcao invalida")