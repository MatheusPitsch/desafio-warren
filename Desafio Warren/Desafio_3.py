'''
O seguinte código tem como objetivo mostrar as combinações com o menor número de elementos, 
que somados dão um valor X, que será definido pelo usuário. 
'''

from itertools import product

#Será digitado um valor aleatório que será usado como resultado final.
valor = int(input('Digite um valor: '))

#Informe os 3 valores que irão gerar diversas combinações e somar.
valores_lista = str(input('Digite os 3 valores que serão usados para a soma (SOMENTE OS NÚMEROS):')) 

#A função 'product' irá gerar todas as combinações possíveis com 3 valores. 
combinacoes = product(valores_lista, repeat = 3)

#Lista de combinações recebe todas as combinações.
lista_combinacoes = list(combinacoes)

matriz_combinacoes = []

#Todas as combinações estão no formato String, nesse for as combinações irão virar Inteiro.
for indice in lista_combinacoes:
    vetor_combinacoes = []
    for valores in indice:
        vetor_combinacoes.append(int(valores))
    matriz_combinacoes.append(vetor_combinacoes)

#Ira somar todas as combinações e verificar se a soma entre os valores é igual o valor digitado no começo. 
for indece in matriz_combinacoes:
    soma = 0
    for valores in indece:
        soma += valores
        if soma == valor:
            print(f'A soma da combinação {indece} é igual a {valor}.\n')

print('Programa Finalizado ✔')