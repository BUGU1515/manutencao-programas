import random

numero = random.randint(1, 20)

while True:
    palpite = int(input("Tente adivinhar o número entre 1 e 20: "))
    
    if palpite > numero:
        print("Menor")
    elif palpite < numero:
        print("Maior")
    else:
        print("Acertou!")
        break