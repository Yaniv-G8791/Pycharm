count=0
test="DATA_"
import flask
try:
    file = open("c:/temp/1231231.txt", 'r')
    while(count < 200):
        count=count+1
        file.write(test+str(count)+" \n")
    file=open("c:/temp/1231231.txt",'r')
    print(file.read())

except ExceptionGroup:
    print("This is an Error")
    raise NameError('AAAAAAAAAAAHHHHHHHHHHH IM AN ERRORROROROROROORORR')

else:
    file.close()
