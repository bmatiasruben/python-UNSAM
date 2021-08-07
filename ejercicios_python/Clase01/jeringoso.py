# -----------------------------------------------------------------
# Ejercicio 1.18
# -----------------------------------------------------------------

cadena = input('Ingrese la frase a traducir a jeringoso: ') # Defino la cadena de entrada como input
capadepenapa = '' # Defino la cadena de salida
vocales = 'aeiou'
vocalesAcento = 'áéíóú'
posicion = 0
uMuda = False

for c in cadena:
    if c in vocales or c in vocales.upper():
        if c == 'u' and (cadena[posicion + 1] == 'i' or cadena[posicion + 1] == 'e'):
            capadepenapa += c
        else:
            capadepenapa += c + 'p' + c.lower()
    elif c in vocalesAcento or c in vocalesAcento.upper():
        for i in range(5):
            if c == vocalesAcento[i]:
                capadepenapa += c + 'p' + vocales[i]
    else:
        capadepenapa += c
    posicion += 1

print(capadepenapa)
