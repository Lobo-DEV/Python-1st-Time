''' EXERCISE 7 '''
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for i in range(1, 11):
    ti = 1 * i
    print(ti)
    


''' EXERCISE 8 '''
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

while True:

    try:
        user_num = int(input('Por favor, intruduzca un número entero: '))
        break
    except ValueError:
        print('Parace que hubo un error con el dato proporcionado.')


num_list = []
i = 0


while i < 5:
    num_list.append(user_num)
    print(*num_list[::-1], sep = ' ')
    user_num +=2
    i +=1
    
    

''' EXERCISE 9 '''
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

while True:
    
    password = "contra-seña"
    user_pass = input('Por favor, introduza su contraseña: ')
    
    if user_pass == password:
        print('Su contraseña ha sido verificada.')
        break
    else:
        print('Lo siento, pero su contraseña no es correcta.')
        continue
    
    
    
''' EXERCISE 10 '''
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

import math





def es_primo(numero):
    if numero <= 1:
        return False
    
    for i in range(2, int(math.sqrt(numero)) +1):
        if numero % i == 0:
            return False
    
    return True


while True:
    
    print('Comprobaremos si su número es un "Número Primo".')
    try:
        user_n = int(input('Por favor, introduzca un número entero: '))
        break
    except ValueError:
        print('Parece que hubo un error con el dato proporcionado.')

  
if es_primo(user_n):
    print('Su número es primo.')
else:
    print('Su número no es primo.')
    
    
    
''' EXERCISE 11 '''
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

while True:
    
    user_word = input('Por favor, introduzca una palabra: ')
    if user_word.isalpha():
        word_list = list(user_word)
        break
    else:
        print('Parece que hubo un error con el dato proporcionado.')
        

# print(*word_list[::-1], sep = ' ')
for word_letter in (word_list[::-1]):
    print(word_letter)



''' EXERCISE 12 '''
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

while True:
    
    user_frase = input('Por favor, introduzca una frase: ')
    if all(c_frase.isalpha() or c_frase.isspace() for c_frase in user_frase):
        break
    else:
        print('Parece que hubo un error con el dato proporcionado.')


while True:
    
    user_letra = input('Por favor, introduzca una letra: ')
    if user_letra.isalpha():
        if len(user_letra) == 1:
            break
        else:
            print('Lo lamento, pero debe introducir una única letra.')
    else:
        print('Parece que hubo un error con el dato proporcionado.')


conteo = 0
for i in user_frase:
    if i == user_letra:
        conteo +=1


print('Su palabra contiene ' +str(conteo)+ ' veces la letra seleccionada.')



''' EXERCISE 13 '''
# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

while True:
    
    print('Repetiré todo lo que usted escriba.')
    print('Cuando desee finalizar, escriba "Salir".')
    u_frase = input('¿Qué desea que repita? ')
    
    if u_frase.upper() == "SALIR":
        print('El programa ha finalizado correctamente.')
        break
    else:
        print(u_frase)
        continue