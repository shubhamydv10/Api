from flask import Flask, request,jsonify
import mysql.connector as conn

app = Flask(__name__)
mydb = conn.connect(host="localhost" , user = "root" , passwd = "shubham1250")
cursor = mydb.cursor()

@app.route("/testdbs")
def test():
    dbs = request.args.get("dbs")
    tble = request.args.get("tble")
    cursor.execute('select * from tble')
    data= cursor.fetchall()


    return "this is my first function for get {} ".format(data)

if __name__ == "__main__":
    app.run(port=5003)