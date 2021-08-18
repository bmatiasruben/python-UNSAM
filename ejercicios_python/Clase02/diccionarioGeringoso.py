# -----------------------------------------------------------------
# Ejercicio 2.14
# -----------------------------------------------------------------

def traduccionGeringoso(palabrasLista): # Defino mi funcion traduccion, tiene una lista de palabras como entrada y un diccionario como salida
    listaTraducida = {} # Inicializo el diccionario vacío
    vocales = 'aeiou'
    vocalesAcento = 'áéíóú'
    for palabra in palabrasLista:
        posicion = 0
        palabraTraducida = '' # Reseteo las variables posicion y palabraTraducida a 0 y vacío para que no se me junten las iteraciones
        for c in palabra: # Código anterior para traducir una palabra a geringoso
            if c in vocales or c in vocales.upper():
                if c == 'u' and (palabra[posicion + 1] == 'i' or palabra[posicion + 1] == 'e'):
                    palabraTraducida += c
                else:
                    palabraTraducida += c + 'p' + c.lower()
            elif c in vocalesAcento or c in vocalesAcento.upper():
                for i in range(5):
                    if c == vocalesAcento[i]:
                        palabraTraducida += c + 'p' + vocales[i]
            else:
                palabraTraducida += c
            posicion += 1

        listaTraducida[palabra] = palabraTraducida # A la clave palabra del diccionario le asigno la variable palabraTraducida

    return listaTraducida # Devuelvo el diccionario completo

palabrasLista = ['banana', 'manzana', 'mandarina'] # Lista de prueba

print(traduccionGeringoso(palabrasLista))
