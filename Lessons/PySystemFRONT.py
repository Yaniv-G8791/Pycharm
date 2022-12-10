import requests
from flask import Flask, render_template, request,redirect
import pymysql
from selenium import webdriver

##DB STATIC PARAMS
dbhost = 'sql.freedb.tech'
dbschema_name = 'freedb_Yaniv_DB'
dbport = 3306
dbuser = 'freedb_Yaniv'
dbpasswd = '!Q4QHwpt$SSzZbp'
dbdb = "freedb_Yaniv_DB"
#Full status
FullStatus={}

def default_page(status, id=99999, err='good'):
    if(err != 'good'):
        return "<H1 id=" + status + ">" + id + "</H1></br></br<h3>Error:</h3></br><p>"+err+"</p>"
    else:
        return "<H1 id=" + status + ">" + id + "</H1>"

def GetUser(id):
    try:
        conn = pymysql.connect(host=dbhost, port=dbport, user=dbuser, passwd=dbpasswd, db=dbschema_name)
        conn.autocommit(True)

        # Getting a cursor from Database
        cursor = conn.cursor()
        # Get user details
        cursor.execute("SELECT id,name FROM " + dbschema_name + ".users where  id=" + id + ";")
        status = cursor.fetchall()
        #resultDictionary = dict((x, y) for x, y in status)
        #status = resultDictionary
        #status = "Success"
        if len(status) !=0:
            status = {"status": "ok", "user_got": id}
            code = 200
        else:
            raise Exception('GetOp', 'Get User Failed User ' + str(id) + ' does not exist in db')



    except Exception as e:
        print(e)
        status = {"status": "error", "FailureReason": str(e)}
        code = 500
    finally:
        cursor.close()
        conn.close()
        FullStatus[0]=status
        FullStatus[1]=code
        return FullStatus

app = Flask(__name__)


# accessed via <HOST>:<PORT>/get_random
# back end
@app.route('/')
def index():
    if request.method == 'GET':
        return default_page()


@app.route('/users/', methods=["GET", "POST"])
def data():
    if request.method == 'GET':

        return render_template('PySystemMainFront.html')
    if request.method == 'POST':
        count = 0
        mylist = {}
        multi = request.form
        for i in multi.items():
            mylist[count] = i
            count = count + 1

    if mylist[0][0].lower() == "get":
         userid = (mylist[0][1].replace("'", ''))
         return redirect('/users/get_user_data/'+userid)


@app.route('/users/get_user_data/<user_id>', methods=['GET'])
def user(user_id):
    users = {}
    if request.method == 'GET':
        status=GetUser(user_id)
        if status[0].get('status') == 'ok' :
            return default_page('user',user_id),status[1]
        elif status[0].get('status') == 'error':
            return default_page('error', user_id, status[0].get('FailureReason')),status[1]
        else:
            return default_page('error',"","Undefined"),status[1]
        #return {'user_id': user_id, 'user_name': users[user_id]}, 200  # status code


app.run(host='127.0.0.1', debug=True, port=5001)
