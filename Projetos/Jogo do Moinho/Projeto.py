pos_dict = {'a': 1, 'b': 2,'c': 3}

def cria_posicao(c,l):
    """
    Construtor
        :param c: str -> Valor que varia entre 'a', 'b' e 'c'
        :param l: str -> Valor que varia entre '1', '2' e '3'
        :return: posicao
    Controi uma posicao
    """
    if type(l) != str or type(c) != str or l not in ('1','2','3') or c not in ('a', 'b', 'c'):
        raise ValueError('cria_posicao: argumentos invalidos') 
    return {'linha': l, 'coluna': c}

def cria_copia_posicao(p):
    """
    Construtor
        :param p: posicao
        :return: posicao
    Recebe uma posicao e cria uma copia da mesma
    """
    return p

def obter_pos_c(p):
    """
    Seletor
        :param p: posicao
        :return: str -> Valor que varia entre 'a', 'b' e 'c' 
    Recebe uma posicao e devolve a coluna a que esta pertence
    """
    return p['coluna']

def obter_pos_l(p):
    """
    Seletor
        :param p: posicao
        :return: str -> Valor que varia entre '1', '2' e '3'
    Recebe uma posicao e devolve a linha a que esta pertence
    """
    return p['linha']

def eh_posicao(p):
    """
    Reconhecedor
        :param p: posicao
        :return: bool
    Recebe um dicionario e verifica se este e uma posicao
    """
    return type(p) == dict and len(p) == 2 and type(obter_pos_c(p)) == str and obter_pos_c(p) in ('a', 'b', 'c') and type(obter_pos_l(p)) == str and obter_pos_l(p) in ('1','2','3')

def posicoes_iguais(p, p2):
    """
    Teste
        :param p: posicao
        :param p2: posicao
        :return: bool
    Recebe duas posicoes e verifica se estas sao identicas
    """
    if obter_pos_c(p) == obter_pos_c(p2) and obter_pos_l(p) == obter_pos_l(p2) and eh_posicao(p) and eh_posicao(p2):
        return True
    return False

def posicao_para_str(p):
    """
    Transformador
        :param p: posicao
        :return: str
    Recebe uma posicao e devolve em string do seguinto modo -> 'a1'
    """
    return '{}{}'.format(obter_pos_c(p), obter_pos_l(p))

def coluna_index(soma):
    """
    Auxiliar
        :param soma: int -> Valor que varia entre 1, 2 e 3
        :return: str -> Valor que varia entre 'a', 'b' e 'c'
    Recebe um inteiro entre 1 e 3 e devolve a letra equivalente por ordem alfabetica
    """
    return [k for k, v in pos_dict.items() if v == soma][0]

def organizar_lista_posicoes(l):
    """
    Auxiliar
        :param: l: list -> Lista de posicoes
        :return: list -> Lista de posicoes organizada
    Recebe uma lista de posicoes e a organiza em torno da linha e depois da coluna
    """
    l = sorted(l, key = lambda k: k['linha'])
    for i in range(1,len(l)):
        if l[i]['linha'] == l[i - 1]['linha'] and pos_dict[l[i]['coluna']] < pos_dict[l[i - 1]['coluna']]:
            l[i], l[i - 1] = l[i - 1], l[i]
    return l

def obter_posicoes_adjacentes(p):
    """
    Funcao de Alto Nivel
        :param: p: posicao
        :return: tuple -> Tuplo de posicoes adjacentes
    Recebe uma posicao e devolve as posicoes adjacentes a esta
    """
    l = []
    coluna = obter_pos_c(p)
    linha = int(obter_pos_l(p))
    posicoes = (cria_posicao('a', '1'), cria_posicao('a', '3'), cria_posicao('c', '1'), cria_posicao('c', '3'), cria_posicao('b', '2'))
    def adjacentes_coluna(p):
        for i in (-1,1):
            soma = pos_dict[coluna] + i
            if soma in (1,2,3):
                l.append(cria_posicao(coluna_index(soma), str(linha)))
    def adjacentes_linha(p):
        for i in (-1,1):
            soma = linha + i
            if soma in (1,2,3):
                l.append(cria_posicao(coluna, str(soma)))
    def adjacentes_diagonal(p):
        for i in (-1, 1):
            soma = linha + i
            for a in (-1, 1):
                soma2 = pos_dict[coluna] + a
                if soma in (1,2,3) and soma2 in (1,2,3):
                    l.append(cria_posicao(coluna_index(soma2), str(soma)))
    adjacentes_coluna(p)
    adjacentes_linha(p)
    if p in posicoes:
        adjacentes_diagonal(p)
    return tuple(organizar_lista_posicoes(l))

