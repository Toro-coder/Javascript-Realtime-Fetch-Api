from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask_cors import CORS, cross_origin

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'locahost'
app.config['MYSQL_ROOT'] = '3306'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'xyz'
app.config['MYSQL_DB'] = ''

mysql = MySQL(app)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/fetchUsers/', methods=["POST", "GET"])
@cross_origin()
def fetchusers():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # fetching total users
    cursor.execute('SELECT count(id) as total FROM users')
    accounts = cursor.fetchall()
    accounts = accounts[0]
    for key, value in accounts.items():
        accounts = value
    # fetching weekly users
    cursor.execute('SELECT count(id) as weekly FROM users WHERE created_on > current_date - INTERVAL (WEEKDAY('
                   'current_date())) DAY')
    weekly = cursor.fetchall()
    weekly = weekly[0]
    for key, value in weekly.items():
        weekly = value

    if accounts and weekly:
        users = accounts, weekly
        return jsonify({'users': users})
    else:
        return jsonify({'message': 'No sign up done'})

@app.route('/gender', methods=['POST', 'GET'])
def gender():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT gender, count(id) as total FROM users WHERE gender !="none" GROUP BY gender')
    gender = cursor.fetchall()
    gender2 = []
    # looping through the list
    for i in gender:
        gender = list(i.values())
        gender2.append(gender)
    if gender2:
        return jsonify({'users': gender2})
    else:
        return jsonify({'message': 'error'})

@app.route('/countyusers', methods=['POST', 'GET'])
def countyusers():
    # fetching total number of users per county
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT location, count(id) as count FROM users WHERE location != "none" GROUP BY location')
    countyusers = cursor.fetchall()
    test = []
    # looping through the list
    for x in countyusers:
        list_of_the_values = list(x.values())
        test.append(list_of_the_values)

    if test:
        return jsonify({'users': test})
    else:
        return jsonify({'message': 'error'})


@app.route('/age_range', methods=['POST', 'GET'])
def age_range():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # fetching users according to age range
    cursor.execute('SELECT CASE WHEN age BETWEEN 18 and 25 THEN "18-25" '
                   'WHEN age BETWEEN 26 and 30 THEN "26-30"'
                   'WHEN age BETWEEN 30 and 35 THEN "30-35"'
                   'WHEN age BETWEEN 36 and 40 THEN "36-40"'
                   'WHEN age BETWEEN 40 and 50 THEN "40-50"'
                   'WHEN age BETWEEN 50 and 60 THEN "50-60"'
                   'WHEN age >= 61 THEN "Above 60"'
                   'END as RANGE_AGE,'
                   'count(id) as total_users '
                   'FROM users WHERE age != "null" group by RANGE_AGE order by RANGE_AGE')
    age_range = cursor.fetchall()
    age_list = []
    # looping through the list
    for age_value in age_range:
        age_range = list(age_value.values())
        age_list.append(age_range)
    if age_list:
        return jsonify({'users': age_list})
    else:
        return jsonify({'message': 'error'})


if __name__ == "__main__":
    app.run(debug=True)
