palabra = input('Ingrese palabra')
jeringoso = ''
    
for i in range (len(palabra)):
    if palabra [i] == 'a':
        jeringoso = jeringoso +'apa'
    elif palabra [i] == 'e':
        jeringoso = jeringoso +'epe'
    elif palabra [i] == 'i':
        jeringoso = jeringoso + 'ipi'
    elif palabra [i] == 'o':
        jeringoso = jeringoso +'opo'
    elif palabra [i] == 'u':
        jeringoso = jeringoso +'upu'
    else:
        jeringoso = jeringoso + palabra[i]

print(jeringoso)
    