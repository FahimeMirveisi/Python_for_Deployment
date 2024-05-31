from flask import Flask, render_template, request

app = Flask("Test Project")

@app.route("/", methods=["GET"])
def my_root():
    name = "Fahime"
    return render_template("index.html", name= name, x = 10)
#return "<p> Hello Flask </p>"

@app.route("/download", methods=["GET"])
def download():
    media = ["image", "music", "movie"]
    return render_template("download.html", media = media)

@app.route("/me")
def my_information():
    my_info = {"firstname": "Fahime", "email": "fahime@gmail.com"}
    return my_info

@app.route("/blog", methods=["GET", "POST"])
def blog():
    if request.method == "GET":
        return "This is get method"
    elif request.method == "PUT":
        return "This is post method"