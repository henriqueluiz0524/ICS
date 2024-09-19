import random

#Gera números aleatorio

def jogo_de_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas = 0
    
    print("Bem-vindo ao jogo de adivinhação!")
    
    while True:
        palpite = int(input("Digite um número entre 1 e 10: "))
        tentativas += 1
        
        if palpite == numero_secreto:
            print("Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas!")
            break
        elif palpite < numero_secreto:
            print("O número secreto é maior. Tente novamente.")
        else:
            print("O número secreto é menor. Tente novamente.")

jogo_de_adivinhacao()