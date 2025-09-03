numero_secreto = 4
print(f'{'-'*5} TENTE ACERTAR O NUMERO {'-'*5}\n')
chute = int(input('Chute um número de 1 a 10 (3 chances)\n'))
if chute == numero_secreto:
    print(f'{'-'*5} PARABÉNS VOCÊ ACERTOU DE PRIMEIRA {'-'*5}\n')
else:
    dica = 'MAIOR'
    if chute > numero_secreto:
        dica = 'MENOR'
    print(f'\nERROU! DICA: O NÚMERO SECREDO É {dica} QUE {chute}')
    chute = int(input(f'Chute um número de 1 a 10 (2 chances)\n'))
    if chute == numero_secreto:
        print(f'{'-'*5} PARABÉNS VOCÊ ACERTOU DE SEGUNDA {'-'*5}\n')
    else:
        dica = 'MAIOR'
        if chute > numero_secreto:
            dica = 'MENOR'
        print(f'\nERROU! DICA: O NÚMERO SECREDO É {dica} QUE {chute}')
        chute = int(input(f'Chute um número de 1 a 10 (ultima chance)\n'))
        if chute == numero_secreto:
            print(f'{'-'*5} VOCÊ ACERTOU NA ÚLTIMA CHANCE {'-'*5}\n')
        else:
            print(f'{'-'*5} VOCÊ É RUIM DE CHUTE! :( {'-'*5}\n')
print(f'\n{'-'*5} GAME OVER! {'-'*5}')
