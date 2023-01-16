import db_connector as db
from flask import Flask, request
import config as config
import os
import signal

jsoncontent = config.configjson()
Status = jsoncontent["Status"]
Reason = jsoncontent["Reason"]
code = jsoncontent["code"]
Dbstatus = jsoncontent["Dbstatus"]
fullstatus = jsoncontent["fullstatus"]
DbFailReason = jsoncontent["DbFailReason"]

app = Flask(__name__)


def validateGet(jsonstatus):
    if jsonstatus[Status] == "error":
        fullstatus[Status] = jsonstatus
        fullstatus[code] = 500
    elif jsonstatus[Status] == "ok":
        fullstatus[Status] = jsonstatus
        fullstatus[code] = 200
    else:
        fullstatus[Status] = jsonstatus
        fullstatus[Status][code] = 500
    return fullstatus

def default_page(status, id=99999, err='good'):
    if(err != 'good'):
        return "<H1 id=" + status + ">" + str(id) + "</H1></br></br<h3>Error:</h3></br><p>"+err+"</p>"
    else:
        return "<H1 id=" + status + ">" + str(id) + "</H1>"


@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        #getting user name from db
        data = db.ManageDb.GetUser(user_id)
        #validating result data (if success o failed)
        fullstatus = validateGet(data)
        #return result as json
        return fullstatus

    elif request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        #return response from create operation
        status = db.ManageDb.CreateUser(user_id, user_name)
        if(status[Status] == "ok"):
            # validate create operation
            status = db.ManageDb.GetUser(user_id)
            fullstatus = validateGet(status)
        else:
            fullstatus = validateGet(status)
        return fullstatus
        #return response to client
    elif request.method == 'DELETE':
        status = db.ManageDb.GetUser(user_id)
        if status[Status] == "ok":
            status = db.ManageDb.DeleteUser(user_id)
            fullstatus = validateGet(status)
        else:
            status[DbFailReason] = "Delete Failed User Not Found"
            fullstatus = validateGet(status)
        return fullstatus
    # return response to client
    elif request.method == 'PUT':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        # return response from create operation
        status = db.ManageDb.GetUser(user_id)
        if(status[Status] == "ok"):
            fullstatus = db.ManageDb.UpdateUsername(user_id, user_name)
        else:
            status[DbFailReason] = "Delete Failed User Not Found"
            fullstatus = validateGet(status)
            # return response to client
        return fullstatus  # status code

# accessed via <HOST>:<PORT>/get_random
# back end

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'

app.run(host='127.0.0.1', debug=True, port=5000)
