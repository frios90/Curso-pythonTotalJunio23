from random import randint

intento = 1
numero_aleatorio =  randint(1,100)
print(numero_aleatorio)

print("Hola jugador")
nombre_jugador = input("ingresa tu nombre : ")
print(f"{nombre_jugador} tienes 8 intentos para adivinar el número")

while intento < 9:
    num = int(input(f"Intento n({intento}) : "))
    if num < 1 or num > 100:
        print(f"{num} no es un número valido. Debe ingresa un número entre 1 y 100")
    elif num < numero_aleatorio:
        print("(x)El número que ingresaste es MENOR que el número a adivinar")
    elif num > numero_aleatorio:
        print("(x)El número que ingresaste es MAYOR que el número a adivinar")
    else:
        print(f"(/){nombre_jugador} HAS GANADO!!. El número incognito es {numero_aleatorio}")
        break
    if intento >= 8:
        print("Ya no te quedan mas intentos :( . Has perdido")
        break
    intento += 1
else:
    print("has salido del juego. gracias por participar")
