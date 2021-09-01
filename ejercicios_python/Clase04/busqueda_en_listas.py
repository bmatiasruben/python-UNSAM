# -----------------------------------------------------------------
# Ejercicio 4.4
# -----------------------------------------------------------------

def buscar_u_elemento(lista, valor):
    pos = -1
    for index, numero in enumerate(lista):
        if numero == valor:
            pos = index
    return pos    
    
def buscar_n_elemento(lista, valor):
    apariciones = 0
    for numero in lista:
        if numero == valor:
            apariciones += 1
    return apariciones    

def maximo(lista):
    max = 0
    for numero in lista:
        if isinstance(numero, int) and numero > 0:
            if numero > max:
                max = numero
        else:
            print(f'La lista debe contener solo números enteros positivos. {numero} no cumple alguna de las condiciones')
    return max
