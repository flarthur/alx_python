import MySQLdb as DBase
from flask import Flask, render_template, request

app = Flask(__name__)

db = "mysql:///froshims.db"

MEMBERS = {}
SPORTS = ["Basketball", "Soccer", "Ultimate Frisbee"]


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["GET", "POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("failure.html")
    sport = request.form.get("sport")
    if sport not in SPORTS:
        return render_template("failure.html")
    MEMBERS[name] = sport
    return render_template("register.html", you=request.form.get("name", "Student."))

    # remember members
    db.execute("INSERT INTO members (name, sport) VALUES(%s, %s)", name, sport)

    # confirm registration
    return redirect("/members")


@app.route("/members")
def members():
    return render_template("members.html", members=MEMBERS)
