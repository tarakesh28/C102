import os
import shutil

from_dir = "E:\C102"
to_dir = "E:\Asset102"

list_of_files = os.listdir(from_dir)

print(list_of_files)


for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)
    if extension == '':
        continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "image"
        path3 = to_dir + '/' + "image" + '/' + file_name
        #print(path1)
        #print(path2)
        if os.path.exists(path2):
            print('Moving file'+file_name+'...')    
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)    
            print('Moving file'+file_name+'...')    
            shutil.move(path1,path3)