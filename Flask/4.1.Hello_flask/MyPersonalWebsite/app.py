from flask import Flask, render_template, send_file

app = Flask("Fahime Personal website")

@app.route("/")
def my_root():
    return render_template("home.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    
    return render_template("about.html")


@app.route("/login")
def login():
    
    return render_template("login.html")


@app.route("/contact")
def contact():
    
    return render_template("contact.html")

# @app.route("/download", methods=["GET"])
# def download():
#     media = ["image", "music", "movie"]
#     return render_template("download.html", media = media)

# @app.route("/me")
# def my_information():
#     my_info = {"firstname": "Fahime", "email": "fahime@gmail.com"}
#     return my_info

@app.route("/blog")
def blog():
    # if request.method == "GET":
    #     return "This is get method"
    # elif request.method == "PUT":
    #     return "This is post method"
    return render_template("blog.html")

@app.route("/download")
def download():
    return send_file('static/fahimecv.pdf', as_attachment=True)