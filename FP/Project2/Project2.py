#Rodrigo Afonso Rato Goncalves 95665

#Posicao========================================================================
#Construtores-------------------------------------------------------------------

def cria_posicao(x,y):
 '''
 Recebe valores correspondentes as coordenadas de uma posicao e devolve a posi-
 cao correspondente.
 '''
 
 #Requisitos para criar posicao
 if isinstance(x,int)\
    and isinstance(y,int)\
    and x >= 0\
    and y >= 0:
  return {'x':x,'y':y}
 
 else:
  raise ValueError('cria_posicao: argumentos invalidos')

 return



def cria_copia_posicao(p):
 '''
 Recebe uma posicao e devolve uma copia dela.
 '''
 return p.copy()

#Seletores----------------------------------------------------------------------

def obter_pos_x(p):
 '''
 Recebe uma posicao e devolve a sua ordenada.
 '''
 return p['x']



def obter_pos_y(p):
 '''
 Recebe uma posicao e devolve a sua ordenada.
 '''
 return p['y']

#Reconhecedores-----------------------------------------------------------------

def eh_posicao(arg):
 '''
 Recebe um argumento e devolve True se este apresentar o formato definido para
 as posicoes.
 '''
 #Requisitos para o argumento ser considerado uma posicao na forma definida
 if isinstance(arg,dict)\
    and len(arg) == 2\
    and 'x' in arg\
    and 'y' in arg\
    and isinstance(arg['x'],int)\
    and isinstance(arg['y'],int)\
    and arg['x'] > 0\
    and arg['y'] > 0:
  return True

 return False
 
#Testes-------------------------------------------------------------------------

def posicoes_iguais(p1,p2):
 '''
 Recebe duas posicoes e devolve True se forem iguais.
 '''
 if p1 == p2:
  return True
 
 return False
 

 
#Transformadores----------------------------------------------------------------

def posicao_para_str(p):
 '''
 Recebe um posicao e devolve a cadeia de caracteres '(x,y)'.
 '''
 p_tup = (obter_pos_x(p),obter_pos_y(p))
 return str(p_tup)

#Funcoes de alto nivel----------------------------------------------------------

def obter_posicoes_adjacentes(p):
 
 '''
 Recebe uma posicao e devolve as posicoes adjacentes a esta de acordo com a
 ordem de leitura do labirinto.
 '''
 
 #Criar as 4 posicoes adjacentes
 p_adj1 = (obter_pos_x(p),obter_pos_y(p) - 1)
 p_adj2 = (obter_pos_x(p) - 1,obter_pos_y(p))
 p_adj3 = (obter_pos_x(p) + 1,obter_pos_y(p))
 p_adj4 = (obter_pos_x(p),obter_pos_y(p) + 1)
 
 #Juntar num tuplo as posicoes adjacentes
 p_adjs = (p_adj1 ,p_adj2 ,p_adj3 ,p_adj4)
 p_adjs_filt = ()

 for ps in p_adjs:
  
  #Verifica se as posicoes nao tem valores negativos
  if ps[0] >= 0 and ps[1] >= 0:
   p_adjs_filt += (cria_posicao(ps[0],ps[1]),)
 
 return p_adjs_filt


#Unidade========================================================================
#Construtores-------------------------------------------------------------------

def cria_unidade(p,hp,strg,exer):
 '''
 Recebe uma posicao, dois valores inteiros maiores do que zero correspondentes
 a vida e forca da unidade,e uma cadeia de caracteres nao vazia correspondente
 ao exercito da unidade e devolve a unidade correspondente.
 '''
 
 #Requisitos para criar uma unidade
 if eh_posicao(p)\
    and isinstance(hp,int)\
    and hp > 0\
    and isinstance(strg,int)\
    and strg > 0\
    and isinstance(exer,str)\
    and len(exer.strip()) > 0:
  return {'p':p , 'hp':hp, 'strg':strg , 'exer':exer.strip()}
 
 else:
  raise ValueError('cria_unidade: argumentos invalidos')
 
 return
 


def cria_copia_unidade(u):
 '''
 Recebe uma unidade e devolve uma copia desta.
 '''
 #Copiar a posicao
 p = cria_copia_posicao(u['p'])
 
 #Copia o resto do dicionario e muda a posicao
 u_copia = u.copy()
 u_copia['p'] = p
 
 return u_copia

