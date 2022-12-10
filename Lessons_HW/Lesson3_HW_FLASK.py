from random import randint
from flask import Flask, render_template,request, url_for, jsonify
import base64
import json
app = Flask(__name__)

# accessed via <HOST>:<PORT>/get_random
@app.route('/context',methods=["GET"])
def data():
    return render_template('context.html')
@app.route('/getcontext',methods=["POST"])
def get_post():
    def base64ToString(b):
        return base64.b64decode(b).decode('windows 1255', errors='ignore')
    data = request.form.get("basedata")
    base=base64ToString(data)
    return str("the file data is:"+base),200


# using default
@app.route('/register')
def hello():
    file=open('C:/temp/1231.txt',"w")
    file.write("this blah")
    file.close()
    return 'success', 201  # status code


# accessed via <HOST>:<PORT>/welcome
@app.route("/welcome")
def welcome():
    return "<H1 id='welcome'>Welcome!</H1>", 200 # status code

@app.route("/data/2")
def BAZINGA():
    x='{"name":"","":30}'
    return "<H1 id='welcome'>BAZINGA!</H1>", 200 # status code
# host is pointing at local machine address
# debug is used for more detailed logs + hot swaping
# the desired port - feel free to change
app.run(host='127.0.0.1', debug=True, port=30000)