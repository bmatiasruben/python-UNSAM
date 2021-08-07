grosorBillete = 0.11 * 0.001 # Grosor de un billete en metros
alturaObelisco = 67.5 # Altura del obelisco en metros
numBilletes = 1
dia = 1

while grosorBillete * numBilletes <= alturaObelisco:
    print(dia, numBilletes, numBilletes * grosorBillete)
    dia += 1
    numBilletes *= 2

print('Cantidad de días: ', dia)
print('Cantidad de billetes: ', numBilletes)
print('Altura final: ', numBilletes * grosorBillete)

# -----------------------------------------------------------------
# Ejercicio 1.4
# -----------------------------------------------------------------

# obelisco.py

# grosor_billete = 0.11 * 0.001 # 0.11 mm en metros
# altura_obelisco = 67.5         # altura en metros
# num_billetes = 1
# dia = 1

# while num_billetes * grosor_billete <= altura_obelisco:
#     print(dia, num_billetes, num_billetes * grosor_billete)
#     dia = dias + 1
#     num_billetes = num_billetes * 2

# print('Cantidad de días', dia)
# print('Cantidad de billetes', num_billetes)
# print('Altura final', num_billetes * grosor_billete)

# El error está en la linea 10, porque la variable dias no existe. La sentencia correcta sería dia = dia + 1