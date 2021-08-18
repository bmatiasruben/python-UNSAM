# -----------------------------------------------------------------
# Ejercicio 2.1
# -----------------------------------------------------------------

# with open('../Data/camion.csv', 'rt') as f:
#     for line in f:
#         print(line, end = '')

# --------------------------

# f = open('../Data/camion.csv', 'rt')
# headers = next(f).split(',')
# print(headers)
# for line in f:
#     row = line.split(',')
#     print(row)

# f.close()

# -----------------------------------------------------------------
# Ejercicio 2.3
# -----------------------------------------------------------------

# f = open('../Data/precios.csv', 'rt')

# for line in f:
#     row = line.split(',')
#     if row[0] == 'Naranja':
#         print('El precio de la naranja es', row[1])

# f.close()

# -----------------------------------------------------------------
# Ejercicio 2.4
# -----------------------------------------------------------------

# import gzip

# with gzip.open('../Data/camion.csv.gz', 'rt') as f:
#     for line in f:
#         print(line, end = '')

# -----------------------------------------------------------------
# Ejercicio 2.5
# -----------------------------------------------------------------

# def saludar(nombre):
#     'Saluda a alguien'
#     print('Hola', nombre)

# nombre = input('Ingrese el nombre de a quien desea saludar: ')
# saludar(nombre)

# -----------------------------------------------------------------
# Ejercicio 2.7
# -----------------------------------------------------------------

# def buscarPrecio(fruta):
#     f = open('../Data/precios.csv', 'rt')

#     for line in f:
#         row = line.split(',')
#         if row[0].lower() == fruta.lower():
#             return row[1]
#             f.close()

#     return False    
    
# fruta = input('Ingrese la fruta a buscar el precio: ')

# precio = buscarPrecio(fruta)

# if precio == False:
#     print(f'{fruta} no figura en el listado de precios')
# else:
#     print(f'El precio de un cajón de {fruta} es: {precio}')

# -----------------------------------------------------------------
# Ejercicio 2.8a
# -----------------------------------------------------------------

def preguntarEdad(nombre):
    edad = int(input(f'ingresá tu edad {nombre}: '))
    if edad<0:
        raise ValueError('La edad no puede ser negativa.')
    return edad

# nombre = input('Ingresa tu nombre: ')
for nombre in ['Pedro','Juan','Caballero']:
    try:
        edad = preguntarEdad(nombre)
        print(f'{nombre} tiene {edad} años.')
    except ValueError:
        print(f'{nombre} no ingresó una edad válida.')