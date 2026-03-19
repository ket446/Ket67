tarefas = []

while True:
    tarefa = input("Digite uma tarefa (ou 'sair' para finalizar): ")
    if tarefa.lower() == 'sair':
        break
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada!")

print("\nSua lista de tarefas:")
for i, t in enumerate(tarefas, start=1):
    print(f"{i}. {t}")
