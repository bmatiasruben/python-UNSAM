# -----------------------------------------------------------------
# Ejercicio 3.17
# -----------------------------------------------------------------

def multiplosN(n):
    'Me calcula los primeros 10 múltiplos del numero n. Devuelve una lista con los valores.'
    multiplos = []
    multiplo = 0
    for i in range(10):
        multiplo += n
        multiplos.append(multiplo)
    return multiplos
    
header = f'{"":>4s}'
separador = f'{"":->5s}'
lineas = []

for i in range(10):
    header += f'{i:4d}'
    separador += f'{"":->4s}'
    linea = f'{str(i) + ":":<4s}' 
    multiplos = multiplosN(i)
    for j in range(10):
        linea += f'{multiplos[i]:4d}'
    lineas.append(linea)

print(header)
print(separador)
for linea in lineas:
    print(linea)

