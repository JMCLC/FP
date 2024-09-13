quantia = float(input('Insere um número: '))
dinheiro = {
    'Notas de 50€': 0,
    'Notas de 20€': 0,
    'Notas de 10€': 0,
    'Notas de 5€': 0,
    'Moedas de 2€': 0,
    'Moedas de 1€': 0,
    'Moedas de 50 cent': 0,
    'Moedas de 20 cent': 0,
    'Moedas de 10 cent': 0,
    'Moedas de 5 cent': 0,
    'Moedas de 2 cent': 0,
    'Moedas de 1 cent': 0
}

while quantia > 0:
    if quantia >= 50:
        quantia -= 50
        dinheiro['Notas de 50€'] += 1
    elif quantia >= 20 and quantia < 50:
        quantia -= 20
        dinheiro['Notas de 20€'] += 1
    elif quantia >= 10 and quantia < 20:
        quantia -= 10
        dinheiro['Notas de 10€'] += 1
    elif quantia >= 5 and quantia < 10:
        quantia -= 5
        dinheiro['Notas de 50€'] += 1
    elif quantia >= 2 and quantia < 5:
        quantia -= 2
        dinheiro['Moedas de 2€'] += 1
    elif quantia >= 1 and quantia < 2:
        quantia -= 1
        dinheiro['Moedas de 1€'] += 1
    elif quantia >= 0.5 and quantia < 1:
        quantia -= 0.5
        dinheiro['Moedas de 50 cent'] += 1
    elif quantia >= 0.2 and quantia < 0.5:
        quantia -= 0.2
        dinheiro['Moedas de 20 cent'] += 1
    elif quantia >= 0.1 and quantia < 0.2:
        quantia -= 0.1
        dinheiro['Moedas de 10 cent'] += 1
    elif quantia >= 0.05 and quantia < 0.1:
        quantia -= 0.05
        dinheiro['Moedas de 5 cent'] += 1
    elif quantia >= 0.02 and quantia < 0.05:
        quantia -= 0.02
        dinheiro['Moedas de 2 cent'] += 1
    elif quantia >= 0.01 and quantia < 0.02:
        quantia -= 0.01
        dinheiro['Moedas de 1 cent'] += 1
    else:
        break

print(dinheiro)