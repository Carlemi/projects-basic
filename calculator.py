'''
aquí vamos a programar una calculadora sencilla, que realice operaciones sencillas
y principales como sumar, restar, multiplicar y dividir con valores
que se soliciten al usuario y que el usuario ingrese
'''
#creamos la función por la cual le pediremos al usuario los valores con los que realizaremos las operaciones

def ask_num():
    number_one = float(input('Por favor ingrese un número: \n>>> '))
    number_two = float(input('Por favor ahora ingrese otro número: \n>>> '))
    