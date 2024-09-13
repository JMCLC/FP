impares = [1, 3, 5, 7, 9]
numero = input('Escreva um número Inteiro: ')
total = ''

for i in range(0, len(numero)):
    for a in range(0, len(impares)):
        if int(numero[i]) == impares[a]:
            total += numero[i]

print(total)