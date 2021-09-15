import random

def jogar():
    print("Bem Vindos ao Jogo de Advinhação")

    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dificil")

    nivel = int(input("Define o nível: "))

    if(nivel==1):
        total_tentativas = 20
    elif(nivel==2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    print(numero_secreto)

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Try Again")
            continue

        acertou = chute == numero_secreto 
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("O seu chute foi maior que o número secreto")
            if (rodada == total_tentativas):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif(menor):
                print("Errou! Chute menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)/3 # função abs:o objetivo dessa função é retornar o número desconsiderando o seu sinal:
            pontos = pontos - pontos_perdidos

    print("Fim do Jogo")

if (__name__== "__main__"):
    jogar()