#Seletores----------------------------------------------------------------------

def obter_posicao(u):
 '''
 Recebe uma unidade e devolve a sua posicao.
 '''
 return u['p']



def obter_vida(u):
 '''
 Recebe uma unidade e devolve os seus pontos de vida.
 '''
 return u['hp']



def obter_forca(u):
 '''
 Recebe uma unidade e devolve os seus pontos de forca.
 '''
 return u['strg']



def obter_exercito(u):
 '''
 Recebe uma unidade e devolve o exercito a que esta pertence.
 '''
 return u['exer']

#Modificadores------------------------------------------------------------------

def muda_posicao(u,p):
 '''
 Modifica destrutivamente a unidade u alterando a sua posicao com o novo
 valor p, e devolve a propria unidade.
 '''
 u['p'] = p
 return u



def remove_vida(u,v):
 '''
 Modifica destrutivamente a unidade u alterando os seus pontos de vida
 subtraindo o valor v, e devolve a propria unidade.
 '''
 u['hp'] -= v
 return u

#Reconhecedores-----------------------------------------------------------------

def eh_unidade(arg):
 '''
 Recebe um argumento e devolve True se este corresponder a uma unidade.
 '''
 
 #Requisitos para o argumento dado seja um unidade na forma definida
 if isinstance(arg,dict)\
    and len(arg) == 4\
    and 'p' in arg\
    and 'hp' in arg\
    and 'strg' in arg\
    and 'exer' in arg\
    and eh_posicao(obter_posicao(arg))\
    and isinstance(obter_vida(arg),int)\
    and isinstance(obter_forca(arg),int)\
    and isinstance(obter_exercito(arg),str)\
    and obter_vida(arg) > 0\
    and obter_forca(arg) > 0\
    and len(obter_exercito(arg).strip()) > 0:
  return True
 
 return False
 
#Testes-------------------------------------------------------------------------

def unidades_iguais(u1,u2):
 '''
 Recebe duas unidades e devolve True se estas forem iguais.
 '''
 if u1 == u2:
  return True
 else:
  return False
 
#Transformadores----------------------------------------------------------------

def unidade_para_char(u):
 '''
 Recebe uma unidade e devolve o primeiro caracter em maiuscula correspondente
 ao exercito a que a unidade pertence.
 '''
 
 #Obter a primeira letra do nome do exercito
 exer = obter_exercito(u)[0]
 return exer.upper()



def unidade_para_str(u):
 '''
 Recebe uma unidade e devolve uma cadeia de caracteres que representa a unidade.
 '''
 stats = [obter_vida(u), obter_forca(u)]
 
 #Devolve a cadeia de caracteres que representa a unidade
 return unidade_para_char(u) + str(stats) + '@' + posicao_para_str(u['p'])

#Funcoes de alto nivel----------------------------------------------------------

def unidade_ataca(u1,u2):
 '''
 Recebe duas unidades e reduz os pontos de vida da segunda subtraido pelos 
 pontos de ataque da primeira. Devolve True se a unidade for destruida.
 '''
 u2 = remove_vida(u2, obter_forca(u1))
 
 if obter_vida(u2) <= 0:
  return True
 
 return False


def ordenar_unidades(tup):
 '''
 Recebe um tuplo com unidades e devolve um tuplo em que as unidades estao 
 ordenadas de acordo com a ordem de leitura do labirinto.
 '''

 #Transforma o tuplo numa lista
 lst_u = list(tup)

