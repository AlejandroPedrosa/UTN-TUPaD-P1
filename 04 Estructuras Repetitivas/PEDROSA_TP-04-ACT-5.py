#Actividad 5:  Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
secreto = random.randint(0, 9)
intentos = 0

while True:
    guess = int(input("Adivina el número (0 a 9): "))
    intentos += 1
    if guess == secreto:
        print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")
        break