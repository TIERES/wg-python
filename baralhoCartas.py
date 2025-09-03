# ♠♣♥♦
import random

naipes = '♠♣♥♦'
valores = (2,3,4,5,6,7,8,9,10,'J','Q','K','A')

baralho = []
isJoker = input('Gerar Joker (s,n)? ') in ('s','S')
isEmbaralhar = input('Embaralhar (s,n)? ') in ('s','S')
quantidadeBaralho = int(input('Quantas baralhos quer jogar? '))
quantidadeJogadores = int(input('Quantas jogadores quer jogar? '))
numCartasJogador = 5
jogadorCartas = {}

def insereJoker(novoBaralho):
    jokerPos = 1
    while jokerPos <= 2:
        novoBaralho.append(f'JK{jokerPos}')
        jokerPos += 1

def criaBaralho(quantidadeBaralho = 2, isJoker = False, isEmbaralhar = True):
    _baralho = []
    novoBaralho = []
    while quantidadeBaralho > 0:
        for naipe in naipes:
            for valor in valores:
                novoBaralho.append(naipe+f'{valor}')
        if isJoker:
            insereJoker(novoBaralho)
        quantidadeBaralho -= 1
        if isEmbaralhar:
            random.shuffle(novoBaralho)
    for item in novoBaralho:
        _baralho.append(item)
    return _baralho

baralho = criaBaralho(quantidadeBaralho, isJoker, isEmbaralhar)

def mostrarBaralho(baralho):
    print(f'[{'] ['.join(baralho)}]')

print(f'Existem {len(baralho)} cartas no nosso baralho:')
mostrarBaralho(baralho)

while quantidadeJogadores > 0:
    jogadorCartas.update({quantidadeJogadores: []})
    posicaoJogador = numCartasJogador
    while posicaoJogador > 0:
        carta = baralho.pop(random.randint(0, len(baralho) - 1))
        jogadorCartas[quantidadeJogadores].append(carta)
        posicaoJogador -= 1
    quantidadeJogadores -= 1

for k, v in jogadorCartas.items():
    print(f'CARTAS DO JOGADOR {k}: [{'] ['.join(v)}]')

print(f'Agora existem {len(baralho)} cartas no nosso baralho:')
mostrarBaralho(baralho)