x = int(input('Insere um número para X: '))
n = int(input('Insere um número para Y: '))
valor = 0

def Fatorial(a):
    fatorial = 1
    for i in range(1, a + 1):
        fatorial *= i
    return fatorial

for i in range(0, n + 1):
    valor += (x ** i) / Fatorial(i)

print(valor)