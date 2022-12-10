import requests
from flask import Flask, render_template, request
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

def default_page(a):
    return "<H1 id='Index'>" + str(a) + "Index Page!</H1>"


def CreateUser(id, Username):
    # Creates a new user in db
    # Establishing a connection to DB
    try:
        conn = pymysql.connect(host=dbhost, port=dbport, user=dbuser, passwd=dbpasswd, db=dbschema_name)
        conn.autocommit(True)

        # Getting a cursor from Database
        cursor = conn.cursor()

        # Inserting data into table
        cursor.execute("INSERT into " + dbschema_name + ".users (id,name) VALUES (" + id + ",'" + Username + "');")
        # get result of insert
        cursor.execute("SELECT id,name FROM "+dbschema_name+".users where  id="+id+";")
        status = cursor.fetchall()
        resultDictionary = dict((x, y) for x, y in status)
        status = resultDictionary
        status = {"status": "ok", "user_added": id}
        code=200


    except Exception as e:
        status = {"status": "error", "FailureReason": str(e)}
        code = 500
    finally:
        cursor.close()
        conn.close()
        FullStatus[0]=status
        FullStatus[1]=code
        return FullStatus

def UpdateUsername(id, Username):
    #Updates Username according to User's id in db
    try:
        conn = pymysql.connect(host=dbhost, port=dbport, user=dbuser, passwd=dbpasswd, db=dbschema_name)
        conn.autocommit(True)

        # Getting a cursor from Database
        cursor = conn.cursor()

        # Update Id Name
        cursor.execute("UPDATE "+dbschema_name+".users SET name = '"+Username+ "' WHERE id ="+id+";")

        status = {"status": "ok", "user_updated": id}
        code = 200

    except Exception as e:
        status = {"status": "error", "FailureReason": str(e)}
        code = 500
    finally:
        cursor.close()
        conn.close()
        FullStatus[0] = status
        FullStatus[1] = code
        return FullStatus

def DeleteUser(id):
    try:
        conn = pymysql.connect(host=dbhost, port=dbport, user=dbuser, passwd=dbpasswd, db=dbschema_name)
        conn.autocommit(True)
        status={}
        # Getting a cursor from Database
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM " + dbschema_name + ".users where  id=" + id + ";")
        t = cursor.fetchall()
        # resultDictionary = dict((x, y) for x, y in status)
        if (len(t) == 0):
            raise Exception('DeleteOp', 'No User ' + id + ' in Db')
        # Update Id Name
        cursor.execute("DELETE FROM " + dbschema_name + ".users  WHERE id =" + id + ";")


        status = "Success"
        status = {"status": "ok", "user_deleted": id}
        code = 200

    except Exception as e:
        status = {"status": "error", "FailureReason": str(e)}
        code = 500
    finally:
        cursor.close()
        conn.close()
        FullStatus[0] = status
        FullStatus[1] = code
        return FullStatus

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
        return render_template('PySystemMain.html')
    if request.method == 'POST':
        count = 0
        mylist = {}
        multi = request.form
        for i in multi.items():
            mylist[count] = i
            count = count + 1

        if mylist[0][0].lower() == "create":
            userid = (mylist[0][1].replace("'", ''))
            a = requests.post('http://127.0.0.1:5000/users/' + userid, json={mylist[1][0]: mylist[1][1]})
            a=a.json()
            return str(a.get('0')),a.get('1')
        elif mylist[0][0].lower() == "get":
            userid = (mylist[0][1].replace("'", ''))
            a = requests.get('http://127.0.0.1:5000/users/' + userid)
            a = a.json()
            return str(a.get('0')),a.get('1')
        elif mylist[0][0].lower() == "delete":
            userid = (mylist[0][1].replace("'", ''))
            a = requests.delete('http://127.0.0.1:5000/users/' + userid)
            a=a.json()
            return str(a.get('0')),a.get('1')
        elif mylist[0][0].lower() == "update":
            userid = (mylist[0][1].replace("'", ''))
            a = requests.put('http://127.0.0.1:5000/users/' + userid, json={mylist[1][0]: mylist[1][1]})
            a = a.json()
            return str(a.get('0')),a.get('1')
        else:
            default_page("A")


@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    users = {}
    if request.method == 'GET':
        status=GetUser(user_id)
        return status
        #return {'user_id': user_id, 'user_name': users[user_id]}, 200  # status code
    elif request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        #return response from create operation
        status = CreateUser(user_id, user_name)
        #return response to client
        return status  # status code
    elif request.method == 'DELETE':
        user = GetUser(user_id)
        if (user[0].get('user_got')):
            status = DeleteUser(user_id)
        else:
            status = {0: {"status": "error", "FailureReason": 'Delete Failed user id frggfdyd;ldf;dks'+str(user_id)+' not in db'}, 1: 500}
        # return response to client
        return status
    elif request.method == 'PUT':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        # return response from create operation
        user=GetUser(user_id)
        if(user[0].get('user_got')):
            status = UpdateUsername(user_id, user_name)
        else:
            status = {0: {"status": "error", "FailureReason": 'Update Failed user id '+str(user_id)+' not in db'}, 1: 500}
        # return response to client
        return status  # status code

app.run(host='127.0.0.1', debug=True, port=5000)
