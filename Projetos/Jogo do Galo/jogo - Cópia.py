### Jose Maria Cardoso ist199096 ###

""" Valor global do tabuleiro que vai ser alterado a medida que a funcao jogo_do_galo() e corrida """
tuplo = ((0,0,0),(0,0,0),(0,0,0)) 

"""Dicionario com as posicoes no tabuleiro em forma de colunas / linhas / diagonais de forma a simplificar o codigo em certas funcoes"""
posicoes = { 
    'linha': ((1,2,3),(4,5,6),(7,8,9)),
    'coluna': ((1,4,7),(2,5,8),(3,6,9)),
    'diagonal': ((1,5,9),(7,5,3)),
}

""" Dicionario que identifica o que taticas cada dificuldade pode utilizar """
jogadas = { 
    'basico': ('centro', 'cantoVazio', 'lateralVazia'),
    'normal': ('vitoria', 'bloqueio', 'centro', 'cantoOposto', 'cantoVazio', 'lateralVazia'),
    'perfeito': ('vitoria', 'bloqueio', 'bifurcacao', 'bloqueioBifurcacao', 'centro', 'cantoOposto', 'cantoVazio', 'lateralVazia')
}

""" Dicionario que atraves da string que escolheram na funcao jogo_do_galo() utiliza 1 ou -1 para identificar o jogador """
numero = {
    'X': 1,
    'O': -1
}

""" Dicionario que identifica a string do vencedor atraves do numero que estavam a utilizar """
vencedor = {
    1: 'X',
    0: 'EMPATE',
    -1: 'O'
}

""" Variavel utilizada para o valor da posicao ser returnada na funcao escolher_posicao_auto() esta variavel e necessaria devido a utilizacao das classes """
posicaoAutoEscolhida = None 

def eh_tabuleiro(tuplo): 
    """ Funcao que verifica se o tabuleiro recebido e de facto um tabuleiro corretamente criado (INPUT -> exemplo:((0,0,0),(0,0,0),(0,0,0)), OUTPUT -> Boolean) """
    if len(tuplo) != 3 or type(tuplo) != tuple:
        return False
    for i in range(len(tuplo)):
        for a in range(len(tuplo[i])):
            if (type(tuplo[i][a]) != int) or (tuplo[i][a] not in (-1, 0, 1)) or (len(tuplo[i]) != 3) or (type(tuplo[i]) != tuple):
                return False
    return True

def eh_posicao(posicao): 
    """ Funcao que verifica se a posicao dada e valida (INPUT -> posicao, OUTPUT -> Boolean) """
    if type(posicao) != int:
        return False
    return 1 <= posicao <= 9

def obter_coluna(tuplo, index):
    """ Funcao que le um tabuleiro e numero da coluna e retorna essa coluna (INPUT -> tabuleiro, numeroDaColuna (valor de 1 a 3), OUTPUT -> tuplo) """
    if (index not in (1,2,3) or type(index) != int) or ((not eh_tabuleiro(tuplo)) or type(tuplo) != tuple):
        raise ValueError('obter_coluna: algum dos argumentos e invalido')
    t = ()
    for i in range(len(tuplo)):
        t = t + (tuplo[i][index - 1],)
    return t

def obter_linha(tuplo, index): 
    """ Funcao que le um tabuleiro e numero da linha e retorna essa linha (INPUT -> tabuleiro, numeroDaLinha (valor de 1 a 3), OUTPUT -> tuplo) """
    if (index not in (1,2,3) or type(index) != int) or ((not eh_tabuleiro(tuplo)) or type(tuplo) != tuple):
        raise ValueError('obter_linha: algum dos argumentos e invalido')
    return tuplo[index - 1]

def obter_diagonal(tuplo, index):
    """ Funcao que le um tabuleiro e numero da diagonal e retorna essa diagonal (INPUT -> tabuleiro, numeroDaDiagonal (valor de 1 a 2), OUTPUT -> tuplo) """
    if (index not in (1,2) or type(index) != int) or ((not eh_tabuleiro(tuplo)) or type(tuplo) != tuple):
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')
    if index == 1:
        return (tuplo[0][0], tuplo[1][1], tuplo[2][2])
    else:
        return (tuplo[2][0], tuplo[1][1], tuplo[0][2])

