x = []
n = 0
positivas = 0

while True:
    y = input('Escreva um número de segundos (-1 para terminar): ')
    if int(y) == -1:
        break
    x.insert(n, y)
    n += 1


for i in range(0, len(x)):
    if int(x[i]) >= 9.5:
        positivas += 1
    
#a) Valor total
print(positivas)

#b) Percentagem
print((positivas * 100) / len(x))