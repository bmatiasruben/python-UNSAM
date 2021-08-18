# -----------------------------------------------------------------
# Ejercicio 3.6
# -----------------------------------------------------------------

# for n in range(10): 
#     print(n, end=' ')

# for n in range(10,0,-1):
#     print(n, end=' ')

# for n in range(0,10,2): 
#     print(n, end=' ')

# -----------------------------------------------------------------
# Ejercicio 3.7
# -----------------------------------------------------------------

# data = [4, 9, 1, 25, 16, 100, 49]
# print(min(data), max(data), sum(data))

# for n, x in enumerate(data):
#     print(n, x)

# -----------------------------------------------------------------
# Ejercicio 3.8
# -----------------------------------------------------------------

def costoCamion(archivo):
    f = open(archivo, 'rt')
    headers = next(f)
    costoTotal = 0
    for index, line in enumerate(f):
        try:
            row = line.split(',')
            costoTotal += int(row[1])*float(row[2])
        except ValueError:
            print(f'Fila {index + 2}: No pude interpretar: {row}')
        
    f.close()
    return(costoTotal)

costo = costoCamion('../Data/missing.csv')
print('Costo total:', costo)