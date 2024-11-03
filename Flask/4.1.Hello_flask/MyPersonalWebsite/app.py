from flask import Flask, render_template, request, redirect, url_for, session
from sqlmodel import Field, SQLModel, create_engine, Session, select
from pydantic import BaseModel

""" 
from flask import Flask, render_template, url_for, redirect, request, send_file
from .database import create_db_and_tables, engine
from sqlmodel import Session, select
from .schemas import RegisterModel
from .models import User
"""

app = Flask("Fahime Personal website")

""" create_db_and_tables() """

class User(SQLModel, table=True):
    id: int

def auth(email, password):
    if email == "fahime@gmail.com" and password == "1234":
        return True
    else:
        return False


@app.route("/")
def my_root():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        my_username = request.form["username"]
        my_password = request.form["password"]
        result = auth(my_username, my_password)
        if result:
            return redirect(url_for('blog'))
        else:
            return redirect(url_for('login'))
        
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        try:
            register_data = RegisterModel(
                city=request.form["city"],
                username=request.form["username"],
                password=request.form["password"],
                firstname=request.form["first_name"],
                lastname=request.form["last_name"],
                country=request.form["country"],
                confirmedpass=request.form["confirm_password"],
                age=request.form["age"],
                email=request.form["email"]
            )

        except:
            print("TypeError")
            return redirect(url_for("register"))
        
        with Session(engine) as db_session:
            statement = select(User).where(User.username == register_data.username)
            result = db_session.exec(statement).first()

        if not result:
            with Session(engine) as db_session:
                user = User(
                    city=register_data.city,
                    username=register_data.username,
                    password=register_data.password
                )

                db_session.add(user)
                db_session.commit()

            print("Your register done successfully")
            return redirect(url_for("login"))
            
        else:
            print("Username already exist, Try another username")
            return redirect(url_for("register"))



@app.route("/contact")
def contact():
    
    return render_template("contact.html")




@app.route("/blog")
def blog():
    
    return render_template("blog.html")

@app.route("/download")
def download():
    return send_file('static/fahimecv.pdf', as_attachment=True)