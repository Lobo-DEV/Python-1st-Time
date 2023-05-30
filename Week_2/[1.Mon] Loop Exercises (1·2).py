''' EXERCISE 1 '''
# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

while True:
    palabra = input('Por favor, escriba una palabra: ')
    if palabra.isalpha():
        veces = 0
        while veces < 10:
            print(palabra)
            veces +=1
        break
    else:
        print('Lo siento. Sólo puede introducir palabras.')



''' EXERCISE 2 '''
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

while True:
    edad = input('Por favor, introduzca su edad en años: ')
    if edad.isnumeric():
        edad = int(edad)
        conteo = 0
        print('Usted ha podido celebrar todos estos cumpleaños:')
        while conteo < edad:
            print('Año: ' +str(conteo + 1))
            conteo +=1
        break
    else:
        print('Lo siento. Sólo puede introducir números.')
        
        

''' EXERCISE 3 '''
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

while True:
    numero = input('Por favor, elija un número entero positivo: ')
    if numero.isnumeric():
        numero = int(numero)+1
        inicio = 1
        list_num = []
        while inicio < numero:
            if inicio % 2 != 0:
                list_num.append(inicio)
                inicio +=1
            else:
                inicio +=1
                continue
        print(*list_num, sep = ', ')
        break
    else:
        print('Lo siento. El dato proporcionado no es válido.')
        
        
        
''' EXERCISE 4 '''
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

while True:
    user_num = input('Por favor, elija un número entero positivo: ')
    if user_num.isnumeric():
        user_num = int(user_num)
        list_n = []
        while user_num > 0:
            list_n.append(user_num)
            user_num -=1
        print(*list_n, sep = ', ')
        break
    else:
        print('Lo siento. El dato proporcionado no es válido.')
        
        

''' EXERCISE 5 '''
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

while True:
    inversion = input('Por favor, especifique una cantidad a invertir: ')
    if inversion.replace('.', '', 1).isdigit():
        inversion = float(inversion)
    else:
        print('Lo siento, la inversión no es válida.')
        continue
    
    interes = input('Por favor, especifique el interés anual: ')
    if interes.isdigit():
        interes = int(interes)
        interes_porcen = float((interes / 100) + 1)
    else:
        print('Lo siento, el interés no es válido.')
        continue
        
    anos = input('Por favor, especifique el número de años de cuota fija: ')
    if anos.isdigit():
        anos = int(anos)
    else:
        print('Lo siento, el número de años no es válido.')
        continue

    total_anos = 1

    print('')
    print('Usted comenzó con una inversión inicial de ' +str(inversion)+ '€')
    print('Con un interes del ' +str(interes)+ '%')
    print('Y una renta fija a ' +str(anos)+ ' años.')
    print('')
    
    while total_anos <= anos:
        total = inversion * (interes_porcen ** total_anos)
        ganancias = total - inversion
        print('Tras ' +str(total_anos)+ ' año/s, usted acumuló un total de: ' +str(round(total, 2))+ '€')
        print('Generando unas ganacias de ' +str(round(ganancias, 2))+ '€')
        total_anos +=1
    break



''' EXERCISE 6 '''
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

# *
# **
# ***
# ****
# *****

while True:
    try:
        print('Voy a imprimir un triángulo con un número de su elección.')
        user_n = int(input('Por favor, introduce un número entero: '))
        break
    except ValueError:
        print('Lo siento, sólo puede introduce números.')
        
first_num = 1
print_ico = "*"
while user_n >= first_num:
    print(print_ico * first_num)
    first_num +=1