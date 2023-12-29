from flask import Flask, render_template, request

app = Flask(__name__)


# @app.route("/")
# def index():
#     # if "name" in request.args:
#     # name = request.args["name"]
#     # else:
#     # name = "Niggas!!!"
#     # name = request.args.get("name", "Nigga!!!")
#     return render_template("index.html")


# @app.route("/greet", methods=["POST"])
# def greet():
#     return render_template("greet.html", name=request.args.get("name", "Niggas!!!"))


#!TO USE ONE ROUTE
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return render_template("greet.html", name=request.form.get("name", "Niggas!!!"))


# I will not get the name that was input in the form. this is because:
# *request.args
# is only used with get, for post:
# * request.form