def tabuleiro_str(tuplo):
    """ Funcao cria uma string do tabuleiro de modo a dar print a este na funcao jogo_do_galo() (INPUT -> tabuleiro, OUTPUT -> str) """
    output = ''
    dicionario = {
        '1': ' X',
        '0': '  ',
        '-1': ' O'
    }
    if (not eh_tabuleiro(tuplo)) or (type(tuplo) != tuple):
        raise ValueError('tabuleiro_str: o argumento e invalido')
    for i in range(len(tuplo)):
        for a in range(len(tuplo[i])):
            string = dicionario[str(tuplo[i][a])]
            if a == 2 and i != 2:
                string += ' \n-----------\n'
            elif a != 2:
                string += ' |' 
            elif a == 2 and i == 2:
                string += ' ' 
            output += string
    return output

def transformar_posicao(linha, coluna): 
    """ Funcao que utiliza o dicionario posicoes para devolver o valor duma posicao atraves da sua linha e coluna (INPUT -> linha, coluna, OUTPUT -> int(valor de 1 a 9)) """
    return posicoes['linha'][linha][coluna]

def eh_posicao_livre(tuplo, posicao): 
    """ Funcao que recebe o tabuleiro e uma posicao e verifica se esta esta vazia (INPUT -> tabuleiro, posicao(valor de 1 a 9), OUTPUT -> Boolean) """
    if (not eh_posicao(posicao) or type(posicao) != int) or (not eh_tabuleiro(tuplo) or type(tuplo) != tuple):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    a = 1
    for i in range(len(tuplo)):
        for a in range(len(tuplo[i])):
            if transformar_posicao(i,a) == posicao and tuplo[i][a] == 0:
                return True
    return False

def obter_posicoes_livres(tuplo): 
    """ Funcao que recebe o tabuleiro e devolve todas as posicoes livres neste (INPUT -> tabuleiro, OUTPUT -> tuplo) """
    if not eh_tabuleiro(tuplo) or type(tuplo) != tuple:
        raise ValueError('obter_posicoes_livres: o argumento e invalido')
    t = ()
    for i in range(len(tuplo)):
        for a in range(len(tuplo[i])):
            if tuplo[i][a] == 0:
                t += (transformar_posicao(i,a),)
    return t

def jogador_ganhador(tuplo):
    """ Funcao que recebe o tabuleiro e verifica se alguem ganhou o jogo e quem o ganhou (INPUT -> tabuleiro, OUPUT -> 0,1,-1) """
    if not eh_tabuleiro(tuplo) or type(tuplo) != tuple:
        raise ValueError('jogador_ganhador: o argumento e invalido')
    i, a = 1, 1
    while i <= 3:
        coluna = obter_coluna(tuplo, i)
        linha = obter_linha(tuplo, i)
        if (coluna[0] == coluna[1] == coluna[2]):
            return coluna[0]
        elif (linha[0] == linha[1] == linha[2]):
            return linha[0]
        i += 1
    while a <= 2:
        diagonal = obter_diagonal(tuplo, a)
        if (diagonal[0] == diagonal[1] == diagonal[2]):
            return diagonal[0]
        a += 1
    return 0
        
def marcar_posicao(tab, jogador, posicao):
    """ Funcao que recebe o tabuleiro, o jogador, e a posicao e identifica que o jogador escolheu essa posicao e altera o tabuleiro (INPUT -> tabuleiro, jogador(valor 1 ou -1), posicao(valor em 1 a 9), OUTPUT -> tabuleiro) """
    if ((not eh_tabuleiro(tab)) or type(tab) != tuple) or (jogador not in (-1,1) or type(jogador) != int) or (posicao not in obter_posicoes_livres(tab) or type(posicao) != int):
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    global tuplo
    lista = list(tab)
    for i in range(len(lista)):
        lista[i] = list(lista[i])
        for a in range(len(lista[i])):
            if transformar_posicao(i , a) == posicao:
                lista[i][a] = jogador
        lista[i] = tuple(lista[i])
    tuplo = tuple(lista)
    return tuple(lista)

