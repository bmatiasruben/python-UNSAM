# -----------------------------------------------------------------
# Ejercicio 4.5
# -----------------------------------------------------------------

def invertir_lista(lista):
    lista_invertida = []
    for numero in lista:
        lista_invertida = [numero] + lista_invertida
    return lista_invertida