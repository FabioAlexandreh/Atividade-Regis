import redis

class TaskManager:
    def __init__(self, host, port, password):
        self.redis_client = redis.StrictRedis(host='redis-18336.c308.sa-east-1-1.ec2.cloud.redislabs.com',port=18336,password='CaNRkPVKo9tacomUnIGLB75WXoXu2Scz')
        self.id_contador = 0

    def proximo_Id(self):
        self.id_contador += 1
        return str(self.id_contador)

    def adicionar_tarefa(self, descricao, status):
        id = self.proximo_Id()
        self.redis_client.hset('tarefas', id, descricao)
        self.redis_client.hset('status_tarefas', id, status)
        return id

    def listar_tarefas(self):
        tarefas = self.redis_client.hgetall('tarefas')
        status_tarefas = self.redis_client.hgetall('status_tarefas')
        print("Lista de Tarefas:")
        for id, descricao in tarefas.items():
            status = status_tarefas.get(id, 'EM ANDAMENTO')
            print(f"Tarefa {id}: {descricao} - Status: {status}")

    def marcar_como_concluida(self, id):
        self.redis_client.hset('tarefas_concluidas', id, 'concluida')

    def remover_tarefas_concluidas(self):
        tarefas_concluidas = self.redis_client.hkeys('tarefas_concluidas')
        for id in tarefas_concluidas:
            self.redis_client.hdel('tarefas', id)
            self.redis_client.hdel('tarefas_concluidas', id)

    def remover_tarefa(self, id):
        self.redis_client.hdel('tarefas', id)
        self.redis_client.hdel('status_tarefas', id)

    def remover_todas_tarefas(self):
        self.redis_client.delete('tarefas')
        self.redis_client.delete('status_tarefas')

if __name__ == "__main__":
    task_manager = TaskManager(host='redis-18336.c308.sa-east-1-1.ec2.cloud.redislabs.com', port=18336, password='CaNRkPVKo9tacomUnIGLB75WXoXu2Scz')

    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa Concluída")
        print("5. Remover Tarefa")
        print("6. Remover Todas as Tarefas")
        print("7. Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            descricao = input("Digite a descrição da tarefa: ")
            status = input("Digite o status da tarefa (EM ANDAMENTO ou CONCLUÍDA): ")
            task_id = task_manager.adicionar_tarefa(descricao, status)
            print(f"Tarefa adicionada com sucesso! ID: {task_id}")
        elif escolha == "2":
            task_manager.listar_tarefas()
        elif escolha == "3":
            id = input("Digite o ID da tarefa a ser marcada como concluída: ")
            task_manager.marcar_como_concluida(id)
            print("Tarefa marcada como concluída!")
        elif escolha == "4":
            task_manager.remover_tarefas_concluidas()
            print("Tarefas concluídas removidas!")
        elif escolha == "5":
            id = input("Digite o ID da tarefa a ser removida: ")
            task_manager.remover_tarefa(id)
            print("Tarefa removida!")
        elif escolha == "6":
            confirmacao = input("Tem certeza que deseja remover todas as tarefas? (s/n): ")
            if confirmacao.lower() == 's':
                task_manager.remover_todas_tarefas()
                print("Todas as tarefas foram removidas!")
            else:
                print("Operação cancelada.")
        elif escolha == "7":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")
