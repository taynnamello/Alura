import Forca
import advinhacao

def escolhe_jogo():
    print("Escolha o Jogo!")
    print("(1) Forca (2) Advinhacao")

    jogo = int(input("Qual Jogo?"))

    if(jogo==1):
        print("Jogando Forca")
        Forca.jogar()
    elif(jogo==2):
        print("Jogando Advinhação")
        advinhacao.jogar()
if (__name__== "__main__"):
    escolhe_jogo()