import requests


def test_PostUser(userid="test", username="test"):
    if userid == 'test':
        userid = input("enter user id: ")
    if username == 'test':
        username = input("enter user name: ")
    a = requests.post('http://127.0.0.1:5000/users/' + str(userid), json={'user_name': username})
    return a

def test_GetUser(userid="test"):
    if userid == 'test':
        userid = input("enter user id: ")
    a = requests.get('http://127.0.0.1:5000/users/' + str(userid))
    return a

p=test_PostUser("1213","asf")
p=p.json()
p1=p.get('0')
p2=p.get('1')
print(str(p1)+" code: "+str(p2))

g=test_GetUser(1243124)
g=g.json()
g1=g.get('0')
g2=g.get('1')
print(str(g1)+" code: "+str(g2))