# -----------------------------------------------------------------
# Ejercicio 3.23
# -----------------------------------------------------------------

from collections import Counter
import csv

def leerParque(archivo, parque):
    f = open(archivo, 'rt', encoding="utf8")
    rows = csv.reader(f)
    headers = next(rows)
    arbolesEnParque = []
    for index, arboles in enumerate(rows):
        try:
            record = dict(zip(headers, arboles)) # Creo un diccionario que tenga los headers como clave y los elementos de fila (todavía no definiendo el tipo) como valores
        except ValueError:
            print(f'ERROR. Se ignoró la linea {index + 2} por falta de datos.') # Arrojo un valor en caso de que falten datos (es index + 2 porque el index arranca en 0 y el archivo tiene headers)
        if record['espacio_ve'].lower() == parque.lower():
            arbolesEnParque.append(record)
    if arbolesEnParque == []:
        print('El parque solicitado no se encuentra en la lista.')
        exit
    else:
        return arbolesEnParque

def especies(listaArboles):
    especiesList = []
    for arbol in listaArboles:
        especiesList.append(arbol['nombre_com'])
    return set(especiesList)

def contarEjemplares(listaArboles):
    especiesDict = Counter()
    for arbol in listaArboles:
        especiesDict[arbol['nombre_com']] += 1
    return especiesDict

def obtenerAlturas(listaArboles, especie):
    alturas = []
    for arbol in listaArboles:
        if arbol['nombre_com'].lower() == especie.lower():  
            alturas.append(float(arbol['altura_tot']))
    if alturas == []:
        print(f'La especie no se encuentra en este parque: {parque}')
        exit
    else:
        return alturas

def obtenerInclinaciones(listaArboles, especie):
    inclinaciones = []
    for arbol in listaArboles:
        if arbol['nombre_com'].lower() == especie.lower():  
            inclinaciones.append(float(arbol['inclinacio']))
    if inclinaciones == []:
        print(f'La especie no se encuentra en este parque: {parque}')
        exit
    else:
        return inclinaciones

def especimenMasInclinado(listaArboles):
    listaEspecies = especies(listaArboles)
    dictInclinaciones = {}

    for especie in listaEspecies:
        dictInclinaciones[especie] = max(obtenerInclinaciones(listaArboles, especie))
    # print(dictInclinaciones)
    inclinacionMax = max(dictInclinaciones, key=dictInclinaciones.get)
    return [inclinacionMax, dictInclinaciones[inclinacionMax]]

def especiePromedioMasInclinada(listaArboles):
    listaEspecies = especies(listaArboles)
    dictInclinaciones = {}

    for especie in listaEspecies:
        inclinaciones = obtenerInclinaciones(listaArboles, especie)
        dictInclinaciones[especie] = sum(inclinaciones)/len(inclinaciones)
    inclinacionMax = max(dictInclinaciones, key=dictInclinaciones.get)
    return [inclinacionMax, dictInclinaciones[inclinacionMax]]

parques = ['General Paz', 'Andes, Los', 'Centenario']

for parque in parques:
    print(parque)
    inclinacionPromMax = especiePromedioMasInclinada(leerParque('../Data/arbolado-en-espacios-verdes.csv', parque))
    print(f'El {inclinacionPromMax[0]} es el arbol, en promedio, más inclinado del parque, con una inclinación promedio de {inclinacionPromMax[1]:0.2f} grados')
