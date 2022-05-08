'''
Esse código tem como objetivo verificar a quantidade de alunos que chegaram antes da aula começar,
para saber se haverá aula ou não.
'''

#Definindo as variaveis.
chegada_normal = 0
chegada_atrasada = 0
quantidade_alunos = 0

#Recebera a informação de quantos alunos é necessário para começar a aula.
quantidade_alunos_necessario = int(input('Digite a quantidade necessário de alunos para começar a aula: '))

while True:

    #Verificara se o valor não é menor ou igual a 0.
    if quantidade_alunos_necessario <= 0:
        print('Quantidade de alunos não aceita.')
        break

    else:

        #Contador de alunos.
        quantidade_alunos += 1

        #Receberá o horário de chegada de cada aluno.
        horario_chegada = int(input(f'Digite o horário de chegada do {quantidade_alunos}° aluno: ')) 

        #verificara se o aluno chegou antes da aula começar ou se está atrasado.
        if horario_chegada <= 0:
            chegada_normal += 1
        else:
            chegada_atrasada += 1

        #Perguntara se você deseja finalizar.
        saida = str(input('Deseja continuar S/N.\n')).upper()
        
        if saida == 'N':
            break
        else:
            continue

#Verificara se os alunos que chegaram são o suficiente para começar a aula.
if quantidade_alunos_necessario > 0:
   
    if chegada_normal >= quantidade_alunos_necessario:
        print('Aula normal.\n')
    else:
        print('Aula cancelada.\n')
    
    print(f'Chegaram antes da aula começar {chegada_normal} alunos.')
    
    if chegada_atrasada == 0:
        print(f'Nenhum aluno chegou atrasado.\n')
    elif chegada_atrasada == 1:
        print(f'Chegou atrasado {chegada_atrasada} aluno.\n')
    else:
        print(f'Chegaram atrasados {chegada_atrasada} alunos.\n')

print('Programa Finalizado ✔')