'''
En este programa escribiremos una lógica donde generaremos un número y el usuario tiene que adivinarlos, hasta 
que no lo adivine no se acaba el programa.
'''

#importamos la lbrería random
import random

# declaramos las variables globales que usaremos en nuestro programa
number_generated= 0
number_asked = 0



# definimos la función que va a generar el número, con el método randint devolveremos un número aleatorio entre 0 y 10
def genarte_number():
    global number_generated
    number_generated = random.randint(0, 10)
    print('***********************************************************************\n')
    print('######## START THE GAME #########\n')
    #global number_generated
    #global number_asked
    number_asked = int(input('Por favor ingresa un número para adivinar entre 0 y 10: \n>>> '))
    
    # con el bucle while realizaremos la petición del número mientras sea diferente al que genere el sistema
    while number_asked < number_generated:
        print('aún no adivinas\n')
        number_asked = int(input('Ingresa otro número\n>>> '))
        if number_asked == number_generated:
            print(f'Adivinaste el número, el número es: {number_generated}')
        elif number_asked > number_generated:
            print('El número ingresado es mayor que el número generado...')
        else:
            print('No te rindas, ya casi lo logras!')
    
genarte_number()