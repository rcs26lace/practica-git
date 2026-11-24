import random
import time

print("🎲 Simulador de dados")

while True:
    input("Pulsa ENTER para tirar los dados...")

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    print("Lanzando...")
    time.sleep(1)

    print("Dado 1:", dado1)
    print("Dado 2:", dado2)
    print("Total:", dado1 + dado2)

    if input("¿Volver a jugar? (s/n): ").lower() != "s":
        print("¡Hasta pronto!")
        break