peca_dict = {'X': 1, ' ': 0, 'O': -1}

def cria_peca(p):
    """
    Construtor
        :param: p: str -> Valor que varia entre 'X', 'O' e ' ' 
        :return: str
    Recebe uma string e cria a sua peca
    """
    if type(p) != str or p not in ('X', 'O', ' '):
        raise ValueError('cria_peca: argumento invalido')
    return p

def cria_copia_peca(p):
    """
    Construtor
        :param: p: peca
        :return: str
    Recebe uma peca e cria a sua copia
    """
    return p

def eh_peca(p):
    """
    Reconhecedor
        :param: p: peca
        :return: bool
    Recebe uma str e verifica se e uma peca
    """
    return type(p) == str and p in ('X', 'O', ' ')

def pecas_iguais(p, p2):
    """
    Teste
        :param: p: peca
        :param: p2: peca
        :return: bool
    Recebe duas pecas e verifica se estas sao iguais
    """
    return p == p2

def peca_para_str(p):
    """
    Transformador
        :param: p: peca
        :return: str
    Recebe uma peca e formata-la
    """
    return '[{}]'.format(p)

def peca_para_inteiro(p):
    """
    Funcao de alto nivel
        :param: p: peca
        :return: int -> Valor que varia entre '1', '-1' e '0' 
    Recebe uma peca e devolve o inteiro que a identifica
    """
    return peca_dict[p]

def cria_tabuleiro():
    """
    Construtor
        :return: list
    Funcao que cria um tabuleiro vazio
    """
    return [list([' '] * 3) for i in range(3)]

def cria_copia_tabuleiro(tab):
    """
    Construtor
        :param: tab: tabuleiro
        :return: list
    Recebe um tabuleiro e cria a sua copia
    """
    if eh_tabuleiro(tab):
        return tab
    return

def obter_peca(tab, p):
    """
    Seletor
        :param: tab: tabuleiro
        :param: p: posicao
        :return: peca
    Recebe um tabuleiro e uma posicao e devolve a peca presente nessa posicao
    """
    return tab[int(obter_pos_l(p)) - 1][pos_dict[obter_pos_c(p)] - 1]

def obter_coluna(tab, i):
    """
    Auxiliar
        :param: tab: tabuleiro
        :param: i: int
        :return: list
    Recebe um tabuleiro e um indice e devolve a coluna que apresenta esse indice
    """
    l = []
    for a in range(len(tab)):
        l.append(tab[a][i - 1])
    return l  

def obter_vetor(tab, v):
    """
    Seletor
        :param: tab: tabuleiro
        :param: v: str -> Valor que varia entre '1', '2', '3', 'a', 'b' e 'c'
        :return: list
    Recebe uma string e devolve a coluna ou linha que esta identifica
    """
    if eh_tabuleiro(tab) and type(v) == str and v in ('1','2','3','a','b','c'):
        if v.isdigit():
            return tab[int(v) - 1]
        else:
            return obter_coluna(tab, pos_dict[v])

def coloca_peca(tab, peca, p):
    """
    Modificador
        :param: tab: tabuleiro
        :param: peca: peca
        :param: p: posicao
        :return: tabuleiro
    Recebe um tabuleiro, uma peca e uma posicao e coloca essa peca na posicao recebida e devolve o tabuleiro editado
    """
    tab[int(obter_pos_l(p)) - 1][pos_dict[obter_pos_c(p)] - 1] = peca
    return tab

def remove_peca(tab, p):
    """
    Modificador
        :param: tab: tabuleiro
        :param: p: posicao
        :return: tabuleiro
    Recebe um tabuleiro e uma posicao e remove essa peca na posicao recebida e devolve o tabuleiro editado
    """
    coloca_peca(tab, cria_peca(' '), p)
    return tab

def move_peca(tab, p, p2):
    """
    Modificador
        :param: tab: tabuleiro
        :param: peca: peca
        :param: p: posicao
        :param: p2: posicao
        :return: tabuleiro
    Recebe um tabuleiro, uma peca e uma posicao e move essa peca na posicao recebida 'p' para a posicao recebida 'p2' e devolve o tabuleiro editado
    """
    tabNovo = coloca_peca(tab, obter_peca(tab, p), p2)
    return remove_peca(tabNovo, p)

