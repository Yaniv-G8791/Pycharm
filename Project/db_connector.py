import pymysql
import config as config

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

def default_page(a):
    return "<H1 id='Index'>" + str(a) + "Index Page!</H1>"

class ManageDb:
    def CreateUser(userid, Username):
        # Creates a new user in db
        # Establishing a connection to DB
        try:
            conn = pymysql.connect(host=dbhost, port=dbport, user=dbuser, passwd=dbpasswd, db=dbschema_name)
            conn.autocommit(True)

            # Getting a cursor from Database
            cursor = conn.cursor()

            # Inserting data into table
            cursor.execute("INSERT into " + dbschema_name + ".users (id,name) VALUES (" + userid + ",'" + Username + "');")
            # get result of insert
            Dbstatus = {Status: "ok"}


        except Exception as e:
            Dbstatus = {Status: "error", DbFailReason: str(e)}

        finally:
            cursor.close()
            conn.close()
            return Dbstatus

    def GetUser(userid):
        try:
            conn = pymysql.connect(host=dbhost, port=dbport, user=dbuser, passwd=dbpasswd, db=dbschema_name)
            conn.autocommit(True)
            # Getting a cursor from Database
            cursor = conn.cursor()
            # Get user details
            cursor.execute("SELECT name FROM " + dbschema_name + ".users where  id=" + userid + ";")
            res = cursor.fetchall()

            if len(res[0][0]) != 0:
                Dbstatus = {Status : "ok", "Username" : res[0][0]}
            else:
                raise Exception('GetOp', 'Get User Failed User ' + str(userid) + ' does not exist in db')
        except Exception as e:
            Dbstatus = {Status: "error", DbFailReason: str(e)}
        finally:
            cursor.close()
            conn.close()
            return Dbstatus

    def UpdateUsername(userid, Username):
        #Updates Username according to User's id in db
        try:
            conn = pymysql.connect(host=dbhost, port=dbport, user=dbuser, passwd=dbpasswd, db=dbschema_name)
            conn.autocommit(True)
            # Getting a cursor from Database
            cursor = conn.cursor()
            # Update Id Name
            cursor.execute("UPDATE "+dbschema_name+".users SET name = '"+Username+ "' WHERE id ="+userid+";")
            Dbstatus = {Status: "ok"}
        except Exception as e:
            Dbstatus = {Status: "error", "reason": str(e)}
        finally:
            cursor.close()
            conn.close()
            return  Dbstatus

    def DeleteUser(userid):
        try:
            conn = pymysql.connect(host=dbhost, port=dbport, user=dbuser, passwd=dbpasswd, db=dbschema_name)
            conn.autocommit(True)
            Dbstatus={}
            # Getting a cursor from Database
            cursor = conn.cursor()
            cursor.execute("DELETE FROM " + dbschema_name + ".users  WHERE id =" + userid + ";")
            Dbstatus = {Status: "ok"}

        except Exception as e:
            Dbstatus = {Status: "error", DbFailReason: str(e)}
        finally:
            cursor.close()
            conn.close()
            return Dbstatus


