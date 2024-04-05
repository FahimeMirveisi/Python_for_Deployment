from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import StreamingResponse
import sqlite3

app = FastAPI()

connection = sqlite3.connect("todo.db")
my_cursor = connection.cursor()

def show_menu():
    print("*** Welcome to my ToDo API ***")
    print("1- Show plans ToDo")
    print("2- Add a new plan")
    print("3- Update a task")
    print("4- Remove your enterd plan")


@app.get("/")
def read_root():

    return show_menu()


@app.get("/tasks")
def read_tasks():
    ...


@app.put("/tasks/{id}")
def update_task():
    ...

@app.post("/tasks")
def add_task():
    ...

@app.delete("/tasks/{id}")
def delete_task():
    ...