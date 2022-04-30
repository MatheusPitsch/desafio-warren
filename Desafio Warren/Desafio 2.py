''''''
chegada_normal = 0
chegada_atrasada = 0
quantidade_alunos = 0

quantidade_alunos_necessario = int(input('Digite a quantidade de alunos que deve ter para começar a aula: '))

while True:


    if quantidade_alunos_necessario <= 0:
        print('Quantidade de alunos não aceita.')
        break

    else:

        quantidade_alunos += 1

        horario_chegada = int(input(f'Digite o horario de chegada do {quantidade_alunos}° aluno: ')) 

        if horario_chegada <= 0:
            chegada_normal += 1
        else:
            chegada_atrasada += 1

        saida = str(input('Deseja continuar SIM/NÃO.\n')).upper()
        if saida == 'NÃO':
            break
        else:
            continue

if quantidade_alunos_necessario > 0:
    if chegada_normal >= quantidade_alunos_necessario:
        print('Aula normal.')
    else:
        print('Aula cancelada.')
    print(f'Chegaram antes da aula começar {chegada_normal} alunos.')
    print(f'Chegaram atrasados {chegada_atrasada} alunos.')