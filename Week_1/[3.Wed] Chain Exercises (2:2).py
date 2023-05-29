''' EXERCISE 7'''
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

while True:
    email = input('Por favor, escriba su email: ')
    if "@" in email and "." in email:
        break
    else:
        print('Parece que hubo un error. Por favor, ingrese un email válido.')

emailFind = email.find("@")
emailEmp = email[:emailFind]
print('A partir de hoy, su correo de empresa es: ' +emailEmp+ '@ceu.es')



''' EXERCISE 8'''
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

while True:
    precio = input('Por favor, introduce un precio en €uros, incluyendo los céntimos: ')
    if "," in precio:
        precio = precio.replace(",", ".")
        break
    elif "'" in precio:
        precio = precio.replace("'", ".")
        break
    elif "." in precio:
        break
    else:
        print('Lo siento, sólo puede añadir un precio válido con 2 decimales.')

precio = round(float(precio), 2)
euros, centimos = str(precio).split(".")

print('El número introducido contiene ' +euros+ '€, y ' +centimos+ ' céntimos.')



''' EXERCISE 9'''
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
from datetime import datetime



while True:
    input_fecha = input('Por favor, introduzca su fecha de nacimiento siguiendo el formato dd/mm/aaaa: ')
    
    try:
        fecha_try = datetime.strptime(input_fecha, "%d/%m/%Y")
        break
    except ValueError:
        print('Lo siento, la fecha introducida no cumple con el formato.')


print('Su fecha de nacimiento es:')
print('Día ' +str(fecha_try.day))
print('Mes ' +str(fecha_try.month))
print('Año ' +str(fecha_try.year))



''' EXERCISE 10'''
# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

lista_compra = input('Por favor, indique todos los artículos de su "Cesta de la Compra", separados por comas: ')

items = lista_compra.split(",")
items = [space.strip() for space in items]

print('Su lista de la compra contiene: ')
for i in items:
    print(i)
    
    
    
''' EXERCISE 11'''
# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

while True:
    
    nombre_pro = input('Por favor, indique el nombre del producto adquirido: ')
    if nombre_pro.isalpha():
        break
    else:
        print('Por favor, introduzta un nombre de producto válido.')
    
    
while True:
    
    unidades_pro = input('Por favor, indique las unidades totales adquiridas de dicho producto: ')
    if unidades_pro.isnumeric():
        unidades_pro = float(unidades_pro)
        break
    else:
        print('Por favor, introduzta un cantidad de unidades válida.')


while True:
        
    precio_pro = input('Por favor, indique el coste total del producto adquirido: ')
    if precio_pro.isnumeric():
        precio_pro = float(precio_pro)
        break
    else:
        print('Por favor, introduzca un precio total válido.')


precio_uni = precio_pro / unidades_pro

print('Usted adquirió el producto: ' +nombre_pro)
print('Por un total de {:03.0f} unidades.'.format(unidades_pro))
print('Un coste unitario de {:09.2f}€'.format(precio_uni))
print('Y un coste total de {:011.2f}€'.format(precio_pro))
