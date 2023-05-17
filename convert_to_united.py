'''
Escribiremos un programa que convierta unidades de medida, tiempo o divisas
'''
# Comenzaremos con convertir unidades de medida, por metros a centímetros

#declararemos las variables que usaremos en nuestro programa

metro = 100
convert_to = float(input('Por favor ingrese cuantos metros quiere convertir a centímetros:\n>>> '))

def convert_to_centimetres(metro):
    global convert_to
    global result
    result = metro * convert_to / 1
    return result

print(convert_to_centimetres(metro))

gramos = 1000 

kilo_to_grams = float(input('Por favor ingrese cuantos kilos quiere convertir a gramos:\n>>> '))

def convert_to_gram(gramos):
    global kilo_to_grams
    global resultado

    resultado = gramos * kilo_to_grams / 1
    return gramos


print(convert_to_gram(gramos))