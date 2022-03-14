from flask import request, Flask
import mysql.connector
import time
import sys
import json

time.sleep(1)

app = Flask(__name__)
HOST = sys.argv[1] if len(sys.argv) > 1 else 'db'

db = mysql.connector.connect(
    host=HOST,
    user="root",
    password="root",
    database="db",
)

cursor = db.cursor()

def get_user(userid: int):
    global cursor
    cursor.execute("SELECT * FROM Users WHERE id = '" + userid + "';")
    resp = cursor.fetchone()
    return json.dumps(resp)

def post_user(user):
    return null

@app.route('/user/<userid>', methods=['GET'])
def user(userid: int):
    return get_user(userid)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
