import os
from flask import (
    Flask, render_template, redirect,
    request, session, url_for, flash)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/landing")
def landing():
    return render_template("landing.html")


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if user_exists:
            flash("User already exists")
            return redirect(url_for("sign_up"))
        
        new_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(new_user)

        session["user"] = request.form.get("username").lower()
        flash("User created successfully")
        return redirect(url_for("my_bike_shed"))

    return render_template("sign-up.html")


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if user_exists:
            if check_password_hash(
                user_exists["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome {}".format(request.form.get("username")))
                    return redirect(
                        url_for("my_profile", username=session["user"]))
            else:
                flash("Username and/or password incorrect")
                return redirect(url_for("sign_in"))
        else:
            flash("Username and/or password incorrect")
            return redirect(url_for("sign_in"))
        
    return render_template("sign-in.html")


@app.route("/my_profile/<username>", methods=["GET", "POST"])
def my_profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    if session["user"]:
        return render_template("my-profile.html", username=username)
    
    return redirect(url_for("sign_in"))


@app.route("/my_bike_shed")
def my_bike_shed():
    my_bike_shed = mongo.db.my_bike_shed.find()
    return render_template("my-bike-shed.html", my_bike_shed=my_bike_shed)


@app.route("/sign_out")
def sign_out():
    session.pop("user")
    return redirect(url_for("sign_in"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)