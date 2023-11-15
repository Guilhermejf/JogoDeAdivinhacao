import random

jogador = 0
computador = 0

print("---- Vamos jogar ----")
min = int(input("Valor minimo: "))
max = int(input("Valor maximo: "))

while (True):
    
    aleatorio = random.randint(min,max)
    valor = input("advinhe o valor entre "+str(min)+" e "+str(max)+": " )


    if (int(valor) == aleatorio):
        jogador = jogador + 1
        print("Acertou !")
        print("Placar Jogador: "+str(jogador)+" computador " + str(computador))        
    else:
        computador = computador + 1
        print("Errou !")
        print("Valor: "+str(aleatorio))
        print("Placar Jogador: "+str(jogador)+" computador " + str(computador))

    if jogador == 10 or computador == 10:
        print("Placar Final Jogador: "+str(jogador)+" computador " + str(computador))
        exit()
