total = ''
while True:
    y = input('Escreva um número de segundos (-1 para terminar): ')
    if int(y) == -1:
        print(total)
        break
    total += y