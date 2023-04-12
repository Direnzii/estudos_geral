print("*******************\nAdivinhe o numero\n*******************")
numero_correto = 50
tentativas = 3
rodada = 1

for chutes in range(1, tentativas + 1):
    print("Tentativa {} de {}".format(chutes, tentativas))
    chute = input("Digite o seu chute: ")
    chute = int(chute)

    correto = chute == numero_correto
    maior =   chute >  numero_correto
    menor =   chute <  numero_correto

    try:
        if correto:
            print("Você acertou!!")
            break
        else:
            if maior:
                print("Seu chute foi maior que o numero correto!!")
            elif menor:
                print("Seu chute foi menor que o numero correto!!")

    rodada = rodada + 1
print("FIM!!")