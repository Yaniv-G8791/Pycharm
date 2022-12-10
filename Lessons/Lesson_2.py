import datetime

print(datetime.datetime.now())

def get_one():
    a = 2
    b = 5
    c = a * b
    return c * 4

def print_name(name):
    print(name)


def return_name(name):
    return "hello " + name

this_is_a_test=return_name("nnnnn")
print_name(this_is_a_test)



def simple_fun():
    import time
    yield 1
    time.sleep(1)
    yield 2


#for v in simple_fun():
#    print(v)



a = [2,"a",True,1,21,24,12,412,4,12,41,53213,3523,5,23,5,23,35,32,5,23,5,3234]
flag=False
count=len(a)
while flag != True:
    a.pop(0)
    print(len(a))
    count = count-1
    if(count == 1):
        flag=True


KEY={"A":1,"B":2,"C":3,"D":4,"E":["T","Y"]}
print(KEY.values())
print(KEY.keys())
print(KEY["E"])