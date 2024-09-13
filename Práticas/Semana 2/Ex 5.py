from math import sqrt

n = 0
x = [0, 0, 0, 0, 0]

while n < 5:
    x[n] = int(input('Insere um número: '))
    n += 1

def CalculateAverage():
    total = 0
    for i in range(0, len(x)):
        total += x[i]
    return total / len(x)

def Calculations():
    average = CalculateAverage()
    value = 0
    for i in range(0, len(x)):
        value += (i - average)**2
    value = sqrt(value * 0.25)
    return value

print(Calculations())