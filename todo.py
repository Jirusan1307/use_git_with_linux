# todo.py
todo_list = []

def show_todo():
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

show_todo()
