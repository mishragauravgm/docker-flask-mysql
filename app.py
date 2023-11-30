from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db = mysql.connector.connect(
    host="mysql",
    user="root",
    password="password",
    database="users_db"
)
cursor = db.cursor()

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()

    if user:
        return "Login successful!"
    else:
        return "Login failed. Invalid username or password."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

