class ToDoList:
    task = ''
    date = ''

    def __init__(self, task, date):
        self.task = task
        self.date = date
    
    def __str__(self):

        return f"Tarefa: {self.task} \nData: {self.date}"

    def do_action(msg):
    
        with open("do_list.txt", "w", encoding="utf-8") as file:
            file['task:'].append(msg)
            
def show_menu():
        print('======To_Do_List=======')
        print('= 1. Adicionar Tarefa =')
        print('= 2. Remover Tarefa   =')
        print('= 3. Exibir Tarefa    =')
        print('= 4. Sair do Programa =')
        print('=======================')