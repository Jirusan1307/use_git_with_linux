# todo.py
todo_list = []

def show_todo():
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

show_todo()

def add_todo(task):
    todo_list.append(task)
