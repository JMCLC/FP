def filtra(lista, tst):
    if not lista:
        return []
    if tst(lista[0]):
        return [lista[0],] + filtra(lista[1::], tst)
    else:
        return filtra(lista[1:], tst)

print(filtra([1, 2, 3, 4, 5], lambda x : x % 2 == 0))

def transforma(lista, fn):
    if not lista:
        return []
    return [fn(lista[0]),] + transforma(lista[1:], fn)

print(transforma([1, 2, 3, 4], lambda x : x ** 3))

def acumula(lista, fn):
    if len(lista) == 1:
        return lista[0]
    return fn(lista[0], acumula(lista[1:], fn))

print(acumula([1, 2, 3, 4], lambda x, y : x + y))