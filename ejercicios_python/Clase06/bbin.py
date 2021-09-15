# -----------------------------------------------------------------
# Ejercicio 6.15
# -----------------------------------------------------------------

def busqueda_lineal_lordenada(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z > e:   # si encontramos a e
            pos = i - 1 # guardamos su posición
    return pos

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

def donde_insertar(lista, x):
    pos = -1
    izq = 0
    der = len(lista) - 1
    while pos == -1 and izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if pos == -1:
        if lista[medio] > x:
            pos = medio
        else:
            pos = medio + 1 
    return pos


def insertar(lista, x):
    posicion = busqueda_binaria(lista, x, verbose = False)
    a_ubicar = donde_insertar(lista, x)
    if posicion == -1:
        lista.insert(a_ubicar, x)
        return a_ubicar
    else:
        return posicion

