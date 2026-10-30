secreto = 7
chute = int(input("dijite sei chute:"))

if secreto==chute :
    print("acertou")
elif chute < secreto:
    print("muito baixo")
elif chute > secreto:
    print("muito auto")