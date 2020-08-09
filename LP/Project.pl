%Rodrigo Afonso Rato Goncalves 95665
:-[codigo_comum].

%=========================Funcoes auxiliares=========================

%Verifica se um elemento se encontra numa lista
membro(E, [P|_]):- E == P,!.
membro(E, [_|R]):- membro(E, R).



%Retorna o indice de uma variavel numa lista
indice_variavel(1, [P|_], E):- P == E,!.

indice_variavel(I, [_|R], E):-
    indice_variavel(I_Aux, R,E),
    I is I_Aux + 1.



%Predicado que da o espaco e as palavras possiveis para esse espaco
espaco_palavras([Espaco|Palavras], Espaco, Novas_Palavras):-
    %Alisa a lista Palavras
    append(Palavras, Novas_Palavras).



%=========================obtem_letras_palavras=========================


obtem_letras_palavras(L_Palavras, Letras):-
    %Ordena a lista de palavra
    sort(L_Palavras, L_Palavras_Ordenado),
    %Decompoe cada palavra num lista com letras e cria a lista correspondente
    maplist(atom_chars, L_Palavras_Ordenado, Letras).



%=========================espaco_fila=========================


% Muda o predicado espaco_fila/2 para espaco_fila/3.
espaco_fila(Fila, Espaco):- espaco_fila(Fila, [], Espaco).

% Verifica se chegou ao fim de um espaco valido
espaco_fila([], Espaco_Aux, Espaco):-
    %Condicao para o Espaco_Aux ser um espaco valido
    length(Espaco_Aux, N),
    N >= 3,
    
    !,

    %Se o Espaco_Aux for valido, inverte-o para por na ordem
    %original
    reverse(Espaco_Aux, Espaco).

