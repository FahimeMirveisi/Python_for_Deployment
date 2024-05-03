from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import StreamingResponse
import sqlite3

app = FastAPI()

connection = sqlite3.connect("todo.db", check_same_thread=False)
my_cursor = connection.cursor()

def exist_ids():
    my_cursor.execute("SELECT id FROM tasks")
    tasks = my_cursor.fetchall()
    id_list = []
    for id_tuple in tasks:
        id_list.append(id_tuple[0])

    return id_list


@app.get("/")
def read_root():
    message = "*** Welcome to my ToDo API ***"
    return message


@app.get("/tasks")
def read_tasks ():
    my_cursor.execute("SELECT * FROM tasks")
    tasks = my_cursor.fetchall()
    
    return tasks


@app.put("/tasks/{id}")
def update_task(id: int, title: str = Form(None), description: str = Form(None), time: str = Form(None), status: int = Form(None)):
    if id not in exist_ids():
        raise HTTPException(status_code=404, detail="Task id not found")
    
    if title is not None:
        my_cursor.execute(f"UPDATE tasks SET title='{title}' WHERE id = {id}")
        connection.commit()
    if description is not None:
        my_cursor.execute(f"UPDATE tasks SET description='{description}' WHERE id = {id}")
        connection.commit()
    if time is not None:
        my_cursor.execute(f"UPDATE tasks SET time='{time}' WHERE id = {id}")
        connection.commit()
    if status is not None:
        my_cursor.execute(f"UPDATE tasks SET status={status} WHERE id = {id}")
        connection.commit()



    my_cursor.execute(f"SELECT * FROM tasks WHERE id = {id}")
    updated_task = my_cursor.fetchone()
    return updated_task



@app.post("/tasks")
def add_task(title: str = Form(None), description: str = Form(None), time: str = Form(None), status: int = Form(None)):


    if title is None or description is None or time is None or status is None:
        raise HTTPException(status_code=400, detail="title, description, time and status shoudn`t be empty")
    
    my_cursor.execute(f"INSERT INTO tasks(title, description, time, status) VALUES('{title}','{description}','{time}',{status})")
    connection.commit()
    
    message = "**********New task added**********"

    my_cursor.execute("SELECT * FROM tasks")
    tasks = my_cursor.fetchall()
    return message, tasks


@app.delete("/tasks/{id}")
def remove_task(id: int):
    
    if id not in exist_ids():
        raise HTTPException(status_code=404, detail="Task id not found")
    
    
    my_cursor.execute(f"DELETE FROM tasks WHERE id ={id}")
    connection.commit()

    message = f"Task with {id} id deleted."

    return message