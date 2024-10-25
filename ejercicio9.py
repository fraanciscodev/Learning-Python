# 9. Adivina el Número
# Escribe un programa donde el usuario debe adivinar un número entre 1 y 10.

import random

numero_secreto = random.randint(1, 10)
print (numero_secreto)
adivina = int(input("Adivina un número entre 1 y 10: "))

if adivina == numero_secreto:
    print("¡Felicidades! Adivinaste el número.")
else:
    print(f"Lo siento, el número era {numero_secreto}.")