def eh_tabuleiro(tab):
    """
    Reconhecedor
        :param: tab: tabuleiro
        :return: bool
    Recebe um tabuleiro e verifica se este de facto e um tabuleiro
    """
    if type(tab) == list and len(tab) == 3:
        for i in range(len(tab)):
            if type(tab[i]) == list and len(tab[i]) == 3:
                for a in range(len(tab[i])):
                    if not eh_peca(tab[i][a]):
                        return False
            else:
                return False
    else:
        return False
    return True

def eh_posicao_livre(tab, p):
    """
    Reconhecedor
        :param: tab: tabuleiro
        :param: p: posicao
        :return: bool
    Recebe um tabuleiro e uma posicao e verifica se esta posicao esta livre
    """
    return tab[int(obter_pos_l(p)) - 1][pos_dict[obter_pos_c(p)] - 1] == cria_peca(' ')

def tabuleiros_iguais(tab, tab2):
    """
    Teste
        :param: tab: tabuleiro
        :param: tab2: tabuleiro
        :return: bool
    Recebe dois tabuleiros e verifica se estes sao iguais
    """
    if not eh_tabuleiro(tab) or not eh_tabuleiro(tab2):
        return False
    for i in range(len(tab)):
        for a in range(len(tab[i])):
            if tab[i][a] != tab2[i][a]:
                return False
    return True

def tabuleiro_para_str(tab):
    """
    Transfomador
        :param: tab: tabuleiro
        :return: str
    Recebe um tabuleiro e retorna a string que representa o tabuleiro
    """
    return '   a   b   c\n1 [{0}]-[{1}]-[{2}]\n   | \\ | / |\n2 [{3}]-[{4}]-[{5}]\n   | / | \\ |\n3 [{6}]-[{7}]-[{8}]'.format(*tab[0], *tab[1], *tab[2])

def tuplo_para_tabuleiro(tuplo):
    """
    Transformador
        :param: tuplo: tuple
        :return: list
    Recebe um tuplo e coloca este na formatacao correta do tabuleiro criada em cria_tabuleiro()
    """
    l = list(tuplo)
    for i in range(len(l)):
        l[i] = list(tuplo[i])
        for a in range(len(l[i])):
            l[i][a] = [k for k, v in peca_dict.items() if v == tuplo[i][a]][0]
    return l

def obter_ganhador(tab):
    """
    Funcao de alto nivel
        :param: tab: tabuleiro
        :return: str
    Recebe um tabuleiro e verifica se alguem ganhou o jogo. Se sim devolve a sua peca
    """
    for i in range(3):
        coluna = obter_coluna(tab, i + 1)
        linha = tab[i]
        if len(set(coluna)) == 1:
            return coluna[0]
        elif len(set(linha)) == 1:
            return linha[0]
    return ' '

def obter_posicoes_livres(tab):
    """
    Funcao de alto nivel
        :param: tab: tabuleiro
        :return: tuple
    Recebe um tabuleiro e devolve um tuplo com as posicoes ainda livres
    """
    t = ()
    for i in range(len(tab)):
        for a in range(len(tab[i])):
            p = cria_posicao(coluna_index(a + 1), str(i + 1))
            if eh_posicao_livre(tab, p):
                t += (p,)
    return t

def obter_posicoes_jogador(tab, peca):
    """
    Funcao de alto nivel
        :param: tab: tabuleiro
        :param: peca: peca
        :return: tuple
    Recebe um tabuleiro e uma peca e devolve um tuplo com as posicoes ocupadas por esta peca
    """
    t = ()
    for i in range(len(tab)):
        for a in range(len(tab[i])):
            p = cria_posicao(coluna_index(a + 1), str(i + 1))
            if tab[int(obter_pos_l(p)) - 1][pos_dict[obter_pos_c(p)] - 1] == peca:
                t += (p,)
    return t

def outro_jogador(peca):
    """
    Auxiliar
        :param: peca: peca
        :return: str
    Recebe uma peca e devolve a peca a ser utilizada pelo jogador adversario
    """
    return [k for k, v in peca_dict.items() if v == peca_dict[peca] * -1][0]