def escolher_posicao_manual(tuplo): 
    """ Funcao utilizada em jogo_do_galo() de modo a permitir o jogador jogar """
    posicao = int(input("Turno do jogador. Escolha uma posicao livre: "))
    if (posicao not in obter_posicoes_livres(tuplo)): 
        raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')
    if (not eh_tabuleiro(tuplo)) or (type(tuplo) != tuple):
       raise ValueError('escolher_posicao_manual: o argumento e invalido')
    return posicao

def posicao_interesecao(index, tipo, index2, tipo2): 
    """ Funcao auxiliar que recebe duas linhas, colunas ou diagonais e o seu numero e indentifica a sua intersecao se existir (INPUT -> index(valor de 1 a 3 ou 2 se for diagonal), tipo('linha', 'diagonal', 'coluna'), index2(igual a index), tipo2(igual a tipo), OUTPUT -> posicao) """
    for i in range(len(posicoes[tipo][index])):
        for a in range(len(posicoes[tipo2][index2])):
            if posicoes[tipo][index][i] == posicoes[tipo2][index2][a]:
                return posicoes[tipo][index][i]
    return 0

class Poder: 
    """ Classe de funcoes que faz a verificacao das jogadas para identificar se a pode realizar ou nao (INPUT -> jogador, OUTPUT -> Boolean) esta funcao utiliza o tabuleiro global de modo a simplificar o codigo """
    def Ganhar(self, jogador):
        i, a = 1, 1
        while i <= 3:
            coluna = obter_coluna(tuplo, i)
            linha = obter_linha(tuplo, i)
            if (coluna[0] == coluna[1] == jogador) and eh_posicao_livre(tuplo, transformar_posicao(2, i - 1)):
                return True
            elif (coluna[1] == coluna[2] == jogador) and eh_posicao_livre(tuplo, transformar_posicao(0, i - 1)):
                return True
            elif (coluna[0] == coluna[2] == jogador) and eh_posicao_livre(tuplo, transformar_posicao(1, i - 1)):
                return True
            elif (linha[0] == linha[1] == jogador) and eh_posicao_livre(tuplo, transformar_posicao(i - 1, 2)):
                return True
            elif (linha[1] == linha[2] == jogador) and eh_posicao_livre(tuplo, transformar_posicao(i - 1, 0)):
                return True
            elif (linha[0] == linha[2] == jogador) and eh_posicao_livre(tuplo, transformar_posicao(i - 1, 1)):
                return True
            i += 1
        while a <= 2:
            diagonal = obter_diagonal(tuplo, a)
            if (diagonal[0] == diagonal[1] == jogador) and eh_posicao_livre(tuplo, posicoes['diagonal'][a - 1][2]):
                return True
            elif (diagonal[1] == diagonal[2] == jogador) and eh_posicao_livre(tuplo, posicoes['diagonal'][a - 1][0]):
                return True
            elif (diagonal[0] == diagonal[2] == jogador) and eh_posicao_livre(tuplo, posicoes['diagonal'][a - 1][1]):
                return True
            a += 1
        return False
    def Bloquear(self, jogador):
        i, a = 1, 1
        while i <= 3:
            coluna = obter_coluna(tuplo, i)
            linha = obter_linha(tuplo, i)
            if (coluna[0] == coluna[1] == jogador * -1) and eh_posicao_livre(tuplo, transformar_posicao(2, i - 1)):
                return True
            elif (coluna[1] == coluna[2] == jogador * -1) and eh_posicao_livre(tuplo, transformar_posicao(0, i - 1)):
                return True
            elif (coluna[0] == coluna[2] == jogador * -1) and eh_posicao_livre(tuplo, transformar_posicao(1, i - 1)):
                return True
            elif (linha[0] == linha[1] == jogador * -1) and eh_posicao_livre(tuplo, transformar_posicao(i - 1, 2)):
                return True
            elif (linha[1] == linha[2] == jogador * -1) and eh_posicao_livre(tuplo, transformar_posicao(i - 1, 0)):
                return True
            elif (linha[0] == linha[2] == jogador * -1) and eh_posicao_livre(tuplo, transformar_posicao(i - 1, 1)):
                return True
            i += 1
        while a <= 2:
            diagonal = obter_diagonal(tuplo, a)
            if (diagonal[0] == diagonal[1] == jogador * -1) and eh_posicao_livre(tuplo, posicoes['diagonal'][a - 1][2]):
                return True
            elif (diagonal[1] == diagonal[2] == jogador * -1) and eh_posicao_livre(tuplo, posicoes['diagonal'][a - 1][0]):
                return True
            elif (diagonal[0] == diagonal[2] == jogador * -1) and eh_posicao_livre(tuplo, posicoes['diagonal'][a - 1][1]):
                return True
            a += 1
        return False
    def Bifurcar(self, jogador):
        for i in range(len(tuplo)):
            linha = obter_linha(tuplo, i + 1)
            for a in range(len(linha)):
                coluna = obter_coluna(tuplo, a + 1)
                if (jogador in linha and jogador in coluna and eh_posicao_livre(tuplo, posicao_interesecao(i, 'linha', a, 'coluna'))):
                    return True
            for e in range(len(linha) - 1):
                diagonal = obter_diagonal(tuplo, e + 1)
                if (jogador in linha and jogador in diagonal and eh_posicao_livre(tuplo, posicao_interesecao(i, 'linha', e, 'diagonal'))):
                    return True
        return False    
    def BloquearBifurcacao(self, jogador):
        for i in range(len(tuplo)):
            linha = obter_linha(tuplo, i + 1)
            for a in range(len(linha)):
                coluna = obter_coluna(tuplo, a + 1)
                if (jogador * -1 in linha and jogador * -1 in coluna and eh_posicao_livre(tuplo, posicao_interesecao(i, 'linha', a, 'coluna'))):
                    return True
            for e in range(len(linha) - 1):
                diagonal = obter_diagonal(tuplo, e + 1)
                if (jogador * -1 in linha and jogador * -1 in diagonal and eh_posicao_livre(tuplo, posicao_interesecao(i, 'linha', e, 'diagonal'))):
                    return True
        return False  
    def Centro(self, jogador):
        return eh_posicao_livre(tuplo, transformar_posicao(1, 1))
    def CantoOposto(self, jogador):
        for i in range(1,3):
            diagonal = obter_diagonal(tuplo, i)
            if (diagonal[0] == jogador * - 1 and eh_posicao_livre(tuplo, posicoes['diagonal'][i - 1][2])):
                return True
            elif (diagonal[2] == jogador * - 1 and eh_posicao_livre(tuplo, posicoes['diagonal'][i - 1][2])):
                return True
        return False
    def CantoVazio(self, jogador):
        for i in range(1,3):
            diagonal = obter_diagonal(tuplo, i)
            for a in range(len(diagonal)):
                if a in (0,2) and i in (0,2) and eh_posicao_livre(tuplo, transformar_posicao(i, a)):
                    return True
        return False 
    def LateralVazia(self, jogador):
        for i in range(1, 4):
            coluna = obter_coluna(tuplo, i)
            for a in range(len(coluna)):
                posicao = transformar_posicao(i - 1, a)
                if posicao in (2,4,6,8) and eh_posicao_livre(tuplo, posicao):
                    return True
        return False

