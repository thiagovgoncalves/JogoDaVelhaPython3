print ('+---------------+')
print ('| JOGO DA VELHA |')
print ('+---------------+')
print()

jog1 = str(input('Digite o nome do jogador 1: '))
jog2 = str(input('Digite o nome do jogador 2: '))
pontos_j1 = 0
pontos_j2 = 0
empate = 0
print ()

def jogodavelha():
    matriz = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    fim = False
    vitoria = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)) #Combinações possíveis para vencer o jogo


    def desenha(): #Desenha a matriz que representa o jogo da velha
        print(matriz[0],'|',matriz[1],'|',matriz[2])
        print('--+---+--')
        print(matriz[3],'|',matriz[4],'|',matriz[5])
        print('--+---+--')
        print(matriz[6],'|',matriz[7],'|',matriz[8])
        print()

    def j1(): #Valida se a casa escolhida para a jogada está vazia ou ocupada na vez do jogador 1
        n = escolha_numero()
        if matriz[n] == '1' or matriz[n] == '2':
            print('\nEsta casa já está ocupada. Tente novamente.')
            j1()
        else:
            matriz[n] = '1'

    def j2(): #Valida se a casa escolhida para a jogada está vazia ou ocupada na vez do jogador 2
        n = escolha_numero()
        if matriz[n] == '1' or matriz[n] == '2':
            print('\nEsta casa já está ocupada. Tente novamente.')
            j2()
        else:
            matriz[n] = '2'

    def escolha_numero(): #Valida se a casa escolhida para a jogada existe dentro da matriz
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print('\nOpção inválida. Tente novamente.')
                        continue
                except ValueError:
                   print('\nOpção inválida. Tente novamente')
                   continue

    def confere(): #Confere se houve vitória (e por qual jogador) ou se houve empate.
        global pontos_j1, pontos_j2, empate
        count = 0
        for a in vitoria:
            if matriz[a[0]] == matriz[a[1]] == matriz[a[2]] == '1':
                print('{} venceu!\n'.format(jog1))
                print('Parabéns!\n')
                pontos_j1 += 1
                return True

            if matriz[a[0]] == matriz[a[1]] == matriz[a[2]] == '2':
                print('{} venceu!\n'.format(jog2))
                print('Parabéns!\n')
                pontos_j2 += 1
                return True

        for a in range(9):
            if matriz[a] == '1' or matriz[a] == '2':
                count += 1
            if count == 9:
                print('Empatou.\n')
                empate += 1
                return True

    while not fim:
        desenha()
        fim = confere()
        if fim == True:
            break
        print('{}, escolha uma casa: '.format(jog1))
        j1()
        print()
        desenha()
        fim = confere()
        if fim == True:
            break
        print('{}, escolha uma casa: '.format(jog2))
        j2()
        print()


    if input('Jogar novamente? (s/n)\n') == 's':
        print()
        jogodavelha()
    else:
        print ('Obrigado por jogar, {} e {}.'.format (jog1, jog2))
        partidas = pontos_j1 + pontos_j2 + empate
        print ('Foram jogadas {} partidas'.format(partidas))
        print('O placar geral ficou: {} ponto(s) para o jogador {} e {} ponto(s) para o jogador {}.'.format(pontos_j1, jog1, pontos_j2, jog2))
        if pontos_j1 > pontos_j2:
            print ('O vencedor geral foi o jogador {}.'.format(jog1))
        elif pontos_j2 > pontos_j1:
            print ('O vencedor geral foi o jogador {}.'.format(jog2))
        else:
            print ('O placar geral ficou empatado.')


jogodavelha()