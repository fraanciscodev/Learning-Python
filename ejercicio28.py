# 28. Juego del Piedra, Papel o Tijera
# Implementa el juego de Piedra, Papel o Tijera entre el usuario y la computadora.

import random

opciones = ["piedra", "papel", "tijera"]
usuario = input("Elige piedra, papel o tijera: ").lower()
computadora = random.choice(opciones)

print(f"Computadora elige: {computadora}")

if usuario == computadora:
    print("Es un empate")
elif (usuario == "piedra" and computadora == "tijera") or \
     (usuario == "papel" and computadora == "piedra") or \
     (usuario == "tijera" and computadora == "papel"):
    print("¡Ganaste!")
else:
    print("Perdiste")