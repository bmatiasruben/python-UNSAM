# -----------------------------------------------------------------
# Ejercicio 1.7
# -----------------------------------------------------------------

# saldo = 500000.0
# tasa = 0.05
# pagoMensual = 2684.11
# totalPagado = 0.0

# while saldo > 0:
#     saldo += saldo * tasa/12 - pagoMensual
#     totalPagado += pagoMensual

# print('Total pagado:', round(totalPagado, 2))

# -----------------------------------------------------------------
# Ejercicio 1.8
# -----------------------------------------------------------------

# saldo = 500000.0
# tasa = 0.05
# pagoMensual = 2684.11
# totalPagado = 0.0
# mes = 0

# while saldo > 0:
#     if mes < 12:
#         saldo += saldo * tasa/12 - 1000
#         totalPagado += pagoMensual + 1000
#     else:
#         saldo += saldo * tasa/12 - pagoMensual
#         totalPagado += pagoMensual
#     mes += 1

# print('Total pagado:', round(totalPagado, 2))
# print('pagado en:', mes, 'meses')

# -----------------------------------------------------------------
# Ejercicio 1.9
# -----------------------------------------------------------------

# saldo = 500000.0
# tasa = 0.05
# pagoMensual = 2684.11
# totalPagado = 0.0
# mes = 0
# pagoExtraComienzo = 61
# pagoExtraFinal = 108
# pagoExtra = 1000

# while saldo > 0:
#     if (mes >= pagoExtraComienzo - 1 and mes < pagoExtraFinal):
#         saldo += saldo * tasa/12 - pagoMensual - pagoExtra
#         totalPagado += pagoMensual + pagoExtra
#     else:
#         saldo += saldo * tasa/12 - pagoMensual
#         totalPagado += pagoMensual
#     mes += 1

# print('Total pagado:', round(totalPagado, 2))
# print('pagado en:', mes, 'meses')

# -----------------------------------------------------------------
# Ejercicio 1.10
# -----------------------------------------------------------------

# saldo = 500000.0
# tasa = 0.05
# pagoMensual = 2684.11
# totalPagado = 0.0
# mes = 0
# pagoExtraComienzo = 61
# pagoExtraFinal = 108
# pagoExtra = 1000

# while saldo > 0:
#     if (mes >= pagoExtraComienzo - 1 and mes < pagoExtraFinal):
#         saldo += saldo * tasa/12 - pagoMensual - pagoExtra
#         totalPagado += pagoMensual + pagoExtra
#     else:
#         saldo+= saldo * tasa/12 - pagoMensual
#         totalPagado += pagoMensual
#     mes += 1
#     print(mes, round(totalPagado, 2), round(saldo, 2))

# print('Total pagado:', round(totalPagado, 2))
# print('pagado en:', mes, 'meses')

# -----------------------------------------------------------------
# Ejercicio 1.12
# -----------------------------------------------------------------

# "False" es una variable tipo string, el valor de verdad de un string es verdadero siempre que tenga algo, y falso si está vacío
# >>> bool("Texto")
# True
# >>> bool("")
# False

# -----------------------------------------------------------------
# Ejercicio 1.14
# -----------------------------------------------------------------

# frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'

# for i in range(5):
#     print('frutas[',-2 + i,']: ', frutas[-2 + i])

# -----------------------------------------------------------------
# Ejercicio 1.15
# -----------------------------------------------------------------

# frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'

# frutas = frutas + 'Pera'

# frutas = frutas.replace('Pera', ',Pera')

# frutas = 'Melón,' + frutas

# -----------------------------------------------------------------
# Ejercicio 1.16
# -----------------------------------------------------------------

# frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'

# frutas = 'Melón,' frutas + ',Pera'

# -----------------------------------------------------------------
# Ejercicio 1.17
# -----------------------------------------------------------------

# cadena = "Ejemplo con for"
# contador = 0

# for c in cadena:
#     if c == 'o':
#         contador += 1
#     print('caracter:', c)

# print('Cantidad de o:', contador)


# -----------------------------------------------------------------
# Ejercicio 1.20
# -----------------------------------------------------------------

# saldo = 500000.0
# tasa = 0.05
# pagoMensual = 2684.11
# totalPagado = 0.0
# mes = 0
# pagoExtraComienzo = 61
# pagoExtraFinal = 108
# pagoExtra = 1000

# while saldo > 0:
#     if (mes >= pagoExtraComienzo - 1 and mes < pagoExtraFinal):
#         if saldo * (1 + tasa/12) < pagoMensual + pagoExtra:
#             saldo = 0
#             totalPagado += saldo * (1 + tasa/12)
#         else:
#             saldo += saldo * tasa/12 - pagoMensual - pagoExtra
#             totalPagado += pagoMensual + pagoExtra
#     else:
#         if saldo * (1 + tasa/12) < pagoMensual:
#             totalPagado += saldo * (1 + tasa/12)
#             saldo = 0
#         else:
#             saldo += saldo * tasa/12 - pagoMensual
#             totalPagado += pagoMensual

#     mes += 1
#     print(f'Tardó {mes} meses en pagar ${round(totalPagado, 2)}, con un saldo de {round(saldo, 2)}')

# print('Total pagado:', round(totalPagado, 2))
# print('pagado en:', mes, 'meses')