def minimax(tab, peca, profundidade, seq_movs):
    """
    Algoritmo
        :param: tab: tabuleiro
        :param: peca: peca
        :param: profundidade: int
        :param: seq_movs: tuple
        :return: str, tuple
    Recebe um tabuleiro, uma peca, um inteiro e um tuplo e devolve as melhores jogadas possiveis a fazer com uma certa profundidade
    """
    adversario = cria_peca('X') if peca_para_inteiro(peca) == -1 else cria_peca('O')
    if peca_para_str(obter_ganhador(tab)) != '[ ]' or profundidade == 0:
        return peca_para_inteiro(obter_ganhador(tab)), seq_movs
    else:
        melhor_resultado, melhor_seq_movs = peca_para_inteiro(peca) * -1, ()
        for i in obter_posicoes_jogador(tab, peca):
            for a in obter_posicoes_adjacentes(i):
                if eh_posicao_livre(tab, a):
                    newtab = move_peca(cria_copia_tabuleiro(tab), i, a)
                    newres, newsecmov = minimax(newtab, adversario, profundidade - 1, seq_movs + (posicao_para_str(i) + posicao_para_str(a),))
                    if not melhor_seq_movs or (peca == cria_peca('X') and newres > melhor_resultado) or (peca == cria_peca('O') and newres < melhor_resultado):
                        melhor_resultado, melhor_seq_movs = newres, newsecmov
        return melhor_resultado, melhor_seq_movs
    
def obter_movimento_manual(tab, peca):
    """
    Funcao Adicional
        :param: tab: tabuleiro
        :param: peca: peca
        :return: dict
    Recebe um tabuleiro e uma peca e devolve a posicao em que o jogador ira colocar a peca ou movimentar a peca
    """
    if len(obter_posicoes_jogador(tab, peca)) == 3:
        pInput = input('Turno do jogador. Escolha um movimento: ')
        if len(pInput) != 4:
            raise ValueError('obter_movimento_manual: escolha invalida')
        pOld = cria_posicao(pInput[0], pInput[1])
        p = cria_posicao(pInput[2], pInput[3])
    else:
        pInput = input('Turno do jogador. Escolha uma posicao: ')
        if len(pInput) != 2:
            raise ValueError('obter_movimento_manual: escolha invalida')
        p = cria_posicao(pInput[0], pInput[1])
    if 'pOld' in locals():
        if pOld != p:
            if not eh_posicao(pOld) or p not in obter_posicoes_adjacentes(pOld) or pOld in obter_posicoes_jogador(tab, outro_jogador(peca)):
                raise ValueError('obter_movimento_manual: escolha invalida')
    else:
        if not eh_posicao(p) or not eh_posicao_livre(tab, p):
            raise ValueError('obter_movimento_manual: escolha invalida')
    if 'pOld' in locals():
        return (pOld, p)
    return (p,)

def obter_movimento_auto(tab, peca, dificuldade):
    """
    Funcao Adicional
        :param: tab: tabuleiro
        :param: peca: peca
        :param: dificuldade: str
        :return: dict
    Recebe um tabuleiro, uma peca, dificuldade e devolve a posicao em que o computador ira colocar a peca ou movimentar a peca de acordo com o algoritmo utilizado (minimax) que calcula as melhores jogadas possiveis dependendo da dificuldade
    """
    pJogador = obter_posicoes_jogador(tab, peca)
    p = None
    if len(pJogador) == 3:
        pOld = None
        if dificuldade == 'facil':
            p = []
            for x in pJogador:
                pOld = x
                for a in obter_posicoes_adjacentes(x):
                    if eh_posicao_livre(tab, a):
                        p.append(a)
                if len(p) != 0:
                    p = p[0]
                    break
            if type(p) != dict:
                pOld = pJogador[0]
                p = pOld 
        elif dificuldade == 'normal':
            jogada = minimax(tab, peca, 1, ())
            pOld = cria_posicao(jogada[1][0][0], jogada[1][0][1])
            p = cria_posicao(jogada[1][0][2], jogada[1][0][3])
        else:
            jogada = minimax(tab, peca, 5, ())
            pOld = cria_posicao(jogada[1][0][0], jogada[1][0][1])
            p = cria_posicao(jogada[1][0][2], jogada[1][0][3])
        return (pOld, p)
    p = melhor_colocacao(tab, peca)
    return (p,)

