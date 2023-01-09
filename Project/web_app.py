from flask import Flask, request, render_template, redirect
import config as config
import db_connector as db

jsoncontent=config.configjson()

##DB STATIC PARAMS
dbhost = jsoncontent["dbhost"]
dbschema_name = jsoncontent["dbschema_name"]
dbport = jsoncontent["dbport"]
dbuser = jsoncontent["dbuser"]
dbpasswd = jsoncontent["dbpasswd"]
dbdb = jsoncontent["dbdb"]
#Full status
Status = jsoncontent["Status"]
Reason = jsoncontent["Reason"]
code = jsoncontent["code"]
Dbstatus = jsoncontent["Dbstatus"]
DbFailReason = jsoncontent["DbFailReason"]
fullstatus = jsoncontent["fullstatus"]

def default_page(status, id='99999', err='good'):
    if(err != 'good'):
        return "<H1 id=" + status + ">" + id + "</H1></br></br<h3>Error:</h3></br><p>"+err+"</p>"
    else:
        return "<H1 id=" + status + ">" + id + "</H1>"

app = Flask(__name__)


# accessed via <HOST>:<PORT>/get_random
# back end
@app.route('/')
def index():
    return redirect("/users/",302)

@app.route('/users/get_user_data/<user_id>', methods=['GET','POST'])
def user(user_id):
    users = {}
    if request.method == 'GET':
        if user_id == "-1":
            return "<H1 id='user'>enter a valid user id instead of -1 in end of url</H1>"
        else:
            status = db.ManageDb.GetUser(user_id)
            if status[Status] == 'ok' :
                return default_page('user', user_id, user_id), 200
            elif status[Status] == 'error' :
                return default_page('error', user_id, status[DbFailReason]), 500
            else:
                return default_page('error', user_id, "Undefined"), status[1]
    if request.method == 'POST':
        if user_id == "-1":
            return "<H1 id='user'>enter a valid user id instead of -1 in end of url</H1>"
        else:
            status=db.ManageDb.GetUser(user_id)
            if status[Status] == 'ok' :
                return default_page('user',user_id), 200
            elif status[Status] == 'error' :
                return default_page('error',user_id, status[DbFailReason]), 500
            else:
                return default_page('error',user_id, "Undefined"), status[1]

@app.route('/users/', methods=['GET'])
def webui():
    if request.method == 'GET':
        return render_template("PySystemMainFront.html")

app.run(host='127.0.0.1', debug=True, port=5001)
