import streamlit as st
import functions
FILEPATH = "todos.txt"

todoList = functions.current_todos(FILEPATH)
def add_todo():
    todo = st.session_state["todo_input"] + '\n'
    print(todo)
    todoList.append(todo)
    functions.write_todos(todoList)

st.title("My todo App")
for index,todo in enumerate(todoList):
    checkbox_state = st.checkbox(todo, key=todo)
    if checkbox_state:
        todoList.pop(index)
        functions.write_todos(todoList)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter todo", label_visibility='hidden',
              placeholder="Add to todo..." ,
              on_change=add_todo, key="todo_input")

st.session_state