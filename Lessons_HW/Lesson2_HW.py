def pause():
    import os
    os.system("pause")


COUNT = 1
print(str(COUNT) + " EXCERSIZE START")
X = '6a'
Y = 6

if type(X) == int and type(Y) == int:
    if X > Y:
        print("BIG")
    elif X == Y:
        print("undefined")
    else:
        print("small")
else:
    print(str(X) + " or " + str(Y) + " are not integers")

print(str(COUNT) + " EXCERSIZE END")
pause()
COUNT = COUNT + 1
print(str(COUNT) + " EXCERSIZE START")

for i in range(6):
    print(str(i))
print(str(COUNT) + " EXCERSIZE END")

pause()
COUNT = COUNT + 1
print(str(COUNT) + " EXCERSIZE START")

def valid_third_ex(var):
    if type(int(var)) == int:
        var = int(var)
        if var <= 0 or var >= 5:
            pass
        else:
            return var
    else:
        return str(var) + " is not an integer"

dict = {"1" : "fall", "2": "spring", "3": "winter", "4": "summer"}
for i in dict.keys():
    d = valid_third_ex(i)
    if type(d) == int:
        print("the value for " + str(i) + " is " + str(dict[i]))
    else:
        print(d)
print(str(COUNT) + " EXCERSIZE END")
pause()
COUNT = COUNT + 1
print(str(COUNT) + " EXCERSIZE START")
print("loop will run 10 times, last number printer is 10 because counter is updated to 11 at the end of the loop")

print(str(COUNT) + " EXCERSIZE END")
pause()
COUNT = COUNT + 1
print(str(COUNT) + " EXCERSIZE START")
dict = {"Age": "31", "F_l": "Y", "ShekelDoll_xch": "3.5", "Abroad": "True", "aprtnum": "38"}
print(dict.values())
dict["Age"] = str(float(dict["Age"]) + float(dict["ShekelDoll_xch"]))
print(dict.values())

print(str(COUNT) + " EXCERSIZE END")
pause()
COUNT = COUNT + 1
print(str(COUNT) + " EXCERSIZE START")
phone=input("Enter your phone number here: ")
print("phone number"+str(phone))
print(str(COUNT) + " EXCERSIZE END")
pause()
COUNT = COUNT + 1
print(str(COUNT) + " EXCERSIZE START")

def printhello():
    print("hello")

def calculate():
    return 5+3.2

printhello()
print(calculate())
print(str(COUNT) + " EXCERSIZE END")
pause()
COUNT = COUNT + 1
print(str(COUNT) + " EXCERSIZE START")
def printname(name):
    if type(name) == str:
        print(str(name))

def calculate(num):
    if type(num) == int or type(num) == float:
        print((num/2))

name = "yaniv"
number = 1232.2
printname(name)
calculate(number)

print(str(COUNT) + " EXCERSIZE END")
pause()
COUNT = COUNT + 1
print(str(COUNT) + " EXCERSIZE START")

def add_numbers(num1,num2):
    if (type(num1) == int or type(num1) == float) and (type(num2) == int or type(num2) == float):
        return num1+num2

def add_strings(str1,str2):
    if (type(str1) == str) and (type(str2) == str):
        return str1 + " " + str2

n1=123
n2=325
s1="foo"
s2="bar"
resN=add_numbers(n1,n2)
resS=add_strings(s1,s2)
print(resN)
print(resS)

print(str(COUNT) + " EXCERSIZE END")

pause()
COUNT = COUNT + 1
print(str(COUNT) + " EXCERSIZE START")
numberarray=[11,23,242]
for i in numberarray:
    print(i)
print(str(COUNT) + " EXCERSIZE END")

pause()
COUNT = COUNT + 1
print(str(COUNT) + " EXCERSIZE START")
numberarray=[11,23,242]
k=0
for i in numberarray:
    k=k+i
print(k)
print(str(COUNT) + " EXCERSIZE END")
pause()
COUNT = COUNT + 1
print(str(COUNT) + " EXCERSIZE START")
dict = {"Age": "31", "F_l": "Y", "ShekelDoll_xch": "3.5", "Abroad": "True", "aprtnum": "38"}
for i in dict.keys():
    print(i)
print(str(COUNT) + " EXCERSIZE END")

pause()
COUNT = COUNT + 1
print(str(COUNT) + " Challenge START")
n=7
for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end="")
    print("\r")

print(str(COUNT) + " Challenge END")

pause()
COUNT = COUNT + 1
print(str(COUNT) + " Challenge START")
N = 50

for i in range(N):
    for j in range(N):
        if (i == j) or ((N - j -1) == i):
            print('*',end='')
        else:
            print(' ',end='')
    print('')

print(str(COUNT) + " Challenge END")

pause()
COUNT = COUNT + 1
print(str(COUNT) + " Challenge START")
def get_input_number():
    num1 = input("hello enter a number please ")
    try:
        if(type(int(num1)) == int):
            return num1
    except ValueError:
        print("ERROR:"+str(num1)+"Input is not a NUMBER")
        return 0

def split_multidigit_and_sum(b):
    my_list = [int(x) for x in str(b)]
    k=0
    for i in my_list:
       k=k+i
    return k

b = get_input_number()
d = split_multidigit_and_sum(b)
print(d)
print(str(COUNT) + " Challenge END")

pause()
COUNT = COUNT + 1
print(str(COUNT) + " Challenge START")
tup = ('h', 'e', 'l', 'l', 'o')
k=''
for i in tup:
    k=k+i
print(k)
print(str(COUNT) + " Challenge END")

pause()
COUNT = COUNT + 1
print(str(COUNT) + " Challenge START")
tup = ('1','2','2','3','2','3','24','23','5','2','6','34','74','57','856','8','79','34','56','34','74','6','65','89','4','35','423','5','213','52','43','24','312','43','25','423','6','53','74','68','64','23','4','234','14211234','3446','362346')
k=0
for i in tup:
    i=int(i)
    if k < i:
       res=k
    else:
        k=i
print("got lowest number: "+str(k))
print(str(COUNT) + " Challenge END")
