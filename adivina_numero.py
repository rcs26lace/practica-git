import random

numero = random.randint(1, 100)
intentos = 0

print("¡Adivina el número del 1 al 100!")

while True:
    respuesta = int(input("Introduce un número: "))
    intentos += 1

    if respuesta < numero:
        print("Demasiado pequeño.")
    elif respuesta > numero:
        print("Demasiado grande.")
    else:
        print(f"¡Correcto! Lo has conseguido en {intentos} intentos.")
        break
