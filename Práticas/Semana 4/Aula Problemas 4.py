def ordenado_decrescente(tuplo):
    for i in range(len(tuplo) - 1):
        if tuplo[i] < tuplo[i + 1]:
            return False
    return True

print(ordenado_decrescente((202,33,23,4,76)))