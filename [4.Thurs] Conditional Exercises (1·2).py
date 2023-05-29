'''EXERCISE 1'''
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

while True:
    
    edad = input('Por favor, indique cuántos años tiene: ')
    
    if edad.isdigit():
        edad = int(edad)
        
        if edad < 18:
            print('Usted es menor de edad. No puede pasar.')
            
        elif 18 <= edad <= 40:
            print('Usted es mayor de edad. Puede pasar.')
            
        elif edad > 40:
            print('Lo siento, la edad máxima permitida es de 40 años.')
        
        break
    
    else:
        print('Parece que hubo un error.')
        
        

'''EXERCISE 2'''
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
import time





password = "piZZa123"
tries = 3
user_tries = tries
block_time = 10 # En segundos


while True:
    
    user_password = input('Por favor, introduzca su contraseña. Recuerde que tiene ' +str(user_tries)+ ' intentos: ')
    
    if user_password == password:
        print('Su contraseña es correcta. Inicializando Sistema.')
        break
        
    else:            
        if user_tries <= 1:
            print('Falló su contraseña ' +str(tries)+ ' veces.')
            print('Este dispositivo ha quedado bloqueado durante ' +str(block_time)+ ' segundos.')
            time.sleep(block_time)
            break
        
        else:
            print('Lo lamento, esta contraseña es incorrecta.')
            user_tries = user_tries-1
            continue



''' EXERCISE 3'''
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

while True:
    
    n1 = input('Por favor, introduzca el número que actuará cómo "Dividendo": ')
    
    if n1.replace(".", "", 1).isdigit():
        if "." in n1:
            n1 = float(n1)
            break
        else:
            n1 = int(n1)
            break
    else:
        print('¡Error! Este dato no es válido.')


while True:
    
    n2 = input('Por favor, introduzca el número que actuará cómo "Divisor": ')
    
    if n2.replace(".", "", 1).isdigit():
        if n2 == "0":
            print('¡Error! El "Divisor" no puede ser "0" (cero)')
        else:
            if "." in n2:
                n2 = float(n2)
                break
            else:
                n2 = int(n2)
                break
    else:
        print('¡Error! Este dato no es válido.')


n3 = round((n1 / n2), 2)

if n3.is_integer():
    n3 = int(n3)


print('El resultado de esta operación es: ' +str(n1)+ '/' +str(n2)+ ' = ' +str(n3))



''' EXERCISE 4 '''
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

while True:
    
    user_n = input('Por favor, introduzca un número entero: ')

    if user_n.isdigit():
        user_n = int(user_n)
        break
    else:
        print('El número introducido no es válido.')
        

if (user_n % 2) != 0:
    print('Su número es "Impar".')
else:
    print('Su número es "Par".')
    
    
    
''' EXERCISE 5 '''
# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad_tributar = 16
bonificacion_tributar = 1000

print('Si usted tiene ' +str(edad_tributar)+ ' o más, y cobra +' +str(bonificacion_tributar)+ '€ al mes, SÍ deberá tributar.')

while True:
    
    user_edad = input('Por favor, introduzca cuántos años tiene: ')
    
    if user_edad.isdigit:
        user_edad = int(user_edad)
        break
    else:
        print('El número introducido no es válido.')
        

while True:
    
    user_bonificacion = input('Por favor, introduza su bonificacion en €uros: ')
    
    if user_bonificacion.replace(".", "", 1).isdigit():
        user_bonificacion = float(user_bonificacion)
        break
    else:
        print('El número introducido no es válido.')
        

if user_edad >= edad_tributar and user_bonificacion >= bonificacion_tributar:
    print('Usted tiene ' +str(edad_tributar)+ ' o más, y cobra +' +str(bonificacion_tributar)+ '€ al mes.')
    print('Por lo tanto, usted SÍ debe tributar.')
elif user_edad < edad_tributar and user_bonificacion >= bonificacion_tributar:
    print('Aunque usted cobra +' +str(bonificacion_tributar)+ '€ al mes, no es mayor de ' +str(edad_tributar)+ ' años.')
    print('Por lo tanto, ustedes NO debe tributar.')
elif user_edad >= edad_tributar and user_bonificacion < bonificacion_tributar:
    print('Aunque usted tiene ' +str(edad_tributar)+ ' o más, no cobra +' +str(bonificacion_tributar)+ '€ al mes.')
    print('Por lo tanto, ustedes NO debe tributar.')
else:
    print('Usted no llega a los mínimos establecidos para tributar.')
    print('Por lo tanto, ustedes NO debe tributar.')