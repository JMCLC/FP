x = [0, 0, 0]
n = 0
highest = 0

while n < 3:
    x[n] = int(input('Insere um número: '))
    n += 1


for i in range(0, len(x)):
    if highest < x[i]:
        highest = x[i]

print(highest)