class Jogo: 
    """ Classe de funcoes que realiza as jogadas (INPUT -> jogador, OUTPUT -> ...) esta funcao utiliza o tabuleiro global de modo a simplificar o codigo e nao da return a valores apenas altera a variavel global de posicaoAutoEscolhida para na funcao que utliza esta classe (escolher_posicao_auto()) se poder devolver o valor da posicao escolhida """
    def Ganhar(self, jogador):
        list = []
        i, a = 1, 1
        while i <= 3:
            coluna = obter_coluna(tuplo, i)
            linha = obter_linha(tuplo, i)
            if (coluna[0] == coluna[1] == jogador) and eh_posicao_livre(tuplo, transformar_posicao(i - 1, 2)):
                list.insert(len(list), transformar_posicao(2, i - 1))
            elif (coluna[1] == coluna[2] == jogador) and eh_posicao_livre(tuplo, transformar_posicao(i - 1, 0)):
                list.insert(len(list), transformar_posicao(0, i - 1))
            elif (coluna[0] == coluna[2] == jogador) and eh_posicao_livre(tuplo, transformar_posicao(i - 1, 1)):
                list.insert(len(list), transformar_posicao(1, i - 1))
            elif (linha[0] == linha[1] == jogador) and eh_posicao_livre(tuplo, transformar_posicao(i - 1, 2)):
                list.insert(len(list), transformar_posicao(i - 1, 2))
            elif (linha[1] == linha[2] == jogador) and eh_posicao_livre(tuplo, transformar_posicao(i - 1, 0)):
                list.insert(len(list), transformar_posicao(i - 1, 0))
            elif (linha[0] == linha[2] == jogador) and eh_posicao_livre(tuplo, transformar_posicao(i - 1, 1)):
                list.insert(len(list), transformar_posicao(i - 1, 1))
            i += 1
        while a <= 2:
            diagonal = obter_diagonal(tuplo, a)
            if (diagonal[0] == diagonal[1] == jogador) and eh_posicao_livre(tuplo, posicoes['diagonal'][a - 1][2]):
                list.insert(len(list), posicoes['diagonal'][a - 1][2])
            elif (diagonal[1] == diagonal[2] == jogador) and eh_posicao_livre(tuplo, posicoes['diagonal'][a - 1][0]):
                list.insert(len(list), posicoes['diagonal'][a - 1][0])
            elif (diagonal[0] == diagonal[2] == jogador) and eh_posicao_livre(tuplo, posicoes['diagonal'][a - 1][1]):
                list.insert(len(list), posicoes['diagonal'][a - 1][1])
            a += 1
        marcar_posicao(tuplo, jogador, sorted(list)[0])
        global posicaoAutoEscolhida
        posicaoAutoEscolhida = sorted(list)[0]
    def Bloquear(self, jogador):
        list = []
        i, a = 1, 1
        while i <= 3:
            coluna = obter_coluna(tuplo, i)
            linha = obter_linha(tuplo, i)
            if (coluna[0] == coluna[1] == jogador * -1) and eh_posicao_livre(tuplo, transformar_posicao(2, i - 1)):
                list.insert(len(list), transformar_posicao(2, i - 1))
            elif (coluna[1] == coluna[2] == jogador * -1) and eh_posicao_livre(tuplo, transformar_posicao(0, i - 1)):
                list.insert(len(list), transformar_posicao(0, i - 1))
            elif (coluna[0] == coluna[2] == jogador * -1) and eh_posicao_livre(tuplo, transformar_posicao(1, i - 1)):
                list.insert(len(list), transformar_posicao(1, i - 1))
            elif (linha[0] == linha[1] == jogador * -1) and eh_posicao_livre(tuplo, transformar_posicao(i - 1, 2)):
                list.insert(len(list), transformar_posicao(i - 1, 2))
            elif (linha[1] == linha[2] == jogador * -1) and eh_posicao_livre(tuplo, transformar_posicao(i - 1, 0)):
                list.insert(len(list), transformar_posicao(i - 1, 0))
            elif (linha[0] == linha[2] == jogador * -1) and eh_posicao_livre(tuplo, transformar_posicao(i - 1, 1)):
                list.insert(len(list), transformar_posicao(i - 1, 1))
            i += 1
        while a <= 2:
            diagonal = obter_diagonal(tuplo, a)
            if (diagonal[0] == diagonal[1] == jogador * -1) and eh_posicao_livre(tuplo, posicoes['diagonal'][a - 1][2]):
                list.insert(len(list), posicoes['diagonal'][a - 1][2])
            elif (diagonal[1] == diagonal[2] == jogador * -1) and eh_posicao_livre(tuplo, posicoes['diagonal'][a - 1][0]):
                list.insert(len(list), posicoes['diagonal'][a - 1][0])
            elif (diagonal[0] == diagonal[2] == jogador * -1) and eh_posicao_livre(tuplo, posicoes['diagonal'][a - 1][1]):
                list.insert(len(list), posicoes['diagonal'][a - 1][1])
            a += 1
        marcar_posicao(tuplo, jogador, sorted(list)[0])
        global posicaoAutoEscolhida
        posicaoAutoEscolhida = sorted(list)[0]
    def Bifurcar(self, jogador):
        list = []
        for i in range(len(tuplo)):
            linha = obter_linha(tuplo, i + 1)
            for a in range(len(linha)):
                coluna = obter_coluna(tuplo, a + 1)
                if (jogador in linha and jogador in coluna and eh_posicao_livre(tuplo, posicao_interesecao(i, 'linha', a, 'coluna'))):
                    list.insert(len(list), posicao_interesecao(i, 'linha', a, 'coluna'))
            for e in range(len(linha) - 1):
                diagonal = obter_diagonal(tuplo, e + 1)
                if (jogador in linha and jogador in diagonal and eh_posicao_livre(tuplo, posicao_interesecao(i, 'linha', e, 'diagonal'))):
                    list.insert(len(list), posicao_interesecao(i, 'linha', e, 'diagonal'))
        marcar_posicao(tuplo, jogador, sorted(list)[0])
        global posicaoAutoEscolhida
        posicaoAutoEscolhida = sorted(list)[0]
    def BloquearBifurcacao(self, jogador):
        list = []
        livres = obter_posicoes_livres(tuplo)
        for i in range(len(tuplo)):
            linha = obter_linha(tuplo, i + 1)
            if (jogador * -1 in linha):
                for a in range(len(linha)):
                    coluna = obter_coluna(tuplo, a + 1)
                    linhaPosicao = posicoes['linha'][i][a]
                    if linhaPosicao in livres:
                        list.insert(len(list), linhaPosicao)
                    if (jogador * -1 in coluna):
                        for x in range(len(coluna)):
                            colunaPosicao = posicoes['coluna'][a][x]
                            if colunaPosicao in livres:
                                list.insert(len(list), colunaPosicao)
                for e in range(len(linha) - 1):
                    diagonal = obter_diagonal(tuplo, e + 1)
                    linhaPosicao = posicoes['linha'][i][e]
                    if linhaPosicao in livres:
                        list.insert(len(list), linhaPosicao)
                    if (jogador * -1 in diagonal):
                        for z in range(len(diagonal)):
                            diagonalPosicao = posicoes['diagonal'][e][z]
                            if diagonalPosicao in livres:
                                list.insert(len(list), diagonalPosicao)
        marcar_posicao(tuplo, jogador, sorted(list)[0])
        global posicaoAutoEscolhida
        posicaoAutoEscolhida = sorted(list)[0]
    def Centro(self, jogador):
        marcar_posicao(tuplo, jogador, 5)
        global posicaoAutoEscolhida
        posicaoAutoEscolhida = 5
    def CantoOposto(self, jogador):
        list = []
        for i in range(1,3):
            diagonal = obter_diagonal(tuplo, i)
            if (diagonal[0] == jogador * - 1 and eh_posicao_livre(tuplo, posicoes['diagonal'][i - 1][2])):
                list.insert(len(list), posicoes['diagonal'][i - 1][2])
            elif (diagonal[2] == jogador * - 1 and eh_posicao_livre(tuplo, posicoes['diagonal'][i - 1][2])):
                list.insert(len(list), posicoes['diagonal'][i - 1][0])
        marcar_posicao(tuplo, jogador, sorted(list)[0])
        global posicaoAutoEscolhida
        posicaoAutoEscolhida = sorted(list)[0]   
    def CantoVazio(self, jogador):
        list = []
        for i in range(1,3):
            diagonal = obter_diagonal(tuplo, i)
            for a in range(len(diagonal)):
                posicao = posicoes['diagonal'][i - 1][a]
                if a in (0,2) and eh_posicao_livre(tuplo, posicao):
                    list.insert(len(list), posicao)
        marcar_posicao(tuplo, jogador, sorted(list)[0])
        global posicaoAutoEscolhida
        posicaoAutoEscolhida = sorted(list)[0]           
    def LateralVazia(self, jogador):
        list = []
        for i in range(1, 4):
            coluna = obter_coluna(tuplo, i)
            for a in range(len(coluna)):
                posicao = transformar_posicao(i - 1, a)
                if posicao in (2,4,6,8) and eh_posicao_livre(tuplo, posicao):
                    list.insert(len(list), posicao)
        marcar_posicao(tuplo, jogador, sorted(list)[0])
        global posicaoAutoEscolhida
        posicaoAutoEscolhida = sorted(list)[0]
    
