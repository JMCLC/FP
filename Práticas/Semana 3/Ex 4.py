def CalcularArea(raio):
    return 3.14 * (raio ** 2)

def Comparar(r1, r2):
    if CalcularArea(r1) > CalcularArea(r2):
        ValueError('Não deveria acontecer')

print(Comparar(10, 2))