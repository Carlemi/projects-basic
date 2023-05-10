'''
aquí vamos a programar una calculadora sencilla, que realice operaciones sencillas
y principales como sumar, restar, multiplicar y dividir con valores
que se soliciten al usuario y que el usuario ingrese
'''

# definiremos las variables a utilizar en cada función que serán globales
save_num = 0
values_to_op = []
dato = 0
#result = 1
#creamos la función por la cual le pediremos al usuario los valores con los que realizaremos las operaciones

def ask_num():
   #pedimos al usuario la cantidad de números con los que operará
   global save_num  
   save_num = int(input('Ingrese la cantidad de números con los que quiera operar: \n>>> '))
   acumulator = 0
   global values_to_op
   global dato
   #utilizamos un while para hacer la petición de los valores a operar 
   
   while save_num > acumulator:
      if save_num <= 0:
        print('Por favor ingrese un número mayor que cero para poder continuar con el programa...')
      elif save_num > 0:
        print(f'Vas a operar {save_num} veces')
        dato = float(input('Por favor ingrese un número: '))
        values_to_op.append(float(dato))
      acumulator += 1
      #acumulator = save_num
   #print(values_to_op)
      

   
        
      
      
#ask_num()
      
    


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
      if option_choice == 1 and option_choice :
         print('Usted ha seleccionado multiplicar sus valores\n')
         print('y el resultado es\n>>>')
      elif option_choice == 2:
         print('Usted ha seleccionado dividir sus valores\n')
         print('y el resultado es\n>>>')
      elif option_choice == 3:
         print('Usted ha seleccionado sumar sus valores\n')
         print('y el resultado es\n>>>')
      elif option_choice == 4:
         print('Usted ha seleccionado restar sus valores\n')
         print('y el resultado es\n>>>')
      elif option_choice == 5:
         print('Gracias por participar hasta pronto....')
      else:
         print('Por favor escoja un número de la lista.')
    except NameError(ValueError):
       print('Ups... no escribió un número...')
#show_menu()

# creamos la funcion para la multiplicación

def multiplicate():
   global values_to_op
   global dato
   #global result 
   dato = 1
   
   for multiplicar in range(len(values_to_op)):
      #result = result * values_to_op[multiplicar]
      dato =  dato * values_to_op[multiplicar]
      print(dato)
      
#haremos una función que imprima todo mientras que el usuario haga todo de manera correcta como lo pide el programa

def print_all():
    print(f'{ask_num()} {show_menu()} {multiplicate()}')


print_all()

    
    





