# JOGAÇO DA VELHA

from time import sleep
def exibir_tabuleiro():
    print(f'\n\033[34m{" " * 7}  {"_" * 20}')  # essse print va da alguns espaços em bracos e depois vai cirar uma linha centralizada
    print(f'{" "*7} |{" "*20}|') # esse va fazer a borda do tabuleiro
    for l,linha in enumerate(tabuleiro): # esse for vai ajudar a mostra o tabuleiro e vai serve como o idetificador das bordas da linha
        print(f'       \033[1:32m{l+1}\033[34m|\033[m     {" | ".join(linha)}      \033[34m|\033[m') # essa parte vai apresentar o tabuleiro mostrando a localização das linhas
        if l<2: # vai ver onde é pra colocar a divisão das linhas
            print(f'\033[34m{" "*8}|\033[m    {"-"*12}   \033[34m |\033[m') # essa parte vei dividir as linhas
    print(f'\033[34m{" "*8}|{"_"*20}|') # vai fecha a boda do tabuleiro
    print('               \033[1:33m1  2   3\033[m\n\n') # vai deixar visivel a localização da coluna
MUDAR_TELA= '\n \n \n \n \n \n\n\n\n\n\n'# SEPARA AS TELAS
def verificar_vitoria():
    global Alguen_ganhou # Variavel que vai mudar si acabar for verdadeiro
    J1colunas=[[],[],[]] # vai pegar so os sinbolos X que são colunas e vai tranformar em linhas dentro de um outra lista
    J1diagonal=[[],[]] # lista para ser analizada em vitorias da diagonal
    for v, l in enumerate(tabuleiro):
        for r,c in enumerate(l):
            if c == '\033[1:31mX\033[m':
                J1colunas[r].append(c)
        if l[v]=='\033[1:31mX\033[m':
            J1diagonal[0].append(l[v]) # Vitoria vertical
        if l[-(v+1)]=='\033[1:31mX\033[m':
            J1diagonal[1].append(l[v]) # Vai jogar as estringes X da vertical aocontrario para a segunda lista de vetores
    for indc,l in enumerate(tabuleiro): # verificando se o sibolo X preexeu as tres simbolos em uma mesma linhas
        vencedor1_por_linha= list(filter(lambda x: x=='\033[1:31mX\033[m',l))
        if (len(vencedor1_por_linha)==3) or ((len(J1colunas[indc]))==3) or (len(J1diagonal[0])==3) or (len(J1diagonal[1])==3):
            print(MUDAR_TELA)
            print(f'{"JOGADOR 1 VENCEU"if pley==2 else"JOGADOR VENCEU"  : >27}')
            Alguen_ganhou = True # variavel dizendo que acabou o jogo
            return
    #verificação do jogador 2
    J2colunas = [[], [],[]]  # vai pegar so os sinbolos O que são colunas e vai tranformar em linhas dentro de um outra lista
    J2diagonal = [[], []]  # lista para ser analizada em vitorias da diagonal
    for v, l in enumerate(tabuleiro):
        for r, c in enumerate(l):
            if c == '\033[1:36mO\033[m':
                J2colunas[r].append(c)
        if l[v] == '\033[1:36mO\033[m':
            J2diagonal[0].append(l[v])  # Vitoria vertical
        if l[-(v + 1)] == '\033[1:36mO\033[m':
            J2diagonal[1].append(l[v])  # Vai jogar as estringes X da vertical aocontrario para a segunda lista de vetores
    for indc, l in enumerate(tabuleiro):  # verificando se o sibolo X preexeu as tres simbolos em uma mesma linhas
        vencedor2_por_linha = list(filter(lambda x: x == '\033[1:36mO\033[m', l))

        if (len(vencedor2_por_linha) == 3) or ((len(J2colunas[indc])) == 3) or (len(J2diagonal[0]) == 3) or (len(J2diagonal[1]) == 3):
            print(MUDAR_TELA)
            print(f'{ "JOGADOR 2 VENCEU"if pley==2 else  "COMPUTADOR VENCEU": >27}')
            Alguen_ganhou = True # variavel dizendo que acabou o jogo
            return

def Deu_velha():
    for linha in tabuleiro:
        if ' ' in linha:# essa vai ser a condição para dar empate se as jogadas que é se estiver a strig espaçso no tabuleiro ele vai entra no if e vai dizer que ainda tem casa livres e a função deu velha é falsa
            return False
    print(MUDAR_TELA)
    print(f'{"O JOGO TERMINOU EM EMPATE": >33}\n')
    return True # se ele não entra no bloco de cima ele vai entra aqui e vai dezer que acabaram as casas livre e deu velha recebe verdadeiro
def Validacao_da_casa(linha,coluna): # Esse def vai veririficar se as tecla digitas  são validas
    from random import randint
    global plinha,pcoluna
    if (linha.isnumeric()) and (coluna.isnumeric()): # vai verificação de se a tecla digitadada é um numero
        plinha = int(linha)
        pcoluna = int(coluna)
        if (0<plinha<=3) and (0<pcoluna<=3): # vai verificar se o numero é valido dentre o intervalo de 1 a 9
            if not tabuleiro[plinha-1][pcoluna-1] in '\033[1:31mX\033[m\033[1:36mO\033[m':# vai verificar se a casa já esta ocupada
                print('\n\n')
                jogada_dos_jogadores() # estiver tudo ok vai mandar essa variaveis para o def jogadas dos jogadores
                return
    if pley ==2 or jogador==1:
        print(mostra_erro)
        Digitar()
    else:
        linha = str(randint(1,3))
        coluna = str(randint(1,3))# vai ser para  o computador jogar e se ele digitar alguma casa ja ocupada ele vai voltar e so vai sair dessa fução si as cordenadas estiverem ok
        Validacao_da_casa(linha, coluna) # So vai sair desse def se os digitos forem coerente as condições do jogo
