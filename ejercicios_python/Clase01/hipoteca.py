# -----------------------------------------------------------------
# Ejercicio 1.11
# -----------------------------------------------------------------

saldo = 500000.0 
tasa = 0.05 
pagoMensual = 2684.11
totalPagado = 0.0 
mes = 0
pagoExtraComienzo = 61
pagoExtraFinal = 108
pagoExtra = 1000

while saldo > 0:
    if (mes >= pagoExtraComienzo - 1 and mes < pagoExtraFinal):
        if saldo * (1 + tasa/12) < pagoMensual + pagoExtra:
            saldo = 0
            totalPagado += saldo * (1 + tasa/12)
        else:
            saldo += saldo * tasa/12 - pagoMensual - pagoExtra
            totalPagado += pagoMensual + pagoExtra
    else:
        if saldo * (1 + tasa/12) < pagoMensual:
            totalPagado += saldo * (1 + tasa/12)
            saldo = 0
        else:
            saldo += saldo * tasa/12 - pagoMensual
            totalPagado += pagoMensual

    mes += 1
    print(mes, round(totalPagado, 2), round(saldo, 2))

print('Total pagado:', round(totalPagado, 2))
print('Pagado en:', mes, 'meses')

# Obtuve al final
# Total pagado: 878202.57
# Pagado en: 310 meses
