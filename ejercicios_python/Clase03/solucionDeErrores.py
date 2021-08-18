#%%
# -----------------------------------------------------------------
# Ejercicio 3.1
# -----------------------------------------------------------------

# Error: El error es de tipo semántico, el while termina en i = 0, porque return hace que salga de la función. Es decir, solo ve si el string tiene una 'a' en la primera posición
# Solución: Para solucionar esto, el i += 1 debería estar dentro del else, y el return debería estar luego del while, es decir, despues de que revise todo el string sin encontrar 'a'

# Error: Además, el programa no reconoce mayusculas, minusculas, acentos, etc, por lo que 'UNSAM 2020' daría False aún arreglando lo anterior
# Solución: Para solucionar esto, en el primer if deberían tener en cuenta estos casos. Creo un string que contenga todos estos caracteres, y reviso si expresión[i] está en ese string

from typing import Type


def tiene_a(expresion):
    tiposA = 'aáäAÁÄ'
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] in tiposA:
            return True
        else:
            i += 1
    return False
            
print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))

#%%

# -----------------------------------------------------------------
# Ejercicio 3.2
# -----------------------------------------------------------------

# Error: Tiene error de sintaxis al no poner dos puntos luego de la función, while e if
# Solución: Agregar los dos puntos a todos esos lugares

# Error: Tiene un error de sintaxis, 'Falso' no es un valor válido de boolean
# Solución: Reemplazar Falso por False

# Error: Idem 3.1. El programa no reconoce mayusculas, minusculas, acentos, etc, por lo que 'UNSAM 2020' daría False aún arreglando lo anterior
# Solución: Para solucionar esto, en el primer if deberían tener en cuenta estos casos. Creo un string que contenga todos estos caracteres, y reviso si expresión[i] está en ese string

def tiene_a(expresion):
    tiposA = 'aáäAÁÄ'
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] in tiposA:
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))

# %%

# -----------------------------------------------------------------
# Ejercicio 3.3
# -----------------------------------------------------------------

# Error: hay un error de tiempo de ejecución porque 1984 está como entero y no como string. No se le puede ver len() a un entero.
# Solución: Agregar un try-except con TypeError

def tiene_uno(expresion):
    try:
        n = len(expresion)
        i = 0
        tiene = False
        while (i<n) and not tiene:
            if expresion[i] == '1':
                tiene = True
            i += 1
        return tiene
    except TypeError:
        print('Error: No se ingresó un string') 

print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))

# %%

# -----------------------------------------------------------------
# Ejercicio 3.4
# -----------------------------------------------------------------

# Error: La suma no da lo que debería porque a la función no se le da ninguna instrucción de return
# Solución: Agregar 'return c' al final de la función

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

# %%

# -----------------------------------------------------------------
# Ejercicio 3.5
# -----------------------------------------------------------------

# Error: Cada vez que se define la variable registro, se modifican todas las asignaciones anteriores.
# Solución: Reiniciar la variable inmediatamente despues del for.

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

# %%
