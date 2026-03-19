tarefas = []

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)

    elif opcao == "2":
        for i, t in enumerate(tarefas):
            print(f"{i+1}. {t}")

    elif opcao == "3":
        break
