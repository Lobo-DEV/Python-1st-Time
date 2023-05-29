''' EXERCISE 6 '''
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

group_A_name = "Grupo A"
group_B_name = "Grupo B"

letter_before = "M" # Excluded
letter_after = "N" # Excluded

man_sex = "MACHO"
woman_sex = "HEMBRA"

group_A = []
group_B = []


while True:   
    user_nom = input('Por favor, escriba su nombre: ')
    
    if user_nom.isalpha():
        user_nom_cap = user_nom.upper()
        break
    else:
        print('Parece que hubo un error.')
        
    
while True:    
    user_sex = input('Por favor, indique su sexo (Macho/Hembra): ')
    
    if (user_sex.upper() == man_sex) or (user_sex.upper() == woman_sex):
        user_sex_cap = user_sex.upper()
        break
    else:
        print('Parece que hubo un error.')
        
        
if (user_nom_cap[0] < letter_before and user_sex_cap == woman_sex) \
or (user_nom_cap[0] > letter_after and user_sex_cap == man_sex):
    group_A.append(user_nom_cap)
    group_A.sort()
else:
    group_B.append(user_nom_cap)
    group_B.sort()
    

if user_nom_cap in group_A:
    print('Usted pertenece al "' +group_A_name+ '"')
    print('Estos son todos los integrantes del "' +group_A_name+ '"')
    print(group_A)
else:
    print('Usted pertenece al "' +group_B_name+ '"')
    print('Estos son todos los integrantes del "' +group_B_name+ '"')
    print(group_B)
    
    
    
''' EXERCISE 7 '''
# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

# Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10000€ y 20000€	15%
# Entre 20000€ y 35000€	20%
# Entre 35000€ y 60000€	30%
# Más de 60000€	45%

# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

renta1 = range(0, 10000)
renta2 = range(10000, 20000)
renta3 = range(20000, 35000)
renta4 = range(35000, 60000)
# renta5 = range(60000, float('inf'))

impositive1 = 5
impositive2 = 15
impositive3 = 20
impositive4 = 30
impositive5 = 45


while True:
    user_renta = input('Por favor, ingrese su renta anual total, sin decimales: ')
    if user_renta.isdigit():
        user_renta = int(user_renta)
        break
    else:
        print('Parece que hubo un error.')
        

if user_renta in renta1:
    print('A usted le pertenece un tipo impositivo del: ' +str(impositive1)+ '%')
elif user_renta in renta2:
    print('A usted le pertenece un tipo impositivo del: ' +str(impositive2)+ '%')
elif user_renta in renta3:
    print('A usted le pertenece un tipo impositivo del: ' +str(impositive3)+ '%')
elif user_renta in renta4:
    print('A usted le pertenece un tipo impositivo del: ' +str(impositive4)+ '%')
else:
    print('A usted le pertenece un tipo impositivo del: ' +str(impositive5)+ '%')
    
    

''' EXERCISE 8 '''
# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	0.4
# Meritorio	0.6 o más

# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

niveles_rendimiento = {
    0.0 : "INACEPTABLE",
    0.4 : "ACEPTABLE",
    0.6 : "¡MERITORIO!" }

keys_list = list(niveles_rendimiento.keys())
# first_key = keys_list[0]
# second_key = keys_list[1]
# third_key = keys_list[2]

bonificacion = 2400


while True:
    try:
        user_points = float(input('Por favor, ingrese sus puntos obtenidos este año: '))
        if (user_points in keys_list) or \
        ((int(str(user_points)[-1]) % 2 == 0) and (user_points > 0.2)):
           break
        else:
            print('Lo lamento, pero su puntuación total no es válida.')
    except ValueError:
        print('Parece que hubo un error. No olvide añadir los decimales.')


nivel_rendimiento = None
for puntuacion in keys_list:
    if user_points >= puntuacion:
        nivel_rendimiento = niveles_rendimiento[puntuacion]


bonificacion_total = (user_points * bonificacion)


if nivel_rendimiento:
    print('Su rango para este año es: ' +nivel_rendimiento)
    print('Usted recibe una bonificación total de: ' +str(bonificacion_total)+ '€')
else:
    print("No se encontró un nivel de rendimiento válido para la puntuación ingresada.")
    
    
    
''' EXERCISE 9 '''
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

edad_r1 = range(0, 4)
edad_r2 = range(4, 18)
edad_r3 = range(18, 60)
edad_max = 60

entrada_r1 = "¡GRATIS!"
entrada_r2 = 5
entrada_r3 = 10


while True:
    try:
        u_edad = int(input('Por favor, introduzca su edad en años: '))
        if u_edad in edad_r1:
            print('El precio para clientes de ' +str(u_edad)+ ' años es ' +entrada_r1)
            break
        elif u_edad in edad_r2:
            print('El precio para clientes de ' +str(u_edad)+ ' años es ' +str(entrada_r2)+ '€')
            break
        elif u_edad in edad_r3:
            print('El precio para clientes de ' +str(u_edad)+ ' años es ' +str(entrada_r3)+ '€')
            break
        else:
            print('Lo sentimos, pero la edad máxima es de ' +str(edad_max)+ ' años')
            break
    except ValueError:
        print('Parece que hubo un error con la edad proporcionada.')
        
        

''' EXERCISE 10 '''
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

from unidecode import unidecode



nom_pizzeria = "Bella Napoli"

ing_base = ("TOMATE", "MOZZARELLA")
ing_veg = ("PIMIENTO", "TOFU")
ing_no_veg = ("PEPERONI", "JAMÓN", "SALMÓN")


print('Bienvenido a la pizzería ¡' + nom_pizzeria + '!')
print('Todas nuestras pizzas incluyen: ' + ', '.join(map(str, ing_base)))
print('Además de esto, usted puede elegir un ingrediente extra.')
print('Esta es nuestra lista de ingredientes:')


while True:
    try:
        print(', '.join(map(str, ing_veg + ing_no_veg)))

        user_ing = str(input('Por favor, elija uno de ellos: '))
        uni_user_ing = unidecode(user_ing).upper()

        if uni_user_ing in (unidecode(ingrediente).upper() for ingrediente in ing_veg):
            print('Su pizza contiene ' + ', '.join(map(str, ing_base)) + ' y ' + user_ing.upper())
            print('Por lo que su pizza es vegetariana.')
            break
        elif uni_user_ing in (unidecode(ingrediente).upper() for ingrediente in ing_no_veg):
            print('Su pizza contiene ' + ', '.join(map(str, ing_base)) + ' y ' + user_ing.upper())
            print('Por lo que su pizza no es vegetariana.')
            break
        else:
            print('Lo lamento, pero sólo están permitidos los ingredientes mostrados.')
    except ValueError:
        print('Parece que hubo un error.')
