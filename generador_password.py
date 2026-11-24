import random
import string

longitud = 16

caracteres = string.ascii_letters + string.digits + "!@#$%&*"

password = "".join(
    random.choice(caracteres)
    for _ in range(longitud)
)

print("Contraseña generada:", password)
