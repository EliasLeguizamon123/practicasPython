#Video juego - Batalla final contra Bulork 'El terrible'
#En este video juego debes pelear y derrotar a Bulork utilizando tus poderes mentales y adivinar en que numero esta pensando
#Pero cuidado! los intentos son limitados.
#Buena suerte.
import random

Intentos = 0

print('Quien se atreve a enfrentar a Bolurk?')

nombreJugador = input()

print('Con que te llamas ' + nombreJugador + '?')

numero = random.randint(1, 20)

print('De acuerdo como me gusta tu nombre, te dejare vivir si adivinas el numero que estoy pensando, de acuerdo ' + nombreJugador + '?')

respuesta = input()

if respuesta == 'si':
    while Intentos <= 6:
        print('Muestrame tus poderes mentales.')
        estimacion = input()
        estimacion = int(estimacion)

        Intentos = Intentos + 1

        if estimacion < numero:
            print('El numero es muy pequeño, intenta de nuevo')

        if estimacion > numero:
            print('El numero es muy grande, intenta de nuevo')

        if estimacion == numero:
            print('¡MALDITO!, lograste vencerme solo por ahora')
            break

        if estimacion == numero:
            Intentos = str(Intentos)
            print( + nombreJugador + ', lograste vencerme solo en ' + Intentos + ' intentos!')

    if estimacion != numero:
        numero = str(numero)
        print('Preparate para sufrir mi ira, el numero en el cual pensaba era: ' + numero)
elif respuesta == 'no':
    print('¡Cobarde!')


if respuesta != 'si' or respuesta != 'no':
    print('Eso no es lo que pregunte basura')
