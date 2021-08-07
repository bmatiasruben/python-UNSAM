# -----------------------------------------------------------------
# Ejercicio 1.5
# -----------------------------------------------------------------

altura = 100 # Altura en metros
rebotes = 0 # Cantidad de veces que la pelota rebotó contra el piso

for i in range(10):
    altura *= 3/5
    rebotes += 1
    print(rebotes, round(altura, 4))
