# todo.py
todo_list = []

def show_todo():
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

def delete_todo(index):
    if 0 <= index < len(todo_list):
        del todo_list[index]


show_todo()
