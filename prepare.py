# -*- coding: utf-8 -*-
import os, sys,re,shutil
from os import chdir
 

path="./csalids_temp/"
dirs=os.listdir(path)

#将文件改名
for dir in dirs:
    newDir= os.path.join(path,dir)
    newFiles=os.listdir(newDir)
    for file in newFiles:
        #rename之前要先用chdir()函数进入到目标文件所在的路径，
        #告诉python编译器要重命名的文件在哪儿，然后才可以修改
        #改变当前工作目录到指定的路径
	old_name = file
	old_path = os.path.join(newDir,old_name)
        print(file)
        new_name = str(dir)+"_"+file
	new_path = os.path.join(newDir,new_name)
	
        os.rename(old_path,new_path)
    #print ‘-----‘
 
#将文件移动到path路径下
#print u‘移动文件‘
for dir in dirs:
    newDir=path + dir + '/'
    newFiles=os.listdir(newDir)
    for file in newFiles:
        oldFilePath=os.path.join(newDir,file)
        newFilePath=os.path.join(path,file)
        shutil.move(oldFilePath, newFilePath)#移动文件到目标路径
