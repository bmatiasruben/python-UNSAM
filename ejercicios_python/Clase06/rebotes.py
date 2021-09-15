# -----------------------------------------------------------------
# Ejercicio 1.5
# -----------------------------------------------------------------

altura = 100 # Altura en metros
rebotes = 0 # Cantidad de veces que la pelota rebotó contra el piso

for i in range(10):
    altura *= 3/5
    rebotes += 1
    print(rebotes, round(altura, 4))

# Obtuve
# 1 60.0
# 2 36.0
# 3 21.6
# 4 12.96
# 5 7.776
# 6 4.6656
# 7 2.7994
# 8 1.6796
# 9 1.0078
# 10 0.6047