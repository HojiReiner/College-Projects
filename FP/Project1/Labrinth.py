#Rodrigo Afonso Rato Goncalves    95665

#2.1.1(eh_labirinto)------------------------------------------------------------
def eh_labirinto (labirinto):
    """Funcao que recebe um argumento de qualquer tipo e devolve True se o 
    seu argumento corresponde a um labirinto e False caso contrario"""
    
#Verifica se o argumento e um tuplo 
    if type(labirinto) is not tuple: 
        return False
    
#Verifica o comprimento Nx do labirinto
    if len(labirinto) < 3:
        return False

#Avalia se as colunas sao tuplos, verifica o seu comprimento, e se so sao 
#compostas por inteiros(0 e 1)
    for colunas_lab in labirinto:
        if type(colunas_lab) is not tuple:
            return False
        elif len(colunas_lab) != len(labirinto[0]) or len(colunas_lab) < 3:
            return False
        
        for elementos in colunas_lab:
            if type(elementos) is not int:
                return False
            elif elementos != 1 and elementos != 0:
                return False

#Verifica se a primeira e ultima coluna sao paredes completas
    if 0 in labirinto[0] or 0 in labirinto[len(labirinto)-1] :
        return False

#Verifica se as colunas interiores tem 1 na ponta
    for colunas_int in labirinto[1:len(labirinto)-1]:
        if colunas_int[0] !=1 or colunas_int[len(labirinto[0])-1] !=1:
            return False           

    return True

#2.1.2(eh_posicao)--------------------------------------------------------------
def eh_posicao(posicao):
    """ Funcao que recebe um argumento de qualquer tipo e devolve True se o 
    seu argumento corresponde a uma posicao e False caso contrario"""
    
#Verifica se o argumento e um tuplo
    if type(posicao) is not tuple:
        return False
    
#Verifica se o argumento so tem 2 elementos
    elif len(posicao) != 2:
        return False
    
#Verifica se os elementos sao inteiros nao negativos    
    for e in posicao:
        if type(e) is not int:
            return False
        elif e < 0:
            return False
    
    return True

#2.1.3(eh_conj_posicoes)--------------------------------------------------------
def eh_conj_posicoes(conj_posicoes):
    """Funcao que recebe um argumento de qualquer tipo e devolve True se o seu 
    argumento corresponde a um conjunto de posicoes unicas e False caso 
    contrario """
    
#Verifica se o argumento e um tuplo
    if type(conj_posicoes) is not tuple:
        return False    
    
    for posicoes in conj_posicoes:
#Verifica se sao posicoes
        if not eh_posicao(posicoes):
            return False
#Verifica se nao ha posicoes repetidas
        if conj_posicoes.count(posicoes) != 1:
            return False
    
    return True

#2.1.4(tamanho_labirinto)-------------------------------------------------------
def tamanho_labirinto (labirinto):
    """Funcao que recebe um labirinto e devolve um tuplo de dois valores
    inteiros correspondendo o primeiro deles a dimensao Nx e o segundo 
    a dimensao Ny do labirinto"""
    
    if not eh_labirinto(labirinto):
        raise ValueError('tamanho_labirinto: argumento invalido')
    
    Nx = len(labirinto)
    Ny = len(labirinto[0])
    
    return (Nx,Ny)

#2.1.5(eh_mapa_valido)----------------------------------------------------------
def eh_mapa_valido (labirinto, conj_posicoes):
    """Funcao que recebe um labirinto e um conjunto de posicoes correspondente 
    as unidades presentes no labirinto, e devolve True se o segundo argumento
    corresponde a um conjunto de posicoes compativeis (nao ocupadas por paredes) 
    dentro do labirinto e False caso contrario"""
    
#Verifica se o labirinto e o conjunto de posicoes sao validos
    if not eh_labirinto(labirinto) or not eh_conj_posicoes(conj_posicoes):
        raise ValueError('eh_mapa_valido: algum dos argumentos e invalido')
#Poe numa variavel o tuplo correspondente ao tamanho do labirinto
    Nx_Ny = tamanho_labirinto(labirinto)

#Verifica se os valores das posicoes e valido
    for posicoes in conj_posicoes:

#Verifica se a posicao se encontra dentro do labirinto
        if posicoes[0] > Nx_Ny[0]:
            return False
        elif posicoes[1] > Nx_Ny[1]:
            return False
        
