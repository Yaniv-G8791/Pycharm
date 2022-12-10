import requests


def test_Postdog(dogname="test", dogage="test",dogbreed="test"):
    if dogname == 'test':
        dogname = input("enter dog name: ")
    if dogage == 'test':
        dogage = input("enter dog age(num): ")
    if dogbreed=='test':
        dogbreed = input("enter dog breed: ")
    a = requests.post('http://127.0.0.1:5002/dogs/' , headers={'dogname': dogname,'dogage':dogage,'dogbreed':dogbreed})
    return a

def test_Getdogs():
    a = requests.get('http://127.0.0.1:5000/dogs/')
    return a

p=test_Postdog("aaa","2314","afaf")
print(p.text)