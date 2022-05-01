''''''
i = 0
for valor in range(1000000):
    
    soma = 0
    
    valor_inverso = (str(valor)[::-1])
    
    if '0' in valor_inverso[0]:
        continue
    
    valor_inverso = int(valor_inverso)
    
    soma = valor + valor_inverso
    
    if soma % 2 == 1:
        i+=1
        print(f'A soma do valor {valor} com {valor_inverso} é {soma}.')

print(f'Existem {i} números reversíveis abaixo de 1000000.')