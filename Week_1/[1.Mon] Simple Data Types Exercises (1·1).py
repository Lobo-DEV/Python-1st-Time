''' EXERCISE 1'''
# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

print ('¡Starting Python!')



''' EXERCISE 2'''
# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

f = '¡Hola Mundo!'
print(f)



''' EXERCISE 3'''
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

us = str(input('Por favor, escriba su nombre: '))
print('¡Hola ' +us+ '!')



''' EXERCISE 4'''
# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética ((3+2) / (2*5))².
ma = (((3 + 2) / (2 * 5)) ** 2)
print(ma)



''' EXERCISE 5'''
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

ht = float(input('Por favor, diga cuántas horas trabajó hoy: '))
ph = float(input('Por favor, diga cuánto cobra por hora : '))
tt = ht * ph
print('Su cobro de hoy es de ' +str(tt)+ '.')



''' EXERCISE 6'''
# Escribir un programa que lea un entero positivo, <N>, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta <N>. La suma de los <N> primeros enteros positivos puede ser calculada de la siguiente forma: suma = (n(n+1)) / 2

n = int(input('Por favor, elija un número: '))

nt = 0
for i in range(1, n+1):
    nt += i
    i += 1

print ('La suma de los números, desde 1 hasta ' +str(n)+ ', es de: ' +str(nt)+ '.')



''' EXERCISE 7'''
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

m = float(input('Por favor, especifique su altura en metros: '))
kg = float(input('Por favor, especifique su peso en Kgs: '))
imc = round((kg / (m ** 2)), 2)

print('Tu índice de masa corporal (IMC) es: ' +str(imc)+ '.')



''' EXERCISE 8'''
# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

while True:
    n = input('Por favor, elija un primer número entero: ')
    if n.isdigit():
        n = int(n)
        break 
    else:
        print('¡Error! Sólo puede introducir números enteros.')

while True:
    m = input('Por favor, elija un segundo número entero: ')
    if m.isdigit():
        m = int(m)
        break 
    else:
        print('¡Error! Sólo puede introducir números enteros.')

c = n // m
r = n % m

print('El "Cociente" de esta división es: ' +str(c))
print('El "Resto" de esta división es: ' +str(r))



''' EXERCISE 9'''
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

while True:
    inv = input('Por favor, especifique, en €uros, de cuánto sería la inversión: ')
    if inv.isnumeric():
        inv = float(inv)
        break
    else:
        print('¡Error! Sólo puede introducir números.')

while True:
    nAnos = input('Por favor, indice a cuántos años sería la inversión: ')
    if nAnos.isdigit():
        nAnos = int(nAnos)
        break
    else:
        print('¡Error! Sólo puede introducir números.')
        
while True:
    intA = input('Por favor, especifique, en porcentaje, de cuánto sería el interés anual: ')
    if intA.isnumeric():
        intA = float(intA)
        break
    else:
        print('¡Error! Sólo puede introducir números.')

creTT = inv * nAnos * (intA / 100)
creInt = creTT - inv
print('Con una inversión anual de ' +str(inv)+ '€')
print('Tras ' +str(nAnos)+ ' años, obtendría un capital total de ' +str(creTT)+ '€')
print('Esto le habría generado ' +str(creInt)+ '€ de interés en ' +str(nAnos)+ ' años.')



''' EXERCISE 10'''
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

clown = 112
doll = 75

while True:
    clownTT = input('Por favor, especifique cuántos "Payasos" se vendienron en el último pedido: ')
    if clownTT.isdigit():
        clownTT = int(clownTT)
        break
    else:
        print('¡Error! Sólo puedes introducir números enteros.')

while True:
    dollTT = input('Por favor, especifique cuántas "Muñecas" se vendienron en el último pedido: ')
    if dollTT.isdigit():
        dollTT = int(dollTT)
        break
    else:
        print('¡Error! Sólo puedes introducir números enteros.')


clownWTT = clownTT * clown
dollWTT = dollTT * doll
weightTT = (clownWTT + dollWTT) / 1000

print('El peso total del pedido es de: ' +str(round(weightTT, 3))+ 'kg')



''' EXERCISE 11'''
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

intAnual = 4 / 100

while True:
    depo = input('Por favor, introduce, en €uros, la cantidad fija depositada en el banco: ')
    if depo.isnumeric():
        depo = float(depo)
        break
    else:
        print('¡Error! Sólo se admiten números, incluyendo decimales.')
        
while True:
    numAnos = input('Por favor, introduce a cuántos años es el deposito fijo.')
    if numAnos.isdigit():
        numAnos = int(numAnos)
        break
    else:
        print('¡Error! Sólo se admiten números enteros.')


for i in range(1, numAnos+1):
    
    capTT = depo * (1 + intAnual) ** i
    intGen = capTT - depo
    
    print('Tras ' +str(i)+ ' año/s, el capital total será de: ' +str(round(capTT, 2))+ '€')
    
    print('En este tiempo usted habría generado ' +str(round(intGen, 2))+ '€ de interés.')
    
    
    
''' EXERCISE 12'''
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

pan = 3.49
des = 60
offPan = pan * (des / 100)

while True:
    offPanV = input('Por favor, indique el número de barras de pan vendidas hoy, que no sean pan fresco: ')
    if offPanV.isdigit():
        offPanV = int(offPanV)
        break
    else:
        print('¡Error! Sólo se admiten núemros enteros')
        
gTToffPan = offPan * offPanV
pTToffPan = (pan - offPan) * offPanV
        
print('El precio del plan fresco es de: ' +str(pan)+ '€')
print('El precio del pan, que no es fresco, es de: ' +str(round(offPan, 2))+ '€, con un descuento del ' +str(round(des, 2))+ '%')
print('La ganancia total en pan, que no es fresco, es de: ' +str(round(gTToffPan, 2))+ '€')
print('La pérdida en venta en pan, que no es fresco, es de: ' +str(round(pTToffPan, 2))+ '€')
