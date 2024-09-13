numero = input('Escreva um inteiro positivo: ')
x = []
n = 0
resultado = ''

for i in range(0, len(numero)):
    x.insert(n, numero[i])
    n += 1

for i in range(0, len(numero)):
    resultado += x[n - 1]
    n -= 1

print(resultado)