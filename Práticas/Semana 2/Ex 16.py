numero = input('Insere um número: ')
n = 0
resultado = ''

for i in range(0, len(numero)):
    resultado += numero[i]
    n += 1

while n > 0:
    resultado += numero[n - 1]
    n -= 1

print(resultado)