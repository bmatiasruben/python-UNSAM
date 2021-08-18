# -----------------------------------------------------------------
# Ejercicio 2.7
# -----------------------------------------------------------------

def buscarPrecio(fruta):
    f = open('../Data/precios.csv', 'rt')

    for line in f:
        row = line.split(',')
        if row[0].lower() == fruta.lower():
            return row[1]
        f.close()

    return False    
    
fruta = input('Ingrese la fruta a buscar el precio: ')

precio = buscarPrecio(fruta)

if precio == False:
    print(f'{fruta} no figura en el listado de precios')
else:
    print(f'El precio de un cajón de {fruta} es: {precio}')