#Forma modificada do Insertion Sort de forma a ordenar as posicoes:

 for i in range(len(lst_u)):
  
  #Unidade a ser comparada
  unidade = lst_u[i]
  
  #Posicao da lista 
  posicao_lst = i
  
  #Se a posicao na lista for 0 nao existe mais nenhum elemento para ser
  #comparado,logo o atual e encontra-se primeiro na ordem de leitura
  #dos que ja foram comparados.
  #Se o elemento anterior na lista estiver um y maior do que a unidade,
  #entao a unidade encontra-se primeiro na ordem de leitura.
  #Se o y for igual compara-se os x.
  while posicao_lst > 0 and obter_pos_y(obter_posicao(lst_u[posicao_lst-1])) >=\
        obter_pos_y(obter_posicao(unidade)):
   
   #Se o y for igual compara-se o x
   if obter_pos_y(obter_posicao(lst_u[posicao_lst-1])) ==\
      obter_pos_y(obter_posicao(unidade)):
    
    #Se o elemento anterior na lista estiver um x maior do que a unidade,
    #entao a unidade encontra-se primeiro na ordem de leitura.    
    if obter_pos_x(obter_posicao(lst_u[posicao_lst-1])) >\
       obter_pos_x(obter_posicao(unidade)):
     lst_u[posicao_lst] = lst_u[posicao_lst - 1]
     posicao_lst -= 1
    
    #Caso contrario ja se encontra ordenado, e sai do while
    else:
     break
   
   #Se o y do elemento anterior for menor entao o elemento anterior passa para
   #a posicao na lista da unidade,e reduz-se a posicao na lista.
   else:
    lst_u[posicao_lst] = lst_u[posicao_lst - 1]
    posicao_lst -= 1
    
  #Como a mudanca dos elementos retira a unidade da lista e preciso introduzi-la
  #no sitio certo. Se nao houver mudanca a unidade continua na sua posicao
  lst_u[posicao_lst] = unidade  
 
 return tuple(lst_u)

#Mapa===========================================================================
#Construtores-------------------------------------------------------------------

def cria_mapa(dim,paredes,exer1,exer2):
 '''
 Recebe um (tuplo) dim de 2 valores inteiros correspondentes as dimensoes Nx e
 Ny do labirinto, um tuplo (paredes) de 0 ou mais posicoes correspondentes as
 paredes interiores do labirinto, e dois tuplos (exer1) e (exer2) cada um com 1
 ou mais unidades do mesmo exercito.
 '''
 
 #Requisito para criar um mapa
 if isinstance(dim,tuple)\
    and len(dim) == 2\
    and isinstance(dim[0],int)\
    and isinstance(dim[1],int)\
    and dim[0] >= 3\
    and dim[1] >= 3\
    and isinstance(paredes,tuple)\
    and isinstance(exer1,tuple)\
    and isinstance(exer2,tuple)\
    and len(exer1) >= 1\
    and len(exer2) >= 1:
  
  for parede in paredes:
   if not eh_posicao(parede):
    raise ValueError('cria_mapa: argumentos invalidos')
   elif not 0 < obter_pos_x(parede) < dim[0]:
    raise ValueError('cria_mapa: argumentos invalidos')
   elif not 0 < obter_pos_y(parede) < dim[1]:
    raise ValueError('cria_mapa: argumentos invalidos')
  
  for u in exer1:
   if not eh_unidade(u):
    raise ValueError('cria_mapa: argumentos invalidos')  
    
  for u in exer2:
   if not eh_unidade(u):
    raise ValueError('cria_mapa: argumentos invalidos')  
  
  #Nomes dos exercitos
  e1 = obter_exercito(exer1[0])
  e2 = obter_exercito(exer2[0])
  
  return {'dim':dim,'paredes':paredes,e1:exer1,e2:exer2}
  
 else:
  raise ValueError('cria_mapa: argumentos invalidos')
 
 return
 
 
 
def cria_copia_mapa(m):
 '''
 Recebe um mapa m e devolve uma copia deste.
 '''
 #Lista com as chaves do mapa
 keys = list(m.keys())
 keys.remove('dim')
 keys.remove('paredes')
 
 #Dimensao do mapa
 dim = m['dim']
 
 #Copia da paredes
 paredes = tuple(cria_copia_posicao(p) for p in m['paredes'])
 
 #Copia dos exercitos
 e1 = tuple(cria_copia_unidade(u) for u in m[keys[0]])
 e2 = tuple(cria_copia_unidade(u) for u in m[keys[1]])
 
 return {'dim':dim,'paredes':paredes,obter_exercito(e1[0]):e1,
         obter_exercito(e2[0]):e2}

#Seletores----------------------------------------------------------------------

def obter_tamanho(m):
 '''
 Recebe um mapa e devolve um tuplo com a dimensao do mapa.
 '''
 return m['dim']



