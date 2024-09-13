n = 1
numero = ''

while n < 10:
    for i in range(1, n + 1):
        numero += str(n)
        resultado = int(numero) * 8 + n
        print(numero + ' x  8 + ' + str(n) + ' = ' + str(resultado))
        n += 1
        if n >= 10:
            break