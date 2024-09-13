def soma_divisores(n):
    i = 1
    res = 0
    while i <= n:
        if n % i == 0:
            res += i
        i += 1
    return res

def codifica(n):
    num = {0: 8, 1: 3, 2: 0, 3: 5, 4: 2, 5: 7, 6: 4, 7: 9, 8: 6, 9: 1}
    res = list(str(n))
    for i in range(len(res)):
        res[i] = str(num[int(res[i])])
    res.reverse()
    return ''.join(res)

def junta_ordenados(t, t2):
    t = list(t)
    for i in range(len(t2)):
        t.append(t2[i])
    return tuple(sorted(t))

def soma_cumulativa(l):
    for i in range(1, len(l)):
        l[i] = l[i] + l[i - 1]
    return l

def soma_pares(l):
    soma = 0
    for i in range(len(l)):
        soma += l[i] if l[i] % 2 == 0 else 0
    return soma

def soma_pares2(l):
    if l == []:
        return 0
    return l[0] + soma_pares2(l[1:]) if l[0] % 2 == 0 else soma_pares(l[1:])

def soma_pares3(l, res = 0):
    if l == []:
        return res
    return soma_pares3(l[1:], l[0] + res) if l[0] % 2 == 0 else soma_pares3(l[1:], res)

def soma_pares4(l):
    return acumula(lambda x, y: x + y, filtra(lambda x: x % 2 == 0, l))


def todos_lista(l, func):
    return l == filter(l, func)