def obter_nome_exercitos(m):
 '''
 Recebe um mapa e devolve os nomes dos exercitos ordenados.
 '''
 #Lista com o nome dos exercitos
 nome_exercitos = list(m.keys())
 nome_exercitos.remove('dim')
 nome_exercitos.remove('paredes') 
 
 return tuple(sorted(nome_exercitos))



def obter_unidades_exercito(m,exer):
 '''
 Recebe um mapa e o nome de um exercito e devolve um tuplo com as unidades do
 exercito ordenadas de acordo com a ordem de leitura do mapa.
 '''
 
 return ordenar_unidades(m[exer])
 
 
 
def obter_todas_unidades(m):
 '''
 Recebe um mapa e devolve um tuplo com todas as unidades ordenadas de acordo 
 com a ordem de leitura do labirinto.
 '''
 
 exercitos = obter_nome_exercitos(m)
 return ordenar_unidades(m[exercitos[0]] + m[exercitos[1]])
 
 
 
def obter_unidade(m,p):
 '''
 Recebe um mapa e uma posicao e devolve a unidade que se encontra nessa posicao.
 '''
 
 #Percorre o tuplo com todas as unidades do mapa e compara as posicoes destas
 #com a posicao dada
 

 for u in obter_todas_unidades(m):

  if posicoes_iguais(obter_posicao(u),p):

   return u
 
 return
 
#Modificadores------------------------------------------------------------------

def eliminar_unidade(m,u):
 '''
 Modifica destrutivamente o mapa m eliminando a unidade u do mapa e deixando
 livre a posicao onde se encontrava a unidade.
 '''
 
 #Cria uma lista com todas as unidades pertencentes ao exercito da unidade dada
 exercito_u = list(obter_unidades_exercito(m,obter_exercito(u)))
 
 #Remove a unidade da lista
 exercito_u.remove(u)
 
 #Muda no mapa o tuplo com as unidades do exercito
 m[obter_exercito(u)] = tuple(exercito_u)
 
 return m



def mover_unidade(m,u,p):
 '''
 Modifica destrutivamente o mapa m e a unidade u alterando a posicao da unidade
 no mapa para a nova posicao p e deixando livre a posicao onde se encontrava.
 '''
 
 muda_posicao(u,p)
 
 return m
 
#Reconhecedores-----------------------------------------------------------------

def eh_posicao_unidade(m,p):
 '''
 Recebe um mapa e uma posicao e devolve True se na posicao se encontra uma
 unidade.
 '''
 
 #Compara a posicao com a poscicao de todas as unidades do mapa
 
 for u in obter_todas_unidades(m):
  if posicoes_iguais(p,obter_posicao(u)):
   return True
 
 return False



def eh_posicao_parede(m,p):
 '''
 Recebe um mapa e uma posicao e devolve True se na posicao se encontra uma
 parede do labirinto.
 '''
 
 #Coordenadas garantidas de serem paredes
 if obter_pos_x(p) == 0\
    or obter_pos_y(p) == 0\
    or obter_pos_x(p) == obter_tamanho(m)[0] - 1\
    or obter_pos_y(p) == obter_tamanho(m)[1] - 1:
  return True
 
 #Compara a posicao com a posicao das paredes interiores do mapa
 for parede in m['paredes']:
  if posicoes_iguais(p,parede):
   return True
 
 return False



def eh_posicao_corredor(m,p):
 '''
 Recebe um mapa e uma posicao e devolve True se na posicao se encontra um
 corredor do labirinto(independente de estar ou nao ocupado por uma unidade).
 '''
 
 #Verifica se nao ultrapassa os limites do mapa
 if  obter_pos_x(p) > obter_tamanho(m)[0]\
     or obter_pos_y(p) > obter_tamanho(m)[1]:
  return False
 
 #Verifica se e uma parede
 elif eh_posicao_parede(m,p):
  return False
 
 return True
 
#Testes-------------------------------------------------------------------------

def mapas_iguais(m1,m2):
 '''
 Recebe dois mapas e devolve True se eles forem iguais.
 '''
 if m1 == m2:
  return True
 
 return False
 
#Transformadores------------------------------------------------------------------

