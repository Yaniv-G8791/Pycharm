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
dbtbl = "dogs"
# Full status
FullStatus = {}


def default_page(a):
    return "<H1 id='Index'>" + str(a) + "Index Page!</H1>"


def CreateDog(name, age, breed):
    # Creates a new user in db
    # Establishing a connection to DB
    try:
        conn = pymysql.connect(host=dbhost, port=dbport, user=dbuser, passwd=dbpasswd, db=dbschema_name)
        conn.autocommit(True)

        # Getting a cursor from Database
        cursor = conn.cursor()
        # Inserting data into table
        cursor.execute(
            "INSERT into " + dbschema_name + "." + dbtbl + " (name,age,breed) VALUES ('" + name + "'," + age + ",'" + breed + "');")
        # get result of insert
        cursor.execute("SELECT * FROM " + dbschema_name + "." + dbtbl + " where  age=12;")
        slct = cursor.fetchall()
        count = 0
        b = {}
        for i in slct:
            b[count] = {"dogname": i[0], "dogage": str(i[1]), "dogbreed": i[2]}
            count = count + 1
        status = b
    except Exception as e:
        status = {"status": "error", "FailureReason": str(e)}
    finally:
        cursor.close()
        conn.close()

        return status


def Updatedogname(id, Username):
    # Updates Username according to User's id in db
    try:
        conn = pymysql.connect(host=dbhost, port=dbport, user=dbuser, passwd=dbpasswd, db=dbschema_name)
        conn.autocommit(True)

        # Getting a cursor from Database
        cursor = conn.cursor()

        # Update Id Name
        cursor.execute("UPDATE " + dbschema_name + ".users SET name = '" + Username + "' WHERE id =" + id + ";")

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
        status = {}
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
        # resultDictionary = dict((x, y) for x, y in status)
        # status = resultDictionary
        # status = "Success"
        if len(status) != 0:
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
        FullStatus[0] = status
        FullStatus[1] = code
        return FullStatus


def GetDogs():
    try:
        conn = pymysql.connect(host=dbhost, port=dbport, user=dbuser, passwd=dbpasswd, db=dbschema_name)
        conn.autocommit(True)

        # Getting a cursor from Database
        cursor = conn.cursor()
        # Get user details
        cursor.execute("SELECT id,name FROM " + dbschema_name + ".users where  id=" + id + ";")
        status = cursor.fetchall()
        # resultDictionary = dict((x, y) for x, y in status)
        # status = resultDictionary
        # status = "Success"
        if len(status) != 0:
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
        FullStatus[0] = status
        FullStatus[1] = code
        return FullStatus


app = Flask(__name__)


@app.route('/dogs/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def dogs():
    users = {}
    if request.method == 'GET':
        status = GetUser()
        return status
        # return {'user_id': user_id, 'user_name': users[user_id]}, 200  # status code
    elif request.method == 'POST':
        # getting the json data payload from request
        request_data = request.headers
        dogname = request_data.get('dogname')
        dogage = request_data.get('dogage')
        dogbreed = request_data.get('dogbreed')
        # treating request_data as a dictionary to get a specific value from key
        # return response from create operation
        status = CreateDog(dogname, dogage, dogbreed)

        # return response to client
        return status  # status code
    elif request.method == 'DELETE':
        user = GetUser()
        if (user[0].get('user_got')):
            status = DeleteUser()
        else:
            status = {0: {"status": "error", "FailureReason": 'Delete Failed user id frggfdyd;ldf;dks not in db'},
                      1: 500}
        # return response to client
        return status
    elif request.method == 'PUT':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        # return response from create operation
        user = GetUser()
        if (user[0].get('user_got')):
            status = Updatedogname()
        else:
            status = {0: {"status": "error", "FailureReason": 'Update Failed user id  not in db'}, 1: 500}
        # return response to client
        return status  # status code


app.run(host='127.0.0.1', debug=True, port=5002)
