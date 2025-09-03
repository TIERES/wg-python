import os
import random
import time

#LIMPA A TELA
def limparTela():
    if os.name == 'nt': # Para Windows
        os.system('cls')
    else: # Para Linux e macOS
        os.system('clear')

#CLASSE DO JOGADOR
class Jogador:
    def __init__(self, nome, jogada):
        self.nome = nome
        self.jogada = jogada
        self.isHumano = nome != ''
        self.zerarPontuacao()
    #SE O JOGADOR GANHOU, SOMAR +1 NOS PONTOS
    def ganhou(self):
        self.pontuacao += 1
    #ZERA TODOS OS PONTOS
    def zerarPontuacao(self):
        self.pontuacao = 0
    #MOSTRA A PONTUACAO DO JOGADOR
    def imprimePontuacao(self):
        print(f'{self.nome} [{self.jogada}]: {self.pontuacao} VITÓRIA{"" if self.pontuacao <= 1 else "S"}')
#CLASSE DO TABULEIRO
class Tabuleiro:
    def __init__(self, jogadores):
        self.limparJogadas()
        self.jogadores = jogadores
        self.isJogadorGanhou = False
        self.letras = ['A', 'B', 'C']
        for jogador in self.jogadores:
            if jogador.nome == '':
                jogador.nome = f'COMPUTADOR {list(filter(lambda _jogador: not _jogador.isHumano, self.jogadores)).index(jogador) + 1}'
    #LIMPA TODAS AS JOGADAS PARA UM NOVO JOGO
    def limparJogadas(self):
        self.jogadas = {
            'A1':' ',
            'B1':' ',
            'C1':' ',
            'A2':' ',
            'B2':' ',
            'C2':' ',
            'A3':' ',
            'B3':' ',
            'C3':' '
        }
    #IMPRIME O TABULEIRO COM AS JOGADAS
    def imprimeTabuleiro(self, isLimparTela = True):
        if (isLimparTela):
            limparTela()
        print('    A   B   C\n')
        for i in range(1,4):
            linha = ''
            for l in self.letras:
                if linha == '':
                    linha = f'{i}   '
                linha += f'{self.jogadas[f"{l}{i}"]}'
                if l != 'C':
                    linha += ' | '
            print(linha)
            if not '3' in linha:
                print('   -----------')
        print('')
    #CONVERTE A JOGADA (EXEMPLO: 1A PARA A1)
    def converterJogada(self, jogada):
        if len(jogada)>1:
            jogadaConvertida = f'{jogada[-1]}{jogada[0]}'
            jogada = jogadaConvertida if jogadaConvertida in self.jogadas.keys() else jogada
        return jogada
    #COMECA O JOGO
    def jogar(self):
        jogada = ''
        while jogada == '':
            for jogador in self.jogadores:
                if self.isJogadorGanhou:
                    self.isJogadorGanhou = False
                    limparTela()
                    continue
                if jogador.isHumano:
                    while jogada == '':
                        self.imprimeTabuleiro()
                        jogadaExemplo = random.choice(list(filter(lambda _jogada: _jogada[1] == ' ', self.jogadas.items())))[0]
                        jogada = input(f'\n{ jogador.nome }, escolha uma posição da velha para marcar [{ jogador.jogada }].'
                                       f' Ex.: { jogadaExemplo.lower() } ou { jogadaExemplo[-1] }{ jogadaExemplo[0].lower() }\n'
                                       f'[S - SAIR]: ').upper()
                        jogada = self.converterJogada(jogada)
                        if jogada == 'S':
                            continue
                        if jogada not in self.jogadas.keys() or self.jogadas[jogada] != ' ':
                            print(f'JOGADA INVÁLIDA{ ", ESSA JOGADA JÁ FOI ESCOLHIDA!" if jogada in self.jogadas.keys() and self.jogadas[jogada] != " " else "!"}')
                            time.sleep(1.5)
                            jogada = ''
                            continue
                    if jogada == 'S':
                        break
                    self.jogadas[jogada] = jogador.jogada
                    jogada = self.verificaVencedor(jogada)
                else:
                    self.imprimeTabuleiro()
                    jogada = random.choice(list(filter(lambda _jogada: _jogada[1] == ' ', self.jogadas.items())))[0]
                    print(f'A posição escolhida pelo {jogador.nome} para colocar [{jogador.jogada}] foi {jogada}!')
                    time.sleep(1.5)
                    self.jogadas[jogada] = jogador.jogada
                    jogada = self.verificaVencedor(jogada)
    #VERIFICA SE TEVE VENCEDOR OU CONTINUA O JOGO
    def verificaVencedor(self, jogada):
        if self.isGameOver():
            self.mostrarPontuacao()
            if input('Deseja jogar novamente?\n[S/N]: ').upper() == 'S':
                jogada = ''
        else:
            jogada = ''
        return jogada
    #VERIFICA SE O JOGO ACABOU COM VENCEDOR OU VELHA
    def isGameOver(self):
        _isGameOver = False
        _deuVelha = False
        for jogador in self.jogadores:
            #VERIFICA AS POSICOES VERTICAIS
            self.isJogadorGanhou = self.jogadas['A1'] == self.jogadas['A2'] == self.jogadas['A3'] == jogador.jogada
            self.isJogadorGanhou = self.jogadas['B1'] == self.jogadas['B2'] == self.jogadas['B3'] == jogador.jogada or self.isJogadorGanhou
            self.isJogadorGanhou = self.jogadas['C1'] == self.jogadas['C2'] == self.jogadas['C3'] == jogador.jogada or self.isJogadorGanhou
            #VERIFICA AS POSICOES HORIZONTAIS
            self.isJogadorGanhou = self.jogadas['A1'] == self.jogadas['B1'] == self.jogadas['C1'] == jogador.jogada or self.isJogadorGanhou
            self.isJogadorGanhou = self.jogadas['A2'] == self.jogadas['B2'] == self.jogadas['C2'] == jogador.jogada or self.isJogadorGanhou
            self.isJogadorGanhou = self.jogadas['A3'] == self.jogadas['B3'] == self.jogadas['C3'] == jogador.jogada or self.isJogadorGanhou
            #VERIFICA AS POSICOES DIAGONAIS
            self.isJogadorGanhou = self.jogadas['A1'] == self.jogadas['B2'] == self.jogadas['C3'] == jogador.jogada or self.isJogadorGanhou
            self.isJogadorGanhou = self.jogadas['A3'] == self.jogadas['B2'] == self.jogadas['C1'] == jogador.jogada or self.isJogadorGanhou
            #AVISA SE TEVE VENCEDOR
            if self.isJogadorGanhou:
                limparTela()
                print(f'* - * - * - * - {jogador.nome} [{jogador.jogada}] VENCEU! * - * - * - * -\n')
                jogador.ganhou()
                _isGameOver = True
                _deuVelha = False
                break
            else: #VERIFICA SE DEU VELHA
                if len(list(filter(lambda _jogada: _jogada == ' ', self.jogadas.values()))) == 0:
                    _deuVelha = True
                    _isGameOver = True
        if _isGameOver:
            if _deuVelha:
                print('* - * - * - * - DEU VELHA! * - * - * - * -\n')
            self.imprimeTabuleiro(False)
            self.limparJogadas()
        return _isGameOver
    def mostrarPontuacao(self):
        for jogador in self.jogadores:
            jogador.imprimePontuacao()