#Verifica se as posicoes nao calham em paredes
        elif labirinto[posicoes[0]][posicoes[1]] == 1:
            return False
    
    return True

#2.1.6(eh_posicao_livre)--------------------------------------------------------
def eh_posicao_livre (labirinto,conj_posicoes,posicao):
    """Funcao que recebe um labirinto, um conjunto de posicoes correspondente a
    unidades presentes no labirinto e uma posicao, e devolve True se a posicao
    corresponde a uma posicao livre (nao ocupada nem por paredes, nem por
    unidades) dentro do labirinto e False caso contrario """

#Verifica se e labirinto e um mapa valido e se as unidades se encontram numa
#posicao nao ocupada por paredes
    try:
        eh_mapa_valido(labirinto,conj_posicoes)
    except:
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    
    if not eh_mapa_valido(labirinto,conj_posicoes):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    
    
#Verifica se e uma posicao valida
    if not eh_posicao(posicao):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')

    Nx_Ny = tamanho_labirinto (labirinto)
#Verifica se a posicao nao coincide com unidade ou paredes, e esta dentro do 
#labirinto

    if posicao in conj_posicoes:
        return False
    elif posicao[0] > Nx_Ny[0] or posicao[1] > Nx_Ny[1]:
        return False
    elif labirinto[posicao[0]][posicao[1]] == 1:
        return False
    
    return True

#2.1.7(posicoes_adjacentes)-----------------------------------------------------
def posicoes_adjacentes(posicao):
    """Funcao que recebe uma posicao e devolve o conjunto de posicoes adjacentes
    da posicao em ordem de leitura de um labirinto."""
    
#Verifica se o argumento e uma posicao valida
    if not eh_posicao(posicao):
        raise ValueError('posicoes_adjacentes: argumento invalido')
   
#Encontra as posicoes adjacentes 
    posicao_adj1 = (posicao[0],posicao[1]-1)
    posicao_adj2 = (posicao[0]-1,posicao[1])
    posicao_adj3 = (posicao[0]+1,posicao[1])
    posicao_adj4 = (posicao[0],posicao[1]+1)
    
#Verifica se as posicoes adjacentes sao validas
    posicoes_adj =(posicao_adj1,posicao_adj2,posicao_adj3,posicao_adj4)
    posicoes_adj_filtradas = ()
    for posicao_adj in posicoes_adj:
        if eh_posicao(posicao_adj):
            posicoes_adj_filtradas = posicoes_adj_filtradas + ((posicao_adj),)
    
    return (posicoes_adj_filtradas)

#2.1.8(mapa_str)----------------------------------------------------------------
def mapa_str(labirinto,conj_posicoes):
    """Funcao que recebe um labirinto e um conjunto de posicoes correspondente
    as unidades presentes no labirinto e devolve a cadeia de caracteres que as 
    representa"""

#Verificar se e um mapa valido
    try:
        eh_mapa_valido(labirinto,conj_posicoes)
    except:
        raise ValueError('mapa_str: algum dos argumentos e invalido')
    if not eh_mapa_valido(labirinto,conj_posicoes):
        raise ValueError('mapa_str: algum dos argumentos e invalido')
    
#Transforma os tuplos em cadeias de caracteres com (#)paredes, (.)corredores
#e (0)unidade
    representacao = ''
#Mete as paredes e os corredores
    for linha in range(len(labirinto[0])):
        for coluna in range(len(labirinto)):
            if labirinto[coluna][linha] == 1:
                representacao += '#'
            else:
                representacao += '.'

#Mete as unidades no labirinto
            for unidade in conj_posicoes:
                if unidade[0] == coluna and unidade[1] ==linha :
                    representacao = representacao[:len(representacao)-1]
                    representacao += 'O'
        
        representacao += '\n'

    return representacao[:len(representacao)-1]

#2.2.1(obter_objetivos)---------------------------------------------------------
def obter_objetivos(labirinto,conj_posicoes,posicao):
    """Funcao que recebe um labirinto, um conjunto de posicoes correspondente as
    unidades presentes no labirinto e uma posicao correspondente a uma das
    unidades, e devolve o conjunto de posicoes (em qualquer ordem)  nao ocupadas
    dentro do labirinto correspondente a todos os possiveis objetivos da unidade
    correspondente a posicao dada. """

#Verifica se o labirinto e o conjunto de posicoes constituem um mapa valido,e
#a posicao pertence ao conjunto de posicoes
    try:
        valido(labirinto,conj_posicoes,posicao)
    except:
        raise ValueError('obter_objetivos: algum dos argumentos e invalido')
    
#Da as posicoes adjacentes da ou das unidades diferentes daquela que foi chamada
#Verificando se as posicoes adjacentes nao sao repetidas
    posicoes_objetivo = ()
    
    for posicoes in conj_posicoes:
        if posicoes != posicao:
            posi_adjacentes = posicoes_adjacentes(posicoes)
            for posi in posi_adjacentes:
                if eh_posicao_livre(labirinto,conj_posicoes,posi):
                    if posi not in posicoes_objetivo:
                        posicoes_objetivo += (posi,)
    
    return posicoes_objetivo


#2.2.2(obter_caminho)-----------------------------------------------------------
def obter_caminho(labirinto,conj_posicoes,posicao):
    """Funcao que recebe um labirinto, um conjunto de posicoes correspondente
    as unidades presentes no labirinto, e uma posicao correspondente a uma das 
    unidadese devolve um conjunto de posicoes (potencialmente vazio caso nao 
    exista nenhuma unidade alcancavel) correspondente  ao  caminho  de  numero  
    minimo  de  passos  desde  a  posicao dada ate a posicao objetivo (ou seja, 
    a posicao mais proxima de acordo com a ordem de leitura do labirinto que se 
    encontra ao numero minimo de passos) """
  
#Verifica se o labirinto e o conjunto de posicoes constituem um mapa valido,e
#a posicao pertence ao conjunto de posicoes
    try:
        valido(labirinto,conj_posicoes,posicao)
    except:
        raise ValueError('obter_caminho: algum dos argumentos e invalido')
    
#Algoritmo de Lee
    fila_exploracao = [[posicao,()],]
    objetivos = obter_objetivos(labirinto,conj_posicoes,posicao)
    while fila_exploracao != []:
        posicao_atual = fila_exploracao[0][0]
        caminho_atual = fila_exploracao[0][1]
        if posicao_atual not in caminho_atual:
            if posicao_atual in objetivos:
                resultado = caminho_atual + (posicao_atual,)
                return resultado
            else:
                for posicao_possivel in posicoes_adjacentes(posicao_atual):
                    if eh_posicao_livre(labirinto,conj_posicoes,\
                                        posicao_possivel):
                        
                        fila_exploracao += [[posicao_possivel, caminho_atual +\
                                             (posicao_atual,)]]

        fila_exploracao = fila_exploracao[1:]

    return ()

#2.2.3(mover_unidade)-----------------------------------------------------------
def mover_unidade(labirinto,conj_posicoes,posicao):
    """Funcao que recebe um labirinto, um conjunto de posicoes correspondente as
    unidades presentes no labirinto, e uma posicao correspondente a uma das 
    unidades, e devolve o conjunto de posicoes  atualizado  correspondente  as 
    unidades presentes no labirinto apos a unidade dada ter realizado um unico 
    movimento"""
    
#Verifica se o labirinto e o conjunto de posicoes constituem um mapa valido,e
#a posicao pertence ao conjunto de posicoes
    try:
        valido(labirinto,conj_posicoes,posicao)
    except:
        raise ValueError('mover_unidade: algum dos argumentos e invalido')   
    

    caminho = obter_caminho(labirinto,conj_posicoes,posicao)
    novo_conjunto = ()
    for i in range(len(conj_posicoes)):
#Verifica se e possivel mover as unidades
        if caminho == ():
            return conj_posicoes
#Verificar as unidades estao lado a lado
        elif posicao in posicoes_adjacentes(conj_posicoes[i]):
            return conj_posicoes
        
#Atualizar as posicoes das unidades mantendo a ordem de leitura
        elif conj_posicoes.index(posicao) == i:
            novo_conjunto += (caminho[1],)
        else:
            novo_conjunto += (conj_posicoes[i],)
           
    return novo_conjunto 
    
#Funcoes auxiliares-------------------------------------------------------------
def valido(labirinto,conj_posicoes,posicao):
    try:
        eh_mapa_valido(labirinto,conj_posicoes)
    except:
        raise ValueError
    if not eh_mapa_valido(labirinto,conj_posicoes):
        raise ValueError      
    elif not eh_posicao(posicao):
        raise ValueError
    elif posicao not in conj_posicoes:
        raise ValueError
    return 
