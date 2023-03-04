
n = int(input("Digite un numero entero: "))

if n > 999:
    if n <= 9999:
        rta = "El número ingresado, si es un número entero positivo de 4 digitos"
    else:
        rta = "El número ingresado, no es un número entero positivo de 4 digitos sino de más de 4 digitos"
else:
    if n >= 0:
        rta = "El número ingresado, no es un número positivo de 4 digitos sino de menos de 4 digitos"
    else:
        rta = "El número ingresado, es un numero negativo"

print(rta)