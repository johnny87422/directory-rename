import csv
import os

def scan_root_dir():
    data_dirs = []
    for item in os.listdir('.'):
        if (os.path.isdir(item)):
            if (item[:1] != '.'):
                data_dirs.append(os.path.abspath(os.path.join(os.getcwd(), item)))
    return data_dirs

dirlist=[]
with open('test.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    for i in rows:
        dirlist.append(i)
        
for i in dirlist:
    print(i)

for i in range(len(dirlist)):
    if i == len(dirlist)-1:
        break
    if dirlist[i] == [] or dirlist[i] == None:
        continue
    try:
        for j in range(0,len(dirlist[i]),2):
            if dirlist[i][j+1] ==  dirlist[i+1][j+1]:
                dirlist[i+1][j] = dirlist[i][j+1]
    except:
        pass
    
for i in dirlist:
    print(i)



rootstr =''
data_dir = scan_root_dir()
data_dir = data_dir[0]
#print(data_dir)


for i in range(len(dirlist)):
    if dirlist[i] == []:
        continue
    if dirlist[i][0] == '':
        continue
    for j in range(0,len(dirlist[i]),2):
        if dirlist[i][j] == '':
            break
        print("before dir ="+data_dir)
        for index, dir_info in enumerate(os.walk(data_dir)):
            print(dir_info[1])
            for  name in dir_info[1]:
                if name == dirlist[i][j]:
                    print("before ="+data_dir+"\\"+name,data_dir)
                    print("after = "+data_dir+"\\"+dirlist[i][j+1])
                    os.rename(data_dir+"\\"+name,data_dir+"\\"+dirlist[i][j+1])
                    try:
                        if dirlist[i][j+2] == '':
                            break
                        data_dir = data_dir+"\\"+dirlist[i][j+1]
                        print("after dir = "+data_dir)
                        break
                    except:
                        print("no after")
                        break
            print()
            break
    data_dir = scan_root_dir()
    data_dir = data_dir[0]









                        
            

            

