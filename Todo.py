arquivo = "tarefas.txt"

# Carrega tarefas do arquivo
try:
    with open(arquivo, "r") as f:
        tarefas = [linha.strip() for linha in f.readlines()]
except FileNotFoundError:
    tarefas = []

def mostrar_menu():
    print("\n=== MINHA LISTA DE TAREFAS ===")
    if tarefas:
        for i, t in enumerate(tarefas, start=1):
            print(f"{i}. {t}")
    else:
        print("Nenhuma tarefa cadastrada ainda.")
    print("\nComandos: 'adicionar', 'remover', 'concluir', 'sair'")

def salvar_tarefas():
    with open(arquivo, "w") as f:
        for t in tarefas:
            f.write(t + "\n")

while True:
    mostrar_menu()
    comando = input("Digite um comando: ").strip().lower()

    if comando == "sair":
        break
    elif comando == "adicionar":
        tarefa = input("Digite a tarefa: ").strip()
        tarefas.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada!")
    elif comando == "remover":
        try:
            numero = int(input("Número da tarefa para remover: "))
            if 1 <= numero <= len(tarefas):
                removida = tarefas.pop(numero-1)
                print(f"Tarefa '{removida}' removida!")
            else:
                print("Número inválido!")
        except ValueError:
            print("Digite um número válido!")
    elif comando == "concluir":
        try:
            numero = int(input("Número da tarefa concluída: "))
            if 1 <= numero <= len(tarefas):
                concluida = tarefas[numero-1]
                tarefas[numero-1] = f"[Concluída] {concluida}"
                
                print(f"Tarefa '{concluida}' marcada como concluída!")
            else:
                print("Número inválido!")
        except ValueError:
            print("Digite um número válido!")
    else:
        print("Comando não reconhecido!")

salvar_tarefas()
print("\nTodas as tarefas foram salvas. Até logo! 🚀")