def escolher_posicao_auto(tab, numero, jogada): 
    """ Funcao que realiza a verificacao e realiza as jogadas decididas como melhores pela dificuldade do computador (INPUT - tabuleiro, numero(valor 1 ou -1), jogada('basico', 'normal' ou 'perfeito'), OUPUT -> posicao) """
    if (not eh_tabuleiro(tab) or type(tab) != tuple) or (numero not in (-1,1) or type(numero) != int) or (jogada not in ('basico', 'normal', 'perfeito') or type(jogada) != str):
        raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')
    global posicaoAutoEscolhida
    global tuplo
    tuplo = tab
    posicaoAutoEscolhida = None
    if 'vitoria' in jogadas[jogada] and Poder().Ganhar(numero):
        Jogo().Ganhar(numero)
    elif 'bloqueio' in jogadas[jogada] and Poder().Bloquear(numero):
        Jogo().Bloquear(numero)
    elif 'bifurcacao' in jogadas[jogada] and Poder().Bifurcar(numero):
        Jogo().Bifurcar(numero)
    elif 'bloqueioBifurcacao' in jogadas[jogada] and Poder().BloquearBifurcacao(numero):
        Jogo().BloquearBifurcacao(numero)
    elif 'centro' in jogadas[jogada] and Poder().Centro(numero):
        Jogo().Centro(numero)
    elif 'cantoOposto' in jogadas[jogada] and Poder().CantoOposto(numero):
        Jogo().CantoOposto(numero)
    elif 'cantoVazio' in jogadas[jogada] and Poder().CantoVazio(numero):
        Jogo().CantoVazio(numero)
    elif 'lateralVazia' in jogadas[jogada] and Poder().LateralVazia(numero):
        Jogo().LateralVazia(numero)
    return posicaoAutoEscolhida

