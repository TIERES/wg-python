print('BEM VINDO AO PROGRAMA ME MÉDIAS DE NOTA')
print('Informe as notas do aluno')
media = 7
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
mediaCalculada = (nota1 + nota2) / 2.0
print('='*10)
print('MÉDIA FINAL: {:.2f}'.format(mediaCalculada))
if mediaCalculada == 10:
    print('APROVADO COM DISTINÇÃO!')
elif mediaCalculada >= media:
    print('Aprovado!')
else:
    print('Reprovado!')