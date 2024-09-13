x = int(input('Escreva um inteiro positivo \n'))
conta = 0

while x > 0:
    conta += int(x % 10)
    x /= 10

while conta >= 9:
    conta -= 9

print(conta)

