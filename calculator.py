'''
aquí vamos a programar una calculadora sencilla, que realice operaciones sencillas
y principales como sumar, restar, multiplicar y dividir con valores
que se soliciten al usuario y que el usuario ingrese, le mostrará el resultado de la operación que escoja
dependiendo de la cantidad de valores que quiera operar entre sí, solo se puede operar por ahora con una operación cada
vez que se ejecute el programa...
'''
from functools import reduce

# definiremos las variables a utilizar en cada función que serán globales
save_num = 0
values_to_op = []

#pedimos al usuario la cantidad de números con los que operará
save_num = int(input('Ingrese la cantidad de números con los que quiera operar: \n>>> '))
acumulator = 0
   
#utilizamos un while para hacer la petición de los valores a operar 
while save_num > acumulator:
    if save_num == 0:
      print('Por favor ingrese un número mayor que cero para poder continuar con el programa...')
    elif save_num > 0:
      print(f'Vas a operar {save_num} veces')
      dato = int(input('Por favor ingrese un número: \n>>> '))
      values_to_op.append(int(dato))
      acumulator += 1
      
# le mostramos el menú al usuario por pantalla para que él escoja que tipo de operación desea realizar 

def show_menu():
    global option_choice 
    option_choice = int(input('Sus opciones para operar son: \n'
                              +'1 Multiplicar\n'
                              +'2 Dividir\n'
                              +'3 Sumar\n'
                              +'4 Restar\n'
                              + '5 Finalizar\n>>> Escriba el número correspondiente a la operación que desea realizar: '))
   
    try:   
        if option_choice == 1:
             print('Usted ha seleccionado multiplicar sus valores\n')
             print(f'el resultado es: {multiply(values_to_op)}')
        elif option_choice == 2:
            print('Usted ha seleccionado dividir sus valores\n')
            print(f'El resultado es: {division}')
        elif option_choice == 3:
            print('Usted ha seleccionado sumar sus valores\n')
            print(f'El resultado es: {adition}')
        elif option_choice == 4:
            print('Usted ha seleccionado restar sus valores\n')
            print(f'El resultado es: {substract}')
        elif option_choice == 5:
            print('Gracias por participar hasta pronto....')
        else:
            print('Por favor escoja un número de la lista.')
    except NameError(ValueError):
        print('Ups... no escribió un número...')


# creamos la funcion para la multiplicación

def multiply(dato):
   global multiplo 
   multiplo = 1
   for i in values_to_op:
       multiplo = multiplo * i
   return multiplo


#esta será la función para la división 
division = reduce(lambda x, y: x / y, values_to_op)


#esta será la función de sumar
adition = reduce(lambda x, y: x + y, values_to_op)


# esta será la función para restar
substract = reduce(lambda x, y: x - y, values_to_op)


show_menu()

    
 





    
    





