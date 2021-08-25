import csv
def leer_camion(lugar):
    with open(lugar,'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)

        camion = []
        for row in rows:
            camion.append((row[0],row[1],row[2]))

        return camion


lugar = '../Data/camion.csv'

camion = leer_camion(lugar)
print(camion)

total = 0
for nombre, cajones, precio in camion:
    total += int(cajones) * float(precio)

print('Total es: ',total)