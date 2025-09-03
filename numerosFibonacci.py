print('O PROGRAMA IRA MOSTRAR n NÚMEROS DA SÉRIE FIBONACCI')
numeros = int(input('Quantos numeros deseja mostrar? '))
serie=[]
pos=0
for i in range(numeros):
    numeroSomar=0
    if pos > 1:
        numeroSomar = serie[pos - 2]
    if pos == 0:
        serie.append(1)
    elif pos == 1:
        serie.append(serie[pos])
    else:
        serie.append(i+numeroSomar)
    pos += 1
print(','.join([str(num) for num in serie]))