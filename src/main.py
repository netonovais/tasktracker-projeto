"""Aplicação de linha de comando para gerenciamento de tarefas."""


def solicitar_titulo() -> str:
    """Solicita um título não vazio e remove espaços nas extremidades."""
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("O título não pode ficar vazio. Tente novamente.")


def solicitar_prioridade() -> str:
    """Solicita uma prioridade válida e a normaliza para o formato padrão."""
    prioridades = {
        "Alta": "Alta",
        "Média": "Média",
        "Media": "Média",
        "Baixa": "Baixa",
    }

    while True:
        prioridade_informada = input("Prioridade (Alta, Média ou Baixa): ").strip()
        prioridade = prioridades.get(prioridade_informada)
        if prioridade:
            return prioridade
        print("Prioridade inválida. Informe Alta, Média ou Baixa.")


def cadastrar_tarefa(tarefas: list[dict[str, str]]) -> None:
    """Lê os dados de uma tarefa e adiciona a tarefa à lista."""
    print("\n--- Cadastro de tarefa ---")
    tarefa = {
        "titulo": solicitar_titulo(),
        "descricao": input("Descrição: ").strip(),
        "prioridade": solicitar_prioridade(),
        "data_limite": input("Data limite: ").strip(),
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")


def listar_tarefas(tarefas: list[dict[str, str]]) -> None:
    """Exibe todas as tarefas cadastradas de forma organizada."""
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Não existem tarefas cadastradas.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao'] or '(sem descrição)'}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite'] or '(não informada)'}")
        print(f"Status: {tarefa['status']}")


def exibir_menu() -> str:
    """Exibe o menu principal e retorna a opção informada."""
    print("\n=== TaskTracker ===")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")
    return input("Escolha uma opção: ").strip()


def main() -> None:
    """Executa o loop principal da aplicação."""
    tarefas: list[dict[str, str]] = []

    while True:
        opcao = exibir_menu()
        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("Aplicação encerrada. Até mais!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()