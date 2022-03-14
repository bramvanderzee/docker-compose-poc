from flask import request, Flask
import mysql.connector
import time

time.sleep(1)

app = Flask(__name__)

db = mysql.connector.connect(
    host="db",
    user="root",
    password="root",
    database="db",
)

cursor = db.cursor()

def get_user(userid: int):
    global cursor
    cursor.execute("SELECT * FROM Users WHERE id = '" + userid + "';")
    return cursor.fetchall()[0]

def post_user(user):
    return null

@app.route('/user/<userid>', methods=['GET'])
def user(userid: int):
    return get_user(userid)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
