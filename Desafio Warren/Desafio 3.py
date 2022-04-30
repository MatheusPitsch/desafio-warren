''''''
from random import Random

import numpy


vetor = []
soma = 0
j= 0

valor = int(input('Digite um valor: '))

for i in range(3):
    valor_soma = int(input('Digite um valor: '))
    vetor.append(valor_soma)

while True:
    
    vetor_aleatorio = []

    for i in range(3):
        valor_aleatorio = numpy.random.choice(vetor)
        vetor_aleatorio.append(valor_aleatorio)
    
    for i in vetor_aleatorio:
        if soma == valor:
            print(vetor_aleatorio)
            j += 1
    
    if j == 10:
        break
