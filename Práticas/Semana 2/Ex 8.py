n = 0
x = []

while True:
    y = int(input('Escreva um número de segundos (um número negativo para terminar): '))
    if y < 0:
        break
    x.insert(n, y)
    print(x[n] / 60 / 60 / 24)
    n += 1
