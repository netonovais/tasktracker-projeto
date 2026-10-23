# TaskTracker

## Descrição
O TaskTracker é uma aplicação de linha de comando (CLI) para cadastrar e
visualizar tarefas durante a execução do programa. Cada tarefa possui título,
descrição, prioridade, data limite e status. Os dados são mantidos em memória
e o status de uma nova tarefa é definido automaticamente como `Pendente`.

## Tecnologias
- Python 3
- Docker e Docker Compose
- Git
- GitHub (para versionamento do projeto)

## Estrutura
```text
tasktracker-projeto/
├── README.md
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Pré-requisitos
- Python 3 instalado para execução local.
- Docker Desktop ou uma instalação funcional do Docker Engine com Docker
  Compose para execução em containers.
- Não são necessárias bibliotecas ou dependências externas.

## Como executar
No terminal, a partir da raiz do projeto:

```bash
python src/main.py
```

### Executar com Docker

A imagem copia somente o diretório `src/` para uma imagem
`python:3.11-slim`, define `/app` como diretório de trabalho e inicia a
aplicação com `python src/main.py`. Para construir a imagem:

```bash
docker build -t tasktracker-app .
```

Para executar o container diretamente, mantendo o terminal interativo
disponível para os comandos da aplicação:

```bash
docker run -it --rm tasktracker-app
```

O `docker-compose.yml` define o serviço `tasktracker-app`, reutiliza o
Dockerfile do projeto e mantém `stdin` e o terminal interativo habilitados.
Para construir a imagem e iniciar a aplicação pelo Docker Compose:

```bash
docker compose run --build --rm tasktracker-app
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
