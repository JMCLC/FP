km = int(input('Distância Percorrida (em kilómetros) : '))
t = int(input('Tempo Demorado (em minutos) : '))

#a)

h = t / 60
km_h = km / h

print(str(km_h) + ' km/h')

#b)

s = t * 60
m = km * 1000
m_s = m / s

print(str(m_s) + ' m/s')