def jogada_dos_jogadores():
    global jogador
     # vai analizar se a tecla digitada esta correta
    # Esse def vai subistituir os espaços em brancos por uma um sibolo que pode ser X ou O
    # Vai idetificar qual jogador é vai subistituir pelo seu respectivo simbolo
    if jogador == 1: # vai ver se é o jogador 1
        tabuleiro[plinha - 1][pcoluna - 1] = '\033[1:31mX\033[m'  # vai subistituir essas cordenadas dessa estrig dentro lista pro X
        if pley == 2:
            jogador = 2 # vai mudar a variavel para o jogador2
        else:
            if pley==1:
                jogador = 'COMPUTADOR' #essa part vai ser pra ele entra em um outro condicionate de jogada da biblioteca radom
            else:
                jogador = 1
    else:
        tabuleiro[plinha - 1][pcoluna - 1] = '\033[1:36mO\033[m' # vai subistituir essas cordenadas dessa estrig dentro lista pro O
        jogador = 1 # vai mudar a variavel para o jogador 1
def Reverter_jogada(reverter=False):
    global jogador # essa variavel vai apenas ver qual é o jogador
    if reverter:
        tabuleiro[plinha - 1][pcoluna - 1] = ' '# essa parte aqui vai pegar as ultimas corddenadas digitadas e vai subistituir por casas vasia
        exibir_tabuleiro()
        print('REFASENDO JOGADA')
        jogador = 1 if jogador==2 else 2 # como ele ta revertendo a jogada ele precisa buscar o jogador que fes a ultima jogada
        Digitar() # essa part vai mandar as novas cordernadas para mudar a jogada
        print(f"{'JOGO EM AMDAMENTO ': >29}")
        exibir_tabuleiro()
def Digitar():
    global linha,coluna
    linha = input('\033[32mLINHA X: >>\033[m' if jogador == 1 else '\033[32mLINHA O: >>\033[m')
    coluna = input('\033[33mCOLUNA X: >>\033[m' if jogador == 1 else '\033[33mCOLUNA O: >>\033[m')
    Validacao_da_casa(linha,coluna) # vai analizar se a tecla digitada esta correta

mostra_erro='\033[31mERRO DE DIGITAÇÃO. DIGITE NOVAMENTE\033[m'
def main():
    global tabuleiro,pley,jogador,Alguen_ganhou,Q_jogadas
    print('\nCOMO JOGAR ?\n\nVOCÊ VAI PECISAR DIGITAR AS CORDENADAS DA CASA PARA EFETUAR A JOGDA:\nPARA CADA JOGADA É NECESSARIO DIGITAR AS CORDENADAS DAS LINHAS E COLUNAS QUE VÃO DE 1 Á 3:\n')
    while True:
        print('\033[34mDIGITE UMA DAS DUAS OPIÇÕES :')
        print('1 - COMEÇAR JOGO..')
        print('2 - SAIR DO JOGO..')
        decisao = input('>>').strip()
        if decisao in '12':
            if decisao=='2':
                break
            while True:
                print('\033[34mDIGITE UMA DAS DUAS OPIÇÕES :')
                print('1 - JOGADOR VS MAQUINA')
                print('2 - JOGADOR VS JOGADOR')
                pley = input('>>').strip()
                if pley in '12':
                    pley = int(pley)
                    jogador = 1
                    Q_jogadas=0
                    Alguen_ganhou = False
                    reverter =False
                    tabuleiro = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
                    print('CARREGANDO..\033[m')
                    sleep(1)
                    print(MUDAR_TELA)
                    while True:

                        print(f"{'JOGO EM ANDAMENTO ': >29}")
                        exibir_tabuleiro()
                        if Q_jogadas > 0 and pley == 2:
                            while True:
                                reverter = input('DESEJA REVERTER A JOGADA ? [S/N]:').strip().upper()
                                if reverter in 'SN':
                                    break
                                print(mostra_erro)

                            reverter = True if reverter == 'S' else False
                        Reverter_jogada(reverter)
                        verificar_vitoria()
                        if Alguen_ganhou or Deu_velha():
                            exibir_tabuleiro()
                            sleep(6)
                            print(MUDAR_TELA)
                            break
                        if pley == 2:
                            print(f'Jogador: {jogador}')
                            Digitar()
                        else:
                            if jogador == 1:
                                print('JOGADOR')
                                Digitar()
                            else:
                                print('COMPUTADOR JOGANDO...')
                                sleep(3)
                                linha = 'Bloqueio'
                                coluna = 'Bloqueio'
                                Validacao_da_casa(linha, coluna)
                        Q_jogadas += 1
                        print(MUDAR_TELA)
                    break
                print(mostra_erro)
        else:
            print(mostra_erro)
    print('VOLTE SEMPRE')

if __name__=='__main__':
    main()
