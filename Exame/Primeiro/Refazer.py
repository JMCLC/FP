###################
##### PARTE 1 #####
###################

#Exercicio 1

def nova_arv():
    return {'r': 0, 'ae': {}, 'ad': {}}

def cria_arv(r, ae, ad):
    return {'r': r, 'ae': ae, 'ad': ad}

def raiz(a):
    return a['r']

def arv_esq(a):
    return a['ae']

def arv_dir(a):
    return a['ad']

def eh_arv(arg):
    if type(arg) == dict and len(arg) == 3:
        items = arg.items()
        for k, v in range(len(items)):
            if items[k] in ('r', 'ae', 'ad'):
                if type(raiz(arg)) == int and type(arv_esq(arg)) == dict and type(arv_dir(arg)) == dict:
                    return True
    return False

def eh_arv_vazia(a):
    if eh_arv(a):
        if raiz(a) == 0 and arv_esq(a) == {} and arv_dir(a) == {}:
            return True
    return False

def arv_iguais(a, a2):
    return eh_arv(a) and eh_arv(a2) and raiz(a) == raiz(a2) and arv_esq(a) == arv_esq(a2) and arv_dir(a) == arv_dir(a2)

#Exercicio 2


#Exercicio 3

#a)

# <resultado> ::= a <random> <random> d
# 
# 
# 
# 

#b)

def verificacao(string):
    if string[0] != 'a' and string[-1] != 'd':
        return False
    changed = False
    tamanho = 0
    for i in range(1, len(string) - 1):
        if string[i] not in ('b', 'c'):
            return False    
        if string[1] == string[i] and changed:
            return False
        if string[1] != string[i] and string[i] != string[-1]:
            changed = True
            tamanho = i - 1
        if i == len(string) - 2 and tamanho != i - tamanho:
            return False
    return True

#Exercicio 4

def codifica(n):
    n = list(str(n)[::-1])
    res = ''
    for i in range(len(n)):
        n[i] = int(n[i])
        if n[i] % 2 == 0:
            if n[i] != 0:
                n[i] = n[i] - 2
            else:
                n[i] = 8
        else:
            if n[i] != 9:
                n[i] = n[i] + 2
            else:
                n[i] = 1
        res += str(n[i])
    return res

###################
##### PARTE 2 #####
###################

#Exercicio 1
def soma_dicionarios(d, d2):
    d3 = dict(d, **d2)
    for k in d:
        if k in d3:
            for v in d[k]:
                if v not in d3[k]:
                    d3[k] = sorted(d3[k] + [v])
    return d3

#Exercicio 2

def eh_primo(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

#a)
def soma_divisores_primos_recursao(n):
    def soma_auxiliar(n, i):
        if n < i:
            return 0
        if n % i == 0 and eh_primo(i):
            return i + soma_auxiliar(n, i + 1)
        return soma_auxiliar(n, i + 1)
    if n == 0:
        return 0
    return soma_auxiliar(n, 1)

#b)
def soma_divisores_primos_cauda(n, i = 1, res = 0):
    if n == 0:
        return 0
    if i > n:
        return res
    else:
        if n % i == 0 and eh_primo(i):
            return soma_divisores_primos_cauda(n, i + 1, res + i)
        return soma_divisores_primos_cauda(n, i + 1, res)

#c)
def soma_divisores_primos(n):
    def obter_divisores(n):
        i = 1
        l = []
        while i <= n:
            if n % i == 0 and eh_primo(i):
                l.append(i)
            i += 1
        return l
    if n == 0:
        return 0
    l = obter_divisores(n)
    res = 0
    for i in range(len(l)):
        res += l[i]
    return res

###################
##### PARTE 3 #####
###################

#Exercicio 1
def mantem_multiplos(l, n):
    res = []
    for i in range(len(l)):
        if l[i] % n == 0:
            res += [l[i]]
    return res

#Exercicio 2
def apenas_digitos_pares(n):
    res = 0
    while n != 0:
        dig = n % 10
        if dig % 2 == 0:
            res = (res * 10) + dig
        n = n // 10
    # Da valor invertido
    return int(str(res)[::-1])

#Exercicio 3
class piscina():
    def __init__(self, limite):
       self.lotacao = limite
       self.ocupacaoAtual = 0
       self.custoInicial = 2
       self.bi = []
       self.horas = []

    def entra(self, bi, h, m):
        def verificacoes(self, bi, h, m):
            if bi in self.bi:
                raise ValueError('entra: a pessoa esta na piscina')
            if h not in range(1, 25) or m not in range(1, 61):
                raise ValueError('entra: argumentos invalidos')
            if self.ocupacaoAtual == self.lotacao:
                raise ValueError('entra: a piscina esta cheia')
        verificacoes(self, bi, h, m)
        self.bi += [bi]
        self.ocupacaoAtual += 1
        self.horas += [[h, m]]
        return self.ocupacaoAtual

    def sai(self, bi, h, m):
        if bi not in self.bi:
            raise ValueError('sai: a pessoa nao esta na piscina')
        for i in range(len(self.bi)):
            if self.bi[i] == bi:
                index = i
        if h not in range(1, 25) or m not in range(1, 61):
            raise ValueError('sai: argumentos invalidos')
        elif self.horas[i][0] > h:
            raise ValueError('sai: horas erradas')
        elif self.horas[i][0] == h and self.horas[i][1] > m:
            raise ValueError('sai: horas erradas')
        res = self.custoInicial
        if h > self.horas[index][0]:
            print(h, self.horas[index][0], h - self.horas[index][0])
            res += (h - self.horas[index][0]) * 0.5
        if m > 0:
            res += 0.5
        self.ocupacaoAtual -= 1
        self.bi.pop(index)
        self.horas.pop(index)
        return 'valor a pagar: Euro ' + str(res)

    def ocupacao(self):
        return self.ocupacaoAtual

#Exercicio 4
def todos_lista(l, func):
    return l == filter(l, func)