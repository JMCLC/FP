horas_trabalhadas = int(input('Horas Trabalhadas: '))
salário_hora = int(input('Salário à hora: '))
salário = 0

if horas_trabalhadas > 40:
    extras = horas_trabalhadas - 40
    extra_salário = extras * (salário_hora * 2)
    salário = extra_salário + (salário_hora * 40)
else:
    salário = horas_trabalhadas * salário_hora

print(salário)
