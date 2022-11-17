from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
from flask_mysqldb import MySQL
import MySQLdb.cursors
import webbrowser
import uuid
import re

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_ROOT'] = '3306'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Cindy1648'
app.config['MYSQL_DB'] = 'hostels'

mysql = MySQL(app)


@app.route('/signups', methods=["POST", "GET"])
def signUps():
    _json = request.json
    _first_name = _json['first_name']
    _last_name = _json['last_name']
    _username = _json['username']
    _email = _json['email']
    _passw = _json['passw']
    _confirm_passw = _json['confirm_passw']
    token = str(uuid.uuid4())

    if _first_name and _last_name and _username and _email and _passw and _confirm_passw and token:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO register VALUES(NULL, % s, % s, % s, % s, % s, % s, % s)',
                        (_first_name, _last_name, _username, _email, _passw, _confirm_passw, token))
        conn = mysql.connection.commit()
        for i in conn:
            conn += i
        return render_template("card.html")

if __name__ == "__main__":
    app.run(debug=True)