limparTela()
print('* - * - * - * - VAMOS JOGAR O JOGO DA VELHA! * - * - * - * -')
nomeJogador1 = input('Nome do primeiro jogador\n[ENTER - COMPUTADOR]: ').upper()
jogadaJogador1 = 'X'
jogadaJogador2 = 'O'
while True:
    if nomeJogador1 == '':
        jogadaJogador1 = random.choice(['X','O'])
        print(f'O COMPUTADOR 1 escolheu jogar com [{ jogadaJogador1 }]!')
    else:
        jogadaJogador1 = input(f'Olá { nomeJogador1 }, qual jogada deseja ser?\n[X/O]: ').upper()
    if jogadaJogador1 not in ['X', 'O']:
        print('JOGADA INVÁLIDA')
        continue
    elif jogadaJogador1 == 'X':
        jogadaJogador2 = 'O'
    else:
        jogadaJogador2 = 'X'
    break
nomeJogador2 = input('Nome do segundo jogador\n[ENTER - COMPUTADOR]: ').upper()
print(f'{ "O COMPUTADOR 2" if nomeJogador2 == "" else f"Olá { nomeJogador2 }, você" } jogará com [{ jogadaJogador2 }]!')
time.sleep(2)
tabuleiro = Tabuleiro([Jogador(nomeJogador1, jogadaJogador1), Jogador(nomeJogador2, jogadaJogador2)])
for i in range(15):
    limparTela()
    random.shuffle(tabuleiro.jogadores)
    print(f'O Jogo da Velha já vai começar, vamos escolher quem começa: [{ tabuleiro.jogadores[0].nome }]\n')
    time.sleep(0.2)
print(f'FICOU DEFINIDO QUE O { tabuleiro.jogadores[0].nome } COMEÇA!')
time.sleep(3)
#INICIA O JOGO
tabuleiro.jogar()