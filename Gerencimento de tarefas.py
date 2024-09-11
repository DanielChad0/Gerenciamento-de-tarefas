lista_de_tarefas = []
lista_filtrada = []
contador_id = 1

def adicionar_tarefa():
    global contador_id
    descricao = input('Dê a descrição da tarefa: ')
    status = input('Escolha o status da tarefa (pendente, em andamento, concluída): ')
    prioridade = input('Escolha a prioridade da tarefa (alta, média, baixa): ')
    tarefa = {
        'id': contador_id,
        'descricao': descricao, 
        'status': status,
        'prioridade': prioridade 
    }
    lista_de_tarefas.append(tarefa)
    contador_id += 1

def vizualizar_tarefas():
    if not lista_de_tarefas:
        print('Nenhuma tarefa encontrada!')
    else:
        for tarefa in lista_de_tarefas:
            print(tarefa)

def filtrar_tarefas():
    lista_filtrada.clear()
    status = input('Insira o status da(s) tarefa(s) que deseja filtrar (pendente, em andamento, concluída): ')
    prioridade = input('Insira a prioridade da(s) tarefa(s) que deseja filtrar (alta, média, baixa): ')
    for tarefa in lista_de_tarefas:
        if tarefa['status'] == status and tarefa['prioridade'] == prioridade:
            lista_filtrada.append(tarefa)
    if lista_filtrada:
        print('Tarefas filtradas:')
        for tarefa in lista_filtrada:
            print(tarefa)
    else:
        print('\nNenhuma tarefa encontrada com os filtros fornecidos.')

def menu(): 
    while True:
        print('''
    Menu:
        (1) Adicionar tarefa
        (2) Visualizar tarefas
        (3) Filtrar tarefas
        (4) Sair
''')
        escolha = input('Escolha uma opção: ')
        if escolha == '1':
            adicionar_tarefa()
        elif escolha == '2':
            vizualizar_tarefas()
        elif escolha == '3':
            filtrar_tarefas()
        elif escolha == '4':
            print('Saindo...')
            break
        else:
            print('Opção inválida!')

resultado = menu()
print(resultado)