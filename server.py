from flask import Flask, render_template, redirect, request
from flask.globals import request
from mysqlconnection import connectToMySQL
app = Flask(__name__)


@app.route("/users")
def index():
    mysql = connectToMySQL('users_schema')
    users = mysql.query_db('SELECT * FROM users;')
    print(users)
    return render_template("index.html", users = users)

@app.route("/users/new")
def show():
    mysql = connectToMySQL('users_schema')
    users = mysql.query_db('SELECT * FROM users;')
    print(users)
    return render_template("show.html", users = users)

@app.route("/users/create", methods=['POST'])
def create_new():
    mysql = connectToMySQL('users_schema')
    query ='INSERT INTO users(first_name, last_name, email) VALUE(%(first_name)s,%(last_name)s,%(email)s);'
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    mysql.query_db(query, data)
    return redirect("/users")


if __name__ == "__main__":
    app.run(debug=True)

