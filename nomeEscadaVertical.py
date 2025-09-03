print('O PROGRAMA VAI PEGAR O NOME INFORMADO E IMPRIMIR EM ESCADA VERTICAL')
nome = input('Qual o seu nome? ')
escada = ''
for n in nome.replace(' ',''):
    escada += n
    print(escada.upper())