''' EXERCISE 1'''
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
import re

while True:
    nombre = input('Por favor, introduce tu nombre: ')
    if re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", nombre):
        nombre = str(nombre)
        break
    else:
        print('¡Error! Sólo se admiten caracteres alfabéticos.')

while True:
    veces = input('Por favor, introduce el número de veces que desea que su nombre se repita.')
    if veces.isdigit():
        veces = int(veces)
        break
    else:
        print('¡Error! Sólo se admiten números enteros.')

for i in range(1, veces+1):
    print(nombre)
    
    
    
''' EXERCISE 2'''
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

while True:
    nomCom = input('Por favor, introduzca su nombre completo. Utilice mayúsculas y munúsculas como desee, no es necesario que sigan ninguna lógica: ')
    if re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", nomCom):
        nomCom = str(nomCom)
        break
    else:
        print('¡Error! Sólo se admiten caracteres alfabéticos.')
        
mayus = ''.join(letra for letra in nomCom if letra.isupper())
minus = ''.join(letra for letra in nomCom if letra.islower())
first = ''.join(palabra[0] for palabra in nomCom.split() if palabra).upper()

print('Estas son todas las letras mayúsculas de tu frase: ' +str(mayus))
print('Estas son todas las letras minúsculas de tu frase: ' +str(minus))
print('Estas son todas las letras iniciales de tu frase, en mayúsculas: ' +str(first))



''' EXERCISE 3'''
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

while True:
    nombreC = input('Por favor, introduce tu nombre completo: ')
    if re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", nombreC):
        nombreC = str(nombreC)
        break
    else:
        print('¡Error! Sólo se admiten caracteres alfabéticos.')
        
letrasNombreC = len(nombreC)
letrasNombreCNoEsp = len(nombreC.replace(' ', ''))
capNombreC = nombreC.upper()
print('El nombre: ' +str(capNombreC)+ ' contiene:')
print(str(letrasNombreC)+ ' caracteres, contando los espacios en blanco.')
print(str(letrasNombreCNoEsp)+ ' caracteres, sin contar los espacios en blanco.')
print(nombreC)



''' EXERCISE 4'''
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

numTLF = True

while numTLF == True:
    
    while True:
        pre = input('Por favor, introduzca el prefijo de su País: +')
        if pre.isdigit():
            break
        else:
            print('¡Error! Lo sentimos, el prefijo introducido no es válido.')

    while True:
        tlf = input('Por favor, introduzca su número de teléfono: ')
        if tlf.isdigit():
            break
        else:
            print('¡Error! Lo sentimos, el número introducido no es válido.')

    while True:
        ext = input('Por favor, introduzca su número de extensión: ')
        if ext.isdigit():
            break
        else:
            print('¡Error! Lo sentimos, la extensión introducida no es válido.')

    ntlf = '+' +pre+ '-' +tlf+ '-' +ext
    
    while True:
        checktlf = input('El número completo introducido es ' +str(ntlf)+ ', ¿es correcto? Responda S/N.')

        if checktlf.upper() == "S":
            print('Número completo: ' +str(ntlf)+ ', confirmado.')
            numTLF = False
            break
        elif checktlf.upper() == "N":
            print('Parece que hubo algún error. Comencemos de nuevo.')
            break
        else:
            print('Lo siento, no le he entendido.')
            continue
        


''' EXERCISE 5'''
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

f1 = input('Por favor, introduzca una frase: ')
f1Inv = f1[::-1]
print('Si invertimos su frase, el resultado es:')
print(f1Inv)



''' EXERCISE 6'''
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

f2 = input('Por favor, escriba una frase en minúsculas: ')

while True:
    vocal = input('Elija una vocal de su frase. Todas las vocales que coincidan se convertirán en mayúsculas.')
    if vocal.lower() in ["a", "e", "i", "o", "u"]:
        break
    else:
        print('Lo siento, pero sólo puede elegir una vocal.')

f2Mod = f2.replace(vocal.lower(), vocal.upper())
print('La frase resultante sería: ' +f2Mod)