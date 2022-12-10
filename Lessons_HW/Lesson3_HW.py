# -*- coding: utf-8 -*-
def pause():
    import os
    os.system("pause")


COUNT = 1
print(str(COUNT) +" and 2"+ " EXCERSIZE START")
try:
    A=1/0;
except Exception as e:
    print("operation failed error:\n "+str(e))
print("EXCERSIZE END")
pause()
COUNT = COUNT + 2
print(str(COUNT) + " EXCERSIZE START")
print("No Finall in Try block should be in the same line as Try")
print("EXCERSIZE END")
pause()
COUNT = COUNT+4
print(str(COUNT) + " EXCERSIZE START")
#write to file
print("זהו משפט ניסיון")
file=open("c:\\temp\\word.txt", 'w',encoding="windows 1255")
file.write("אדשגשדרא")
file.close()
#read from file
file=open("c:\\temp\\word.txt", encoding="windows 1255")
line=file.readline()
print(str(line))
file.close()

print(str(COUNT) + " EXCERSIZE END")