% Verifica se o Espaco_Aux e um espaco valido
espaco_fila([P|_], Espaco_Aux, Espaco):-
    %Verifica se P e uma parede(#)
    P == '#',

    %Testa o Espaco_Aux para ver se e um espaco valido
    espaco_fila([], Espaco_Aux, Espaco).

%Se o Espaco_Aux no anterior nao for um espaco valido, limpa o Espaco_Aux
%e continua a procura por um espaco valido
espaco_fila([P|R], _, Espaco):-
    P == '#',
    espaco_fila(R, [], Espaco).

%Se o P for diferente de uma parede(#) adiciona-o ao Espaco_Aux,e continua
%a procura.
espaco_fila([P|R], Espaco_Aux ,Espaco):-
    P \== '#',
    espaco_fila(R, [P|Espaco_Aux], Espaco).



%=========================espacos_fila=========================


espacos_fila(Fila, Espacos):-

    %Encontra todas os espacos validos da fila dada 
    bagof(X, espaco_fila(Fila, X), Espacos),
    
    %Evita solucoes extra, nomeadamente a lista vazia
    !.

espacos_fila(_, []).



%=========================espacos_puzzle=========================


espacos_puzzle(Grelha,Espacos):-
    %%Encontra todos os espacos horizontais
    maplist(espacos_fila, Grelha, Espacos_Horizontais),

    %Transpoe a matriz de forma a ter listas com os espacos verticais
    mat_transposta(Grelha, Grelha_Transposta),
    
    %Encontra todos os espacos verticais
    maplist(espacos_fila, Grelha_Transposta, Espacos_Verticais),

    %Junta as listas de espacos horizontais e verticais de forma a 
    %obter os espacos totais da grelha
    append(Espacos_Horizontais, Espacos_Verticais, Espacos_Totais),

    %Alisa a lista de forma a ter o output correto
    append(Espacos_Totais, Espacos).



%=========================espacos_com_posicoes_comuns=========================


%Transforma o predicado espacos_com_posicoes_comuns/2 em espacos_com_posicoes_comuns/3
espacos_com_posicoes_comuns(Lista_Espacos, Espaco, Espacos_Comuns):- 

    %Retira da variavel Lista_Espacos o espaco a ser avaliado
    exclude(==(Espaco), Lista_Espacos, Espacos_Possiveis),
    espacos_com_posicoes_comuns_aux(Espacos_Possiveis, Espaco, Espacos_Comuns).


%Caso terminal da recursao, ja nao elementos no espaco a ser avaliado
espacos_com_posicoes_comuns_aux(_, [], []).
    

%Predicado que encontra os espacos em comum com as variaveis do espaco dado
espacos_com_posicoes_comuns_aux(Lista_Espacos, [P|R],[Alisa_Comum|Espacos_Comuns]):-

    %Verificar se P e uma variavel
    var(P),

    %Encontra o espaco em comum com a variavel
    bagof(X, (member(X,Lista_Espacos), membro(P,X)), Comum),

    %Retira a lista a mais do espaco
    append(Comum, Alisa_Comum),

    %Recursao
    espacos_com_posicoes_comuns_aux(Lista_Espacos, R, Espacos_Comuns),!.

%Nao ha espaco em comum com a variavel
espacos_com_posicoes_comuns_aux(Lista_Espacos, [_|R], Espacos_Comuns):-
    espacos_com_posicoes_comuns_aux(Lista_Espacos, R, Espacos_Comuns).

%=========================palavra_possivel_esp=========================


palavra_possivel_esp(Palavra, Espaco, Espacos_Totais, Letras):-

    %Compara o tamanho da palavra com o tamanho do espaco
    length(Palavra,Dim_Palavra),
    length(Espaco,Dim_Espaco),
    Dim_Palavra == Dim_Espaco,

    %Verifica se a palavra unifica com o espaco 
    subsumes_term(Espaco,Palavra),

    %Espacos comuns ao espaco dado
    espacos_com_posicoes_comuns(Espacos_Totais, Espaco, Espacos_Comuns),

    %Ver se existem palavras com as mesmas letras que a palavra dada
    %nas posicoes em comum com a posicao dada
    palavras_complementares(Palavra,Espaco,Espacos_Comuns,Letras).

%Caso terminal da recursao
palavras_complementares([],[],[],_).


palavras_complementares([Letra_Palavra|R_Palavra],[P|R],[Posicao_Comum|R_Comum],Letras):-
    %Verificar se a Posicao_Comum e a posicao que contenha P, se for
    %verdade obtem o indice na Posicao_Comum onde P se encontra
    %O indice indica onde a letra da palavra correspondente ao posicao P se
    %encontra na posicao comum
    indice_variavel(I_Letra,Posicao_Comum,P),

    !,

    %Procura palavras na lista Letras que tenham letras correspondentes no 
    %indice e e que unifiquem com o espaco(Verifica tamanho e posicao de letras que ja existam)
    %Letra
    bagof(X, (member(X,Letras), nth1(I_Letra, X, Letra_Palavra)), Palavras_Possiveis),

    %Ver se as palavras possiveis unificam com o espaco dado, de forma a ter em conta
    %as letras que ja se encontrem no espaco
    bagof(Z, (member(Z,Palavras_Possiveis), subsumes_term(Posicao_Comum,Z)),_),
    
    %Continua a recursao
    palavras_complementares(R_Palavra, R, R_Comum, Letras).
 
%Caso nao haja espaco comum para a posicao P ou palavras com letras no indice dado
palavras_complementares([_|R_Palavra],[_|R],Espacos_Comuns,Letras):-
    palavras_complementares(R_Palavra, R, Espacos_Comuns, Letras).


%=========================palavras_possiveis_esp=========================


palavras_possiveis_esp(Letras, Espacos_Totais, Espaco, Palavras_Possiveis):-

    %Encontra todas as palavras da lista Palavras_Possiveis que satisfacam o predicado palavra_possivel_esp 
    findall(X,(member(X,Letras), palavra_possivel_esp(X, Espaco, Espacos_Totais, Letras)), Palavras_Possiveis).



%=========================palavras_possiveis=========================


palavras_possiveis(Letras, Espacos, Palavras_Possiveis):-
    %Para dada espaco encontra a palavras que tem os requesitos necessarios para pertencer a esse
    bagof([X,Y], (member(X, Espacos), palavras_possiveis_esp(Letras, Espacos, X, Y)), Palavras_Possiveis).



%=========================letras_comuns=========================


letras_comuns(Lista_Palavras, Letras_Comuns):-

    %Escolhe a primeira palavra da lista para servir de teste
    nth1(1, Lista_Palavras, Palavra),

    %Retira a primeira Palavra da lista
    exclude(==(Palavra), Lista_Palavras, Nova_Lista_Palavras),

    %Procura na lista de palavras as palavras que tem a mesma letra que a 
    %primeira palavra na mesma posicao
    procura_letra_comum(Palavra, Nova_Lista_Palavras, 0, Letras_Comuns).


%Caso terminal da recursao
procura_letra_comum([], _, _, []).

procura_letra_comum([Letra|R_Palavra], Lista_Palavras, Indice, [(Indice_Atual,Letra)|Letras_Comuns]):-
    
    %Indice da Letra atual a ser verificada
    Indice_Atual is Indice + 1,

    %Devolve uma lista vazia se todas as palavras tem a letra na posicao correta
    findall(X, (member(X, Lista_Palavras),\+ nth1(Indice_Atual, X, Letra)), Lista_Vazia),
    Lista_Vazia == [],

    !,
    
    %Continua a procura
    procura_letra_comum(R_Palavra, Lista_Palavras, Indice_Atual, Letras_Comuns).

procura_letra_comum([_|R_Palavra], Lista_Palavras, Indice, Letras_Comuns):-
    %Indice da Letra que falhou no caso anterior
    Indice_Atual is Indice + 1,
    procura_letra_comum(R_Palavra, Lista_Palavras, Indice_Atual, Letras_Comuns).



%=========================atribui_comuns=========================


atribui_comuns([]).

%Escolhe uma lista com o espaco e as palavras possiveis para este
atribui_comuns([Espaco_Palavras|R]):-
  
    %Obtem o espaco e as palavras possiveis para esse
    espaco_palavras(Espaco_Palavras, Espaco, Palavras),
    
    %Verifica se existe 1 ou mais palavras para o espaco 
    length(Palavras, N_Palavras),
    N_Palavras >= 1,

    %Encontra as letras comuns entre as palavras dadas
    letras_comuns(Palavras, Letras_Comuns),
    
    %Unificacao das variaveis com as letras em posicoes comuns
    unificacao(Espaco, Letras_Comuns),

    %Proxima lista
    atribui_comuns(R).


unificacao(_,[]).

unificacao(Espaco,[(Indice, Letra)|R_Letra]):-

    %Unifica a variavel em Indice com a letra dada
    nth1(Indice,Espaco,Letra),

    %Continua a unificacao
    unificacao(Espaco, R_Letra).



%=========================retira_impossiveis=========================


%Caso terminal da recursao
retira_impossiveis([], []).


retira_impossiveis([Espaco_Palavras|R], [[Espaco, Possiveis]|Novas_Palavras_Possiveis]):-

    %Obtem o espaco e as palavras possiveis para esse
    espaco_palavras(Espaco_Palavras, Espaco, Palavras),

    %Encontra todas as palvras que o espaco pode unificar
    findall(X,(member(X,Palavras), subsumes_term(Espaco,X)), Possiveis),

    %Adiciona a lista com o espaco e as palavras que o espaco consegue unificar e continua a recursao
    retira_impossiveis(R, Novas_Palavras_Possiveis).



%=========================obtem_unicas=========================


obtem_unicas([],[]).

obtem_unicas([Espaco_Palavras|R], [Alisa_Palavra|Unicas]):-

    %Obtem as palavras possiveis para o espaco atual
    espaco_palavras(Espaco_Palavras, _, Palavra),

    %Verifica se so existe uma palavra possivels
    length(Palavra, N_Palavras),
    N_Palavras == 1,

    !,

    %Alisa a palavra para tirar a lista extra
    append(Palavra, Alisa_Palavra),

    %Continua a procura
    obtem_unicas(R,Unicas).

%No caso de o espaco anterior ter mais do que uma palavra possivel
%Continua para o proximo
obtem_unicas([_|R], Unicas):-
    obtem_unicas(R,Unicas).



%=========================retira_unicas=========================


retira_unicas(Palavras_Possiveis, Novas_Palavras_Possiveis):-

    %Obtem todas as palavras unicas 
    obtem_unicas(Palavras_Possiveis, Unicas),

    %retira_unicas/2 passa para retira_unicas/3
    retira_unicas(Palavras_Possiveis, Unicas, Novas_Palavras_Possiveis).


%Caso final da recursao
retira_unicas([],_,[]).


retira_unicas([Espaco_Palavras|R], Unicas, [[Espaco,Novas_Palavras]|Novas_Palavras_Possiveis]):-
    
    %Obtem o espaco e as palavras possiveis para o espaco atual
    espaco_palavras(Espaco_Palavras, Espaco, Palavras),

    %Ver se o espaco tem mais do que uma palavra unica
    length(Palavras,N_Palavras),
    N_Palavras > 1,

    %Encontra todas as palavras do espaco que pertencem a lista de unicas
    %e cria uma lista sem essas
    findall(X,(member(X,Palavras), \+member(X,Unicas)), Novas_Palavras),

    !,

    %Continua a procura
    retira_unicas(R, Unicas, Novas_Palavras_Possiveis).

%No caso de so existir 1 palavra possivel para o espaco
retira_unicas([Espaco_Palavras|R], Unicas, [[Espaco,Palavra]|Novas_Palavras_Possiveis]):-
    %Obtem o espaco e as palavras possiveis para o espaco atual
    espaco_palavras(Espaco_Palavras, Espaco, Palavra),

    %Continua a procura
    retira_unicas(R, Unicas, Novas_Palavras_Possiveis).



%=========================simplifica=========================

simplifica(Palavras_Possiveis, Novas_Palavras_Possiveis):-


    %Aplicacao dos 3 predicados necessarios
   
    atribui_comuns(Palavras_Possiveis),
    retira_impossiveis(Palavras_Possiveis, Palavras_Possiveis_Sem_Impossiveis),
    retira_unicas(Palavras_Possiveis_Sem_Impossiveis, Palavras_Possiveis_Sem_Unicas),

    %Verifica se o Palavras_Possiveis recebido e igual ao resultado final de aplicacar os
    %3 predicados, ou seja nao houve nenhuma alteracao&
    Palavras_Possiveis_Sem_Unicas \== Palavras_Possiveis,

    !,

    %Se nao forem iguais
    simplifica(Palavras_Possiveis_Sem_Unicas, Novas_Palavras_Possiveis).


%Se nao houver nenhuma alteracao acaba o ciclo
simplifica(Palavras_Possiveis, Palavras_Possiveis):-
    
    atribui_comuns(Palavras_Possiveis).


%=========================inicializa=========================


inicializa([Palavras|Grelha],Palavras_Possiveis):-

    %Retira a lista a mais da grelha
    append(Grelha, Grelha_Correta),

    %Obtem a lista com as listas das letras de cada palavra
    obtem_letras_palavras(Palavras,Letras),

    %Obtem os espacos vazio so puzzle
    espacos_puzzle(Grelha_Correta, Espacos),

    %Obtem as palavras possiveis para cada espaco vazio
    palavras_possiveis(Letras, Espacos, Pre_Palavras_Possiveis),

    %Simplifica o maximo possivel os espaco com as palavras
    simplifica(Pre_Palavras_Possiveis, Palavras_Possiveis).



%=========================escolhe_menos_alternativas=========================


escolhe_menos_alternativas([Espaco_Palavras|R], Escolha):-

    %Obtem o espaco e as palavras possiveis para o espaco atual
    %De forma a encontrar um caso teste para servir de comparacao
    espaco_palavras(Espaco_Palavras, _, Palavras),

    %Ver se o tamnho e maior do que 1
    length(Palavras, N_Palavras),
    N_Palavras > 1,

    %Procura pela lista o caso valido em primeiro lugar
    procura_menos_alternativa(R, Espaco_Palavras, N_Palavras, Escolha),
    
    !.

%Se o Espaco_Palavras anterior so tenha uma palvra para o espaco
escolhe_menos_alternativas([_|R], Escolha):-
    escolhe_menos_alternativas(R, Escolha).



%Caso final da recursao
procura_menos_alternativa([], Espaco_Palavras, _, Espaco_Palavras).

procura_menos_alternativa([Espaco_Palavras|R], _, N_Teste, Escolha):-

    %Encontra as palavras possiveis para o espaco 
    espaco_palavras(Espaco_Palavras, _, Palavras),

    %Verifica se o numero de palavras encontradas para o espaco considerado
    %e maior do que 1 e menor do que o atual menor numero de palavras para um espaco
    length(Palavras, N_Palavras),
    N_Palavras > 1,
    N_Palavras < N_Teste,

    !,

    %Continua a procura
    procura_menos_alternativa(R, Espaco_Palavras, N_Palavras, Escolha).

%Caso o Espaco_Palavras anterior nao se o novo menor
procura_menos_alternativa([_|R], Espaco_Palavras, N_Teste, Escolha):-
    procura_menos_alternativa(R, Espaco_Palavras, N_Teste, Escolha).



%=========================experimenta_pal=========================


experimenta_pal([Espaco|Palavras], Palavras_Possiveis, Novas_Palavras_Possiveis):-
    %Retira a lista a mais
    append(Palavras, Alisa_Palavras),

    %Preparacao para a escolha de uma das palavras possiveis para unificar o espaco 
    experimenta_escolhe(Espaco, Alisa_Palavras, Palavras_Possiveis, Novas_Palavras_Possiveis).



%Escolhe a primeira palavra da lista para unificar com o espaco
experimenta_escolhe(Espaco, [Palavra|_], Palavras_Possiveis, Novas_Palavras_Possiveis):-

    %Cria o Novas_Palavras_Possiveis com a palavra unificada com o espaco 
    experimenta_constroi(Espaco, Palavra, Palavras_Possiveis, Novas_Palavras_Possiveis).


%Passa para a proxima palavra possivel para o espaco dado
experimenta_escolhe(Espaco, [_|R_Palavras], Palavras_Possiveis, Novas_Palavras_Possiveis):-
    experimenta_escolhe(Espaco, R_Palavras, Palavras_Possiveis, Novas_Palavras_Possiveis).



%Caso final da recursao
experimenta_constroi(_, _, [], []).

experimenta_constroi(Espaco, Palavra, [Espaco_Palavras| R_Palavras_Possiveis], [[Espaco,[Palavra]]|Novas_Palavras_Possiveis]):-
    
    %Obtem o espaco atual do Palavras_Possiveis e compara para ver se e igual ao dado
    espaco_palavras(Espaco_Palavras, Mesmo_Espaco, _),
    Espaco == Mesmo_Espaco,

    !,

    %Unifica a palavra com o espaco
    Espaco = Palavra,

    %Continua a construir o Novas_Pals_Possiveis
    experimenta_constroi(Espaco, Palavra, R_Palavras_Possiveis, Novas_Palavras_Possiveis).

%Caso o espaco do Palavras_Possiveis seja diferente do dado continua
experimenta_constroi(Espaco, Palavra, [Espaco_Palavra| R_Palavras_Possiveis], [Espaco_Palavra|Novas_Palavras_Possiveis]):-
    experimenta_constroi(Espaco, Palavra, R_Palavras_Possiveis, Novas_Palavras_Possiveis).



%=========================resolve_aux=========================


%Verifica se so existe uma palavra possivel para o espaco
comp_1(Espaco_Palavras):- 
    espaco_palavras(Espaco_Palavras, _, Palavras),
    length(Palavras, N_Palavras),
    N_Palavras == 1.

%Verifica todos os espaco so tem uma palavra possivel
resolvido(Simp_Palavras_Possiveis, Simp_Palavras_Possiveis):-
    %Devolve lista vazia se todos os espaco so tiverem 1 palavra
    exclude(comp_1, Simp_Palavras_Possiveis, Vazia),
    Vazia == [].



resolve_aux(Palavras_Possiveis, Novas_Palavras_Possiveis):-
    %Verifica se o Palavras_Possiveis ja e uma soulcao
    resolvido(Palavras_Possiveis, Novas_Palavras_Possiveis).


%Se nao for solucao continua a procura
resolve_aux(Palavras_Possiveis, Novas_Palavras_Possiveis):-

    %Escolhe o espaco com o menor numero de palavra possiveis
    escolhe_menos_alternativas(Palavras_Possiveis, Escolha),

    experimenta_pal(Escolha, Palavras_Possiveis, Palavras_Possiveis_Aux),

    simplifica(Palavras_Possiveis_Aux, Simp_Palavras_Possiveis),

    %Continua a procura
    resolve_aux(Simp_Palavras_Possiveis, Novas_Palavras_Possiveis),

    !.



%=========================resolve=========================


resolve(Puzzle):-

    %Palavras possivies para o puzzle
    inicializa(Puzzle,Palavras_Possiveis),

    %Caso o puzzle nao seja resolvido no inicializa, e resolvido no
    %resolve_aux, se for fica igual
    resolve_aux(Palavras_Possiveis, _).


%===========================================================================