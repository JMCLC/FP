numero = input('Insere um número: ')
total = 0

for i in range(0, len(numero)):
    total += int(numero[i])

print(total)