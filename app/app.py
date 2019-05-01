from flask import Flask, jsonify, g, render_template
import requests
import sqlite3
import os
from pprint import pprint

# the all-important app variable:
app = Flask(__name__)
DATABASE = "./database.sqlite"

# check if the database exist, if not create the table and insert a few lines of data
if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE users 
               (first_name TEXT  NOT NULL, 
                last_name TEXT   NOT NULL, 
                age INTEGER   NOT NULL, 
                favorite_color TEXT  NOT NULL);''')
    conn.commit()
    cur.execute("INSERT INTO users VALUES('Mike', 'Tysonull', '40', 'Blue');")
    cur.execute("INSERT INTO users VALUES('Thomas', 'Jasper', '40', 'Purple');")
    cur.execute("INSERT INTO users VALUES('Jerry', 'Mouse', '40', 'Yellow');")
    cur.execute("INSERT INTO users VALUES('Peter', 'Pan', '40', 'Pink');")
    conn.commit()
    conn.close()


# helper method to get the database since calls are per thread,
# and everything function is a new thread when called
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# helper to close
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    cur = get_db().cursor()
    res = cur.execute("select * from users")
    return render_template("index.html", users=res)


if __name__ == "__main__":
    app.run()