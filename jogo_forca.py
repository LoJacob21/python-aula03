import random

palavras = ["Tigre" , 
            "Melancia" , 
            "Carro", 
            "Safari", 
            "Girafa",
            "Amarelo",
            "Formiga",
            "Bolo",
            "Cama",
            "Clube",
            "Doce",
            "Escola",
            "Pijama",
            "Rato"
            ]
palavra = random.choice(palavras)

# print(f"A palavra sorteada foi: {palavra}")

letras_user = []
chances = 10
ganhou = False

while True:

    for letra in palavra:
        if letra.lower() in letras_user:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print(f"Você tem {chances} chances")
    tentativa = input("Informe uma letra para advinhar: ")     
    letras_user.append(tentativa.lower())    

    if tentativa.lower() not in palavra.lower():
        chances -= 1

    ganhou = True

    for letra in palavra:
        if letra.lower() not in letras_user:
            ganhou = False
    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"Parabéns você venceu!! A palavra era: {palavra}")
else:
    print(f"Game Over !! A palavra era: {palavra}")