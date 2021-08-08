# -----------------------------------------------------------------
# Ejercicio 1.13
# -----------------------------------------------------------------

print('------ Calculadora del volúmen de una esfera ------')

while True:
    try:
        radio = float(input('Ingrese el radio de la esfera: '))
        if radio < 0:
            raise ValueError
        break
    except ValueError:
        print('ERROR! Ingrese un radio válido')

pi = 3.14159265359

print('El volumen de la esfera es:', 4/3 * pi * radio ** 3)

# Obtuve
# Ingrese el radio de la esfera: 6
# El volumen de la esfera es: 904.77868423392