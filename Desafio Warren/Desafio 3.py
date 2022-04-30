''''''
from random import Random
import numpy

matriz_vetor_aleatorio = []
vetor = []
j = 0

valor = int(input('Digite um valor: '))

for i in range(3):
    valor_soma = int(input('Digite um valor: '))
    vetor.append(valor_soma)

while True:
    
    vetor_aleatorio = []

    for i in range(3):
        valor_aleatorio = numpy.random.choice(vetor)
        vetor_aleatorio.append(valor_aleatorio)
    
    soma = 0
    for i in vetor_aleatorio:
        soma += i
        if soma == valor:  
            print(vetor_aleatorio)
            j += 1
    if j == 2:
        break

#PRECISO ACHAR UMA FORMA DE NÃO MOSTRA REPETIDOS RESULTADOS
#PRECISO ACHAR UM MODO DE PARA O WHILE