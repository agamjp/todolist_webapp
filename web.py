import streamlit as st
import dict
import file_functions as ff


todolist = ff.get_todos()


def add_todo(todos=todolist):
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    ff.write_todos(todos)
    st.session_state["new_todo"] = ''


def edit_todo(todos=todolist):
    todo_key = "edited_todo" + str(todos.index(to_edit))
    if todo_key in st.session_state.keys():
        new_todo = st.session_state[todo_key] + '\n'
        print(new_todo)
        todos[todos.index(to_edit)] = new_todo
        ff.write_todos(todos)
        st.session_state[todo_key] = ''
        st.rerun()


def completion_mode(todos=todolist):
    for index, item in enumerate(todolist):
        checkbox = st.checkbox(item, key=index)
        if checkbox:
            print(checkbox)
            print(item)
        todos.pop(index)
        ff.write_todos(todos)
        del st.session_state[index]
        st.rerun()


st.title("My Todo App title")
st.subheader("My Todo App title, just smaller")
st.write("And with teeny tiny letters for people with good eyes!!!")

mode = st.radio("Select mode:", key="todolist_mode",
                options=["completion", "edition"], horizontal=True)


if mode == "completion":
    st.write("To do:")
    completion_mode()
elif mode == "edition":
    to_edit = st.radio("To do:", key="to_edit", options=todolist)
    st.text_input(label="Edit:", autocomplete=to_edit,
                  key="edited_todo" + str(todolist.index(to_edit)),
                  on_change=edit_todo(), placeholder="Enter edited todo")


st.text_input(label="", placeholder=dict.todo_prompt,
              key="new_todo", on_change=add_todo)