def jogo_do_galo(simbolo, estrategia):
    """ Funcao principal do jogo que comeca o jogo e decide quem deve jogar e verifica se alguem ganhou (INPUT -> simbolo('X' ou 'O'), estrategia('basico', 'normal', 'perfeito'), OUPUT -> vencedor('X', 'O', 'EMPATE') """
    if (simbolo not in ('X', 'O') or type(simbolo) != str) or (estrategia not in ('basico','normal','perfeito') or type(estrategia) != str):
        raise ValueError('jogo_do_galo: algum dos argumentos e invalido')
    global jogador
    jogador = numero[simbolo]
    increment = 1
    if simbolo == 'X':
        increment = 2
    resultado = 0
    print('Bem-vindo ao JOGO DO GALO.')
    print("O jogador joga com '" + simbolo + "'.")
    while resultado == 0:
        if obter_posicoes_livres(tuplo) == () and jogador_ganhador(tuplo) == 0:
            break
        if increment % 2 == 0:
            marcar_posicao(tuplo, jogador, escolher_posicao_manual(tuplo))
        else:
            print('Turno do computador (' + estrategia + '):')
            escolher_posicao_auto(tuplo, jogador * -1, estrategia)
        print(tabuleiro_str(tuplo))
        increment += 1
        resultado = jogador_ganhador(tuplo)
    return vencedor[jogador_ganhador(tuplo)]