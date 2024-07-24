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
                        url_for("my_bike_shed", username=session["user"]))
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
    my_bike_shed = list(mongo.db.my_bike_shed.find())
    return render_template("my-bike-shed.html", my_bike_shed=my_bike_shed)


@app.route("/my_bike/<bike_id>")
def my_bike(bike_id):
    bike = mongo.db.my_bike_shed.find_one({'_id': ObjectId(bike_id)})
    return render_template("my-bike.html", bike=bike)


@app.route("/add_bike", methods=["GET", "POST"])
def add_bike():
    categories = mongo.db.categories.find()

    if request.method == "POST":
        # Gets data from form and converts all values 
        # to lists so that it can be inserted into a nested dictionary
        form_data = request.form.to_dict(flat=False)
        new_bike = {}
        for key, value in form_data.items():
            # Keys are split and 'cleaned'
            keys = key.split('[')
            keys = [k.replace(']', '') for k in keys]
            d = new_bike
            for k in keys[:-1]:
                # setdefault makes sure dictionary
                # key exists before setting value
                d = d.setdefault(k, {})
            d[keys[-1]] = value[0].lower()
        mongo.db.my_bike_shed.insert_one(new_bike)
        return redirect(url_for("my_bike_shed"))

    return render_template("add-bike.html", categories=categories)


@app.route("/edit_bike/<bike_id>", methods=["GET", "POST"])
def edit_bike(bike_id):
    if request.method == "POST":
        updated_bike = request.form.to_dict()
        updated_bike_data = {}

        # Rebuilds nested dictionaries to be inserted back into db
        for key, value in updated_bike.items():
            if '.' in key:
                keys = key.split('.')
                nested_dict = {keys[-1]: value}
                for k in reversed(keys[:-1]):
                    nested_dict = {k: nested_dict}
                # Merge nested_dict into updated_bike_data
                for k, v in nested_dict.items():
                    if k in updated_bike_data:
                        updated_bike_data[k].update(v)
                    else:
                        updated_bike_data[k] = v
            else:
                updated_bike_data[key] = value

        # Perform the update with the entire updated_bike_data dictionary
        mongo.db.my_bike_shed.update_one(
            {'_id': ObjectId(bike_id)},
            {'$set': updated_bike_data}
        )

        return redirect(url_for("my_bike_shed"))

    bike = mongo.db.my_bike_shed.find_one({'_id': ObjectId(bike_id)})
    categories = mongo.db.categories.find()
    return render_template("edit-bike.html", bike=bike, categories=categories)


@app.route("/delete_bike/<bike_id>")
def delete_bike(bike_id):
    mongo.db.my_bike_shed.delete_one({'_id': ObjectId(bike_id)})
    flash("Bike successfully deleted")
    return redirect(url_for("my_bike_shed"))


@app.route("/sign_out")
def sign_out():
    session.pop("user")
    return redirect(url_for("landing"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)