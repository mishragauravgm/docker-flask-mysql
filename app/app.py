from flask import Flask, jsonify
import mysql.connector


app = Flask(__name__)


def user_data():
    config = {
        #'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'users'
    }
    connection = mysql.connector.connect(**config) #connect to sql database
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT user_name, user_email FROM user_data') #fetch the entries
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


@app.route('/')
def index():
    return jsonify({'User Data': user_data()})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)