# -----------------------------------------------------------------
# Ejercicio 7.10
# -----------------------------------------------------------------

def valor_absoluto(n):
    '''
    Pre: N un numero real
    Pos: Devuelve el valor absoluto de N
    '''
    if n >= 0:
        return n
    else:
        return -n
    # No hay invariantes

def suma_pares(l):
    '''
    Pre: l una lista de numeros reales
    Pos: Devuelve la suma de los pares en l
    '''
    res = 0
    for e in l:
        if e % 2 == 0:
            res += e # Suma elementos en caso que sean divisibles por 2
        else:
            res += 0
    return res
    # Invariantes:
    # res

def veces(a, b):
    '''
    Pre: a y b dos numeros reales
    Pos: Devuelve el producto a*b
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
    # Invariantes:
    # res
    # nb

def collatz(n):
    '''
    Pre: n numero entero
    Pos: Devuelve la cantidad de veces que se sigue la sucesion de Collatz hasta llegar a 1
    '''    
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res
    # Invariantes:
    # res