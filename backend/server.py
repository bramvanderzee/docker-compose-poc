from flask import request, Flask
from flask_cors import CORS, cross_origin
import mysql.connector
import time
import sys
import json

time.sleep(1)

app = Flask(__name__)
CORS(app, support_credentials=True)

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
    if not resp:
        return None
    return json.dumps(resp)

def post_user(user):
    return null

@app.route('/user/<userid>', methods=['GET'])
@cross_origin(supports_credentials=True)
def user(userid: int):
    user = get_user(userid)
    if user and user != "" and user != None:
        return user, 200
    else:
        return 'User not found', 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
