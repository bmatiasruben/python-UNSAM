# -----------------------------------------------------------------
# Ejercicio 1.18
# -----------------------------------------------------------------

nombreUsuario = input('Ingrese nombre de usuari@: ')
print('Hola,', nombreUsuario)

frase = input('Ingresa la frase a traducir a lenguaje inclusivo: ')

palabras = frase.split()
numPalabra = 0
simbolos = ',.;:/'

for palabra in palabras:
    if palabra[-1] in simbolos:
        if 'o' in palabra[-3:]:
            palabra = palabra[:-3] + palabra[-3:].replace('o', 'e')
    else:
        if 'o' in palabra[-2:]:
            palabra = palabra[:-2] + palabra[-2:].replace('o', 'e')
    palabras[numPalabra] = palabra
    numPalabra += 1

fraseT = ' '.join(palabras)
print(fraseT)
