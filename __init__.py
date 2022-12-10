def get_current_dir(dirs):
    import os
    return os.listdir(dirs)

def copy_music(song):
    import shutil
    shutil.copy(song , "C:\\music2\\")

def backup_song(song)
    # test if song with same name exists in folder


d = "C:\\Music\\"
a = get_current_dir(d)
print(a)
for file in a:
    m = d + file
    print(m)
    copy_music(m)

# for x in range(3, 100, 2):
#    print(x)

# MAX = 5
# count = 0
# while count < MAX:
#    print(count)
#    count += 1

# count = 0
# while 1 > 1:
#    print(count)
#    break
#    if (count >= 5):
#        pass



