cadena = 'Erase una vez'
capadepenapa = ''
for c in cadena:
    if (c != 'a') & (c != 'e') & (c != 'i') & (c != 'o') & (c != 'u'):
        capadepenapa = capadepenapa + c
    else:
        capadepenapa = capadepenapa + c + 'p' + c
print (capadepenapa)