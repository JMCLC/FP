n = 0
x = []
total = ''

while True:
    y = input('Escreva um dígito (-1 para terminar): ')
    if int(y) < 0:
        for i in range(0, len(x)):
            if x != []:    
                total += str(x[i])
            else:
                total = '0'
        print(total)
        break
    x.insert(n, y)
    n += 1
    