def melhor_colocacao(tab, peca):
    """
    Auxiliar
        :param: tab: tabuleiro
        :param: peca: peca
        :return: p
    Recebe um tabuleiro e uma peca e devolve a posicao em que o computador deveria colocar a peca de acordo com as estrategias
    """
    def vitoria(tab, peca, tipo, jogada):
        res = None
        peca = cria_copia_peca(peca)
        if jogada == 'bloqueio':
            peca = outro_jogador(peca)
        for i in range(3):
            coluna = obter_coluna(tab, i + 1)
            linha = tab[i]
            sColuna = set(coluna)
            sLinha = set(linha)
            if len(sColuna) == 2 and set((peca, ' ')) == sColuna and coluna.count(peca) == 2:
                res, tipo, index = coluna, 'coluna', i+1
            elif len(sLinha) == 2 and set((peca, ' ')) == sLinha and linha.count(peca) == 2:
                res, tipo, index = linha, 'linha', i+1
        if type(res) == list and tipo == 'verificacao':
            res = True
        elif tipo == 'verificacao':
            res = False
        else:
            for i in range(len(res)):
                if res[i] == ' ':
                    if tipo == 'coluna':
                        res = cria_posicao(coluna_index(index), str(i + 1))
                        break
                    else:
                        res = cria_posicao(coluna_index(i + 1), str(index))
                        break
        return res
    def centro(tab, peca, tipo):
        p = cria_posicao('b', '2')
        if tipo == 'verificacao':
            return eh_posicao_livre(tab, p)
        else:
            return p
        res = None
        return res
    def cantoVazio(tab, peca, tipo):
        res = None
        l = []
        for i in range(len(tab)):
            for a in range(len(tab[i])):
                if a % 2 == 0 and tab[i][a] == ' ' and i != 1:
                    res.append(cria_posicao(coluna_index(a + 1), str(i + 1)))
        if len(l) > 0:
            l = organizar_lista_posicoes(l)
            if tipo == 'verificacao':
                res = True
            else:
                res = l[0]
        elif tipo == 'verificacao':
            res = False
        return res
    def lateralVazia(tab, peca, tipo):
        res = None
        posicoes = (cria_posicao('b', '1'), cria_posicao('a', '2'), cria_posicao('c', '2'), cria_posicao('b', '3'))
        l = []
        for i in range(tab):
            for a in range(tab[i]):
                p = cria_posicao(coluna_index(a + 1), str(i + 1))
                if p in posicoes and tab[i][a] == ' ':
                    l.append(p)
        if len(l) > 0:
            l = organizar_lista_posicoes(l)
            if tipo == 'verificacao':
                res = True
            else:
                res = l[0]
        elif tipo == 'verificacao':
            res = False
        return res
    if vitoria(tab, peca, 'verificacao', ' '):
        p = vitoria(tab, peca, ' ', ' ')
    elif vitoria(tab, peca, 'verificacao', 'bloqueio'):
        p = vitoria(tab, peca, ' ', 'bloqueio')
    elif centro(tab, peca, 'verificacao'):
        p = centro(tab, peca, ' ')
    elif cantoVazio(tab, peca, 'verificacao'):
        p = cantoVazio(tab, peca, ' ')
    elif lateralVazia(tab, peca, 'verificacao'):
        p = lateralVazia(tab, peca, ' ')
    return p

def moinho(pecaStr, dificuldade):
    """
    Funcao Adicional
        :param: pecaStr: peca
        :param: dificuldade: str
        :return: str
    Funcao principal do jogo. Recebe uma peca e uma dificuldade e organiza o jogo decidindo quem deveria ser o proximo a jogar e quando o jogo acaba este retorna a string da peca do vencedor
    """
    if type(pecaStr) != str or not eh_peca(pecaStr[1]) or type(dificuldade) != str or dificuldade not in ('facil', 'normal', 'dificil'):
        raise ValueError('moinho: argumentos invalidos')
    print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade {}.'.format(dificuldade))
    peca = pecaStr[1]
    resultado = ' '
    increment = 0
    if peca == 'O':
        increment += 1
    tab = cria_tabuleiro()
    print(tabuleiro_para_str(tab))
    while resultado == ' ':
        if increment % 2 == 0:
            p = obter_movimento_manual(tab, peca)
            if len(p) == 2:
                if p[0] != p[1]:
                    tab = move_peca(tab, p[0], p[1])
            else:
                tab = coloca_peca(tab, peca, p[0])
        else:
            print('Turno do computador ({}):'.format(dificuldade))
            p = obter_movimento_auto(tab, outro_jogador(peca), dificuldade)
            if len(p) == 2:
                tab = move_peca(tab, p[0], p[1])
            else:
                tab = coloca_peca(tab, outro_jogador(peca), p[0])
        print(tabuleiro_para_str(tab))
        increment += 1
        resultado = obter_ganhador(tab)
    return peca_para_str(resultado)