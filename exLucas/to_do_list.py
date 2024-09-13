from list_crud import ToDoList,show_menu

task = input("Digite uma tarefa: ")
date = input("Digite a data marcada: ")

toDoList = ToDoList(task,date)

show_menu()
