# todo.py

todo_list = []

def add_todo(task):
    todo_list.append(task)

def show_todo():
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

def delete_todo(index):
    if 0 <= index < len(todo_list):
        del todo_list[index]
# ลองเพิ่มรายการ
add_todo("Buy milk")
add_todo("Finish homework")
add_todo("Exercise")

# แสดงรายการ
show_todo()
