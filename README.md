# TaskTracker

## Descrição
O TaskTracker é uma aplicação de linha de comando (CLI) para cadastrar e
visualizar tarefas durante a execução do programa. Cada tarefa possui título,
descrição, prioridade, data limite e status. Os dados são mantidos em memória
e o status de uma nova tarefa é definido automaticamente como `Pendente`.

## Tecnologias
- Python 3
- Git
- GitHub (para versionamento do projeto)

## Estrutura
```text
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Pré-requisitos
- Python 3 instalado.
- Não são necessárias bibliotecas ou dependências externas.

## Como executar
No terminal, a partir da raiz do projeto:

```bash
python src/main.py
```

## Funcionalidades disponíveis
Ao executar a aplicação, o menu oferece:

1. **Cadastrar nova tarefa**: informa título, descrição, prioridade e data
   limite. A prioridade aceita `Alta`, `Média`, `Media` ou `Baixa`, e `Media`
   é armazenada como `Média`.
2. **Visualizar tarefas cadastradas**: lista todas as tarefas com suas
   propriedades; quando não há tarefas, exibe uma mensagem informativa.
3. **Sair da aplicação**: encerra o programa corretamente.

Exemplo de fluxo:

```text
Escolha uma opção: 1
Título: Revisar atividade
Descrição: Conferir os requisitos da Fase 2
Prioridade (Alta, Média ou Baixa): Alta
Data limite: 20/10/2026
Tarefa adicionada com sucesso!
```
