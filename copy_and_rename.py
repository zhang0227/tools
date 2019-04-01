#! /usr/bin/env python
# coding=utf-8
import os
import shutil
import time
import sys



def copy_and_rename(fpath_input, fpath_output):
    for file in os.listdir(fpath_input):
        
        oldname = os.path.join(fpath_input, file)
        newname_1 = os.path.join(fpath_output,
                                 os.path.splitext(file)[0] + "_1.txt")
        newname_2 = os.path.join(fpath_output,
                                 os.path.splitext(file)[0] + "_2.txt")
        newname_3 = os.path.join(fpath_output,
                                 os.path.splitext(file)[0] + "_3.txt")
        newname_4 = os.path.join(fpath_output,
                                 os.path.splitext(file)[0] + "_4.txt")
        newname_5 = os.path.join(fpath_output,
                                 os.path.splitext(file)[0] + "_5.txt")

        shutil.copyfile(oldname, newname_1)
        shutil.copyfile(oldname, newname_2)
        shutil.copyfile(oldname, newname_3)
        shutil.copyfile(oldname, newname_4)
        shutil.copyfile(oldname, newname_5)


if __name__ == '__main__':
    print('start ...')
    t1 = time.time() * 1000
    #time.sleep(1) #1s
    fpath_input = "D:/train/labels/"
    fpath_output = "D:/train/labels2"
    copy_and_rename(fpath_input, fpath_output)
    t2 = time.time() * 1000
    print('take time:' + str(t2 - t1) + 'ms')
    print('end.')
