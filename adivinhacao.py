import random
retorno = "S"
while(retorno == "S"):
    print("****************************************")
    print("Bem vindo no jogo de adivinhação")
    print("****************************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 3
    rodada = 1
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    while (nivel != 1 and nivel != 2 and nivel !=  3):
        print("Número invalido. Tente Novamente")
        nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #while(rodada <= total_de_tentativas):
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format (rodada, total_de_tentativas))
        numero = int(input("Digite o seu numero:"))
        while (numero < 1 or numero > 100):
            print("Tentativa inválida. Digite um novo número entre 1 e 100.")
            chute = input("Digite o seu numero: ")
            numero = int(chute)
            print("Você digitou", chute)

        if(numero < 1 or numero > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero == numero_secreto
        maior = numero > numero_secreto
        menor = numero < numero_secreto

        if(acertou):
            print ("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o numero secreto!")
            elif(menor):
                print("Você errou! O seu chute foi menor que o numero secreto!")
            pontos_perdidos = abs(numero_secreto - numero)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")
    retorno = input("Tentar Novamente? (S/N)")

