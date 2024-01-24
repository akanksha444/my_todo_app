FILEPATH = 'todos.txt'

def current_todos(filepath_local=FILEPATH):
    #It reads the todo items from the text file

    with open(filepath_local) as file_local:
        todolist_local = file_local.readlines()
        todolist_local = [item.title() for item in todolist_local]
    return todolist_local


def write_todos(todolist_local, filepath_local=FILEPATH):
    #stores the todo items to the text file

    todolist_local = [item.title() for item in todolist_local]
    with open(filepath_local, 'w') as file_local:
        file_local.writelines(todolist_local)
    return None

if __name__ == "__main__":
    print(f'This is the value of __name__: {__name__}')