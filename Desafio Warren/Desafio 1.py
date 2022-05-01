'''
O código tem como objetivo somar um valor X e o inverso dele, sendo que não podera conter zero no inicio de X ou valor inverso e 
o resultado da soma devera ser impar.
'''

#Criando a variavel indice.
indice = 0

#Ira gerar todos os valor de zero a um milhão.
for valor in range(1000000):
    
    soma = 0
    
    #Transformando valor em string, invertendo ele e adicionando esse valor a variavel valor_inverso.
    valor_inverso = (str(valor)[::-1])
    
    #Se o valor inverso conter zero no inicio o codigo pulara esse valor e dara continuidade.
    if '0' in valor_inverso[0]:
        continue
    
    #Transformando o valor inverso em inteiro para poder fazer o cauculo.
    valor_inverso = int(valor_inverso)
    
    #Somando os valores
    soma = valor + valor_inverso
    
    #Verificando se a soma dos valores é impar.
    if soma % 2 == 1:
        indice+=1
        print(f'A soma do valor {valor} com {valor_inverso} é {soma}.')

print(f'Existem {indice} números reversíveis abaixo de 1000000.\n')

print('Programa Finalizado ✔')