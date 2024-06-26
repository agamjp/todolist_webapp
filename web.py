import streamlit as st
import dict
import file_functions as ff


todolist = ff.get_todos()


def add_todo(todos=todolist):
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    ff.write_todos(todos)
    st.session_state["new_todo"] = ''


def edit_todo(index_, todos=todolist):
    todo_key = "edited_todo" + str(index_)
    if todo_key in st.session_state.keys():
        new_todo = st.session_state[todo_key] + '\n'
        print(new_todo)
        todos[index_] = new_todo
        ff.write_todos(todos)
        st.session_state[todo_key] = ''
        st.rerun()


def completion_mode(index_, todos=todolist):
    todos.pop(index_)
    ff.write_todos(todos)
    # del st.session_state[index_]
    st.rerun()


st.title("My Todo App")
st.subheader("An App of Mine with Todos")
st.write("It is an <b>App</b> where I can add and edit <b>Todos</b>, and it belongs to <b>Me</b>",
         unsafe_allow_html=True)

mode = st.radio("Select mode:", key="todolist_mode",
                options=["completion", "edition"], horizontal=True)
if len(todolist) == 0:
    st.write("The list is empty!")
else:
    chosen_todo = st.radio("To do:", key="todo", options=[i for i in todolist], index=None)
    for index, item in enumerate(todolist):
        if chosen_todo == item:
            if mode == "edition":
                st.text_input(label="Edit selected todo:", autocomplete=item,
                              key="edited_todo" + str(index), label_visibility="visible",
                              on_change=edit_todo(index), placeholder="Enter edited todo")
            else:
                completion_mode(index)

st.text_input(label="", placeholder=dict.todo_prompt,
              key="new_todo", on_change=add_todo)
