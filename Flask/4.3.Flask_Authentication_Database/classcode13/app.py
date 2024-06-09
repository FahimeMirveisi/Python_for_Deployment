import os
from flask import Flask , render_template, request, redirect, url_for, session
from deepface import DeepFace
from sqlmodel import Field, SQLModel, create_engine, Session, select
from pydantic import BaseModel


app = Flask("Analyze Face")
app.config["UPLOAD_FOLDER"] = './uploads'
app.config["ALLOWED_EXTENSIONS"] = {'png', 'jpg', 'jpeg'}

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    city: str = Field()
    username: str = Field()
    password: str = Field()


engine = create_engine('sqlite:///./database.db', echo=True)
SQLModel.metadata.create_all(engine)

# pydantic models for request validation

class RegisterModel(BaseModel):
    city: str
    username: str
    password: str

class LoginModel(BaseModel):
    username: str
    password: str

def auth(email, password):
    if email == "fahime@gmail.com" and password == "1234":
        return True
    else:
        return False
    

def allowed_file(filename):
    return True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        my_email = request.form["email"]
        my_password = request.form["password"]
        result = auth(my_email, my_password)
        if result:
            # upload
            return redirect(url_for('upload'))

        else:
            # login
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
                password=request.form["password"]
            )
        except:
            print("Type error")
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
            

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    elif request.method == "POST":
        my_image = request.files['image']
        if my_image.filename == "":
            return redirect(url_for('upload'))
        else:
            if my_image and allowed_file(my_image.filename):
                save_path = os.path.join(app.config["UPLOAD_FOLDER"], my_image.filename)
                my_image.save(save_path)

                result = DeepFace.analyze(
                    img_path = save_path,
                    actions = ['age'],
                )

                age = result[0]['age']
                print(age)


            return render_template("result.html", age = age)


# @app.route("/result")
# def result():
#     return render_template("result.html")

