# Gerenciador de Tarefas
O Gerenciador de Tarefas é um programa simples implementado em Python que utiliza o Redis para gerenciar uma lista de tarefas. Ele permite adicionar, listar, marcar tarefas como concluídas e remover tarefas da lista.

## Instalação
Certifique-se de ter o Python instalado em seu sistema. Você pode baixar o Python em python.org.

Instale o pacote redis via pip:

Copy code
pip install redis
Configuração do Redis
O gerenciador de tarefas se conecta a um servidor Redis para armazenar as tarefas. Antes de executar o programa, certifique-se de ter acesso a um servidor Redis e ajuste as configurações de conexão no arquivo atividade.py.

Uso
Execute o programa atividade.py.

Copy code
python atividade.py

# Escolha uma das opções disponíveis:

> Adicionar Tarefa: Permite adicionar uma nova tarefa à lista.
> Listar Tarefas: Lista todas as tarefas atualmente na lista.
> Marcar Tarefa como Concluída: Permite marcar uma tarefa como concluída.
> Remover Tarefa Concluída: Remove todas as tarefas marcadas como concluídas da lista.
> Remover Tarefa: Remove uma tarefa específica da lista.
> Remover Todas as Tarefas: Remove todas as tarefas da lista.
> Sair: Encerra o programa.

