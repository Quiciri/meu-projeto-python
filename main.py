import random

def jogar():
    numero = random.randint(1, 20)
    tentativas = 0
    print("=== Jogo de Adivinhação ===")
    print("Adivinhe um número entre 1 e 20")

    while True:
        palpite = int(input("Seu palpite: "))
        tentativas += 1

        if palpite < numero:
            print("O número é MAIOR")
        elif palpite > numero:
            print("O número é MENOR")
        else:
            print(f"🎉 Acertou em {tentativas} tentativa(s)!")
            break

jogar()
#baralho
