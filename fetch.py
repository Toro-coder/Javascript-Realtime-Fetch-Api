from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask_cors import CORS, cross_origin

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_ROOT'] = '3306'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Cindy1648'
app.config['MYSQL_DB'] = 'campaigns'

mysql = MySQL(app)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/fetchUsers', methods=["POST", "GET"])
@cross_origin()
def fetchusers():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT count(id) as count FROM users')
    accounts = cursor.fetchall()
    if accounts:
        return jsonify({'users': accounts})
    else:
        return jsonify({'message': 'No sign up done'})


if __name__ == "__main__":
    app.run(debug=True)
