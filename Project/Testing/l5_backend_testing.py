import requests


def test_PostUser(userid="-1", username="test"):
    a = requests.post('http://127.0.0.1:5000/users/' + str(userid), json={'user_name': username})
    return a

def test_GetUser(userid="-1"):
    a = requests.get('http://127.0.0.1:5000/users/' + str(userid))
    return a

uid=input("enter user id: ")
uname=input("enter user name: ")

p = test_PostUser(uid,uname)
p = p.json()
p1 = p["Status"]
p2 = p["Code"]
print(str(p1)+" code: "+str(p2))

g = test_GetUser(uid)
g = g.json()
g1 = g["Status"]
g2 = g["Code"]
print(str(g1)+" code: "+str(g2))