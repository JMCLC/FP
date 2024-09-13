s = int(input('Número de Segundos: '))
dias = s / 60 / 60 / 24
horas = 0 
minutos = 0
segundos = 0 
resto = dias - int(dias)

if resto != 0:
    horas = resto * 60
    resto = horas - int(horas)
    if resto != 0:
        minutos = resto * 60
        resto = minutos - int(minutos)
        if resto != 0:
            segundos = resto * 60 

print(str(int(dias)) + ' Dias : ' + str(int(horas)) + ' Horas : ' + str(int(minutos)) + ' Minutos : ' + str(int(segundos)) + ' Segundos')