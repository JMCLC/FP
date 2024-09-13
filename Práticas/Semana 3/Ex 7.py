def Valor(q, j, n):
    if type(q) != int or j <= 0 or j >= 1 or type(n) != int:
        ValueError('Algum dos numeros nao esta no formato correto')