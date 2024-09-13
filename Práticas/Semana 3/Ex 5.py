def Bissexto(ano):
    if (ano % 4 == 0 and ano % 10 != 0) or (ano % 4 == 0 and ano % 400 == 0):
        return True
    return False

print(Bissexto(1984))