def mapa_para_str(m):
 '''
 Recebe um mapa e devolve uma cadeia de caracteres que represente o mapa.
 '''
 
 #Transforma numa lista o tuplo com o tamanho do mapa
 dim_f = list(obter_tamanho(m))
 
 #Inicio do mapa
 dim_i = [0,0]
 
 mapa = ''

 #Enquanto as coordenadas de dim_i forem diferentes de dim_f entao ainda nao se
 #ultrapassou o tamanho do map (soma-se +1 as coordenadas porque as coordenadas
 #contam-se do a partir do 0 e o tamanho a partir do 1
 
 while [dim_i[0]+1,dim_i[1]+1] != dim_f:
  p = cria_posicao(dim_i[0],dim_i[1])
 
  #Aumenta-se em 1 ate x de dim_i for igual a x de dim_f(ultrapassa o limite do
  #mapa por 1) muda o x de dim_i para 0 e aumenta o y de dim_i em 1, e na 
  #na posicao atual mete-se uma muda de linha
  if dim_i[0] == dim_f[0]:
   dim_i [0] = 0
   dim_i [1] += 1
   mapa += '\n'
  
  #Se forem coordenas de uma parede
  elif eh_posicao_parede(m,p):
   mapa += '#'
   dim_i [0] += 1
  
  #Se forem coordenas de uma unidade
  elif eh_posicao_unidade(m,p):
   mapa += unidade_para_char(obter_unidade(m,p))
   dim_i [0] += 1
  
  #Se forem coordenas de um corredor
  else:
   mapa += '.'
   dim_i [0] += 1
  
  
 return mapa + '#'
 
#Funcoes de alto nivel----------------------------------------------------------

def obter_inimigos_adjacentes(m,u):
 '''
 Recebe um mapa e unidade e devolve um tuplo contendo as unidades inimigas
 adjacentes.
 '''
 
 #Tuplo com as posicoes adjacentes da unidade
 p_adj = obter_posicoes_adjacentes(obter_posicao(u))
 u_inimigas = ()
 
 #Verifica-se se na posicao encontra-se uma unidade e se essa unidade e inimiga
 for ps in p_adj:
  if eh_posicao_unidade(m,ps):
   if obter_exercito(obter_unidade(m,ps)) != obter_exercito(u):
    u_inimigas += (obter_unidade(m,ps),)
 
 return u_inimigas



def obter_movimento(mapa, unit):
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo, 
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)

#Funcoes adicionais=============================================================
#Calcula_pontos-----------------------------------------------------------------

def calcula_pontos(m,exer):
 '''
 Recebe um mapa e uma cadeia de caracteres correspondente ao nome de um dos
 exercitos do mapa e devolve a sua pontuacao (soma da vida das unidades).
 '''
 
 #Pontos iniciais
 pontos = 0
 
 #Todas as unidades do exercito dado
 exercito = obter_unidades_exercito(m,exer)
 
 #Soma dos pontos de vida de cada unidade presente no exercito
 for u in exercito:
  pontos += obter_vida(u)
 
 return pontos
 


def simula_turno(m):
 '''
 Funcao que modifica o mapa de acordo com a simulacao de um turno de batalha
 completo, e devolve o propeio mapa. Num turno cada unidade, se possivel,
 realiza um movimento e um ataque
 '''
 
 #Todas as unidades do mapa ordenadas pela ordem de leitura
 unidades_mapa = list(obter_todas_unidades(m))
 for u in unidades_mapa:

  #So realiza um turno unidade que se encontram no mapa (vivas)
  u_atual = obter_unidade(m,obter_posicao(u))
  if u_atual != None:
   
   #Posicao destino da unidade
   p_destino = obter_movimento(m,u)
  
   #Se a posicao de destino for diferente da atual, existe movimento
   if not posicoes_iguais(obter_posicao(u),p_destino):
    mover_unidade(m,u,p_destino)
   
   #Obter tuplo com os inimigos adjacentes ordenados pela ordem de leitura
   inimigos = obter_inimigos_adjacentes(m,u)
   
   #Se existir inimigos atacar o primeiro
   if len(inimigos) != 0:
    
    #Se o inimigo morrer, elimina-lo do mapa
    if unidade_ataca(u,inimigos[0]):
     eliminar_unidade(m,inimigos[0])

 return m



def simula_batalha(file,modo):
 '''
 Funcao principal que permite simular uma batalha completa. A batalha termina
 quando um dos exercitos vence ou, se apos um turno de batalha nao ocorreu 
 nenhuma alteracao no mapa. Recebe uma cadeia de caracteres e um booleano de
 devolve o nome do vencedor, em cado de empate devolve 'EMPATE'.
 A cadeia de caracteres corresponde a um ficheiro e o booleano corresponde ao
 modo de jogo - verboso(True) em que se mostra o mapa e a pontuacao apos cada
 turno de batlha e o quiet(False) em que so se mostra o mapa e a pontuacao no
 inicio e no fim da simulacao.
 '''
 
 #Abrir o ficheiro
 config = open(file)
 
 #Dimensao do mapa
 dim = eval(config.readline())
 #Caracteristicas da unidades do exercito 1
 e1 = eval(config.readline())
 #Caracteristicas da unidades do exercito 2
 e2 = eval(config.readline())
 #Paredes
 paredes = eval(config.readline())
 #Coordenadas das unidades do exercito 1
 e1_p = eval(config.readline())
 #Coordenadas das unidades do exercito 2
 e2_p = eval(config.readline())
 
 #Fechar ficheiro
 config.close()
 
 #Criacao do exercito 1
 exercito_1 = tuple(cria_unidade(cria_posicao(p[0], p[1]),e1[1],e1[2],e1[0]) for p in e1_p)
 #Criacao do exercito 2
 exercito_2 = tuple(cria_unidade(cria_posicao(p[0], p[1]),e2[1],e2[2],e2[0]) for p in e2_p)
 #Criacao das paredes
 paredes = tuple(cria_posicao(p[0], p[1]) for p in paredes)
 
 #Criar o mapa
 mapa = cria_mapa(dim,paredes,exercito_1,exercito_2)
 
 #Obter o nome do exercitos 
 exercitos = obter_nome_exercitos(mapa)
 
 #Mapa no incio
 print(mapa_para_str(mapa))
 #Pontos no inicio
 print('[ ' + exercitos[0] + ':' + str(calcula_pontos(mapa,exercitos[0])) + ' '\
       + exercitos[1] + ':' + str(calcula_pontos(mapa,exercitos[1])) + ' ]')



  #Enquanto nenhum exercito tiver 0 pontos realiza turnos
 while calcula_pontos(mapa,exercitos[0]) != 0\
       and calcula_pontos(mapa,exercitos[1]) != 0:
   
  #Copia do mapa antes do turno
  mapa_antigo = cria_copia_mapa(mapa)
   
  #Executa um turno
  simula_turno(mapa)
   
  #Modo verboso: print do mapa e pontos ao fim de cada turno)
  if modo:
   #Mapa depois de um turno realizado
   print(mapa_para_str(mapa))
   #Pontos resultantes do turno anterior
   print('[ ' + exercitos[0] + ':' + str(calcula_pontos(mapa,exercitos[0])) +\
      ' ' + exercitos[1] + ':' + str(calcula_pontos(mapa,exercitos[1])) + ' ]')
   
   
  #Se o mapa depois do turno for igual ao anterior do turno, existe empate
  if mapas_iguais(mapa_antigo,mapa):
    
   #Modo quiet: empate
   if not modo:
    #Mapa depois do ultimo turno
    print(mapa_para_str(mapa))
    #Pontos depois do ultimo turno
    print('[ ' + exercitos[0] + ':' + str(calcula_pontos(mapa,exercitos[0])) +\
       ' ' + exercitos[1] + ':' + str(calcula_pontos(mapa,exercitos[1])) + ' ]')     
    
   return ('EMPATE')
  
 #Modo quiet: vitoria de um exercito
 if not modo:
  #Mapa depois do ultimo turno
  print(mapa_para_str(mapa))
  #Pontos depois do ultimo turno
  print('[ ' + exercitos[0] + ':' + str(calcula_pontos(mapa,exercitos[0])) +\
     ' ' + exercitos[1] + ':' + str(calcula_pontos(mapa,exercitos[1])) + ' ]')    
  
 #Apos um dos exercitos tiver 0 pontos, declarar o vencedor
 if calcula_pontos(mapa,exercitos[0]) == 0:
  return exercitos[1]
  
 else:
  return exercitos[0]
 
 return
