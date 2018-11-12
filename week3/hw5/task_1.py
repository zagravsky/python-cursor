# Task 1
# Create a tree of directories (any depth, any names).
# Create files in some of directories (how many. and where - up to you).
# Using recursive function and os module, pretty print the tree with directory and file names.

>>> import os
>>> os.getcwd()
'D:\\Python'
>>> os.chdir("D:\\Python\\projects\\hw5")
>>> os.getcwd()
'D:\\Python\\projects\\hw5'
>>> os.mkdir("OStest1")
>>> os.mkdir("OStest2")
>>> os.mkdir("OStest3")
>>> os.chdir("D:\\Python\\projects\\hw5\\OStest1")
>>> f = open("test1.txt", "w+")
>>> f.close()
>>> os.chdir("D:\\Python\\projects\\hw5\\OStest2")
>>> f = open("test2.txt", "w+")
>>> f.close()
>>> os.chdir("D:\\Python\\projects\\hw5\\OStest3")
>>> f = open("test3.txt", "a+")
>>> f.close()
>>> def dir_tree(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            print(path)
        else:
            dir_tree(path)


>>> import pprint
>>> pprint.pprint(dir_tree("D:\Python\projects\hw5"))
D:\Python\projects\hw5\.idea\hw5.iml
D:\Python\projects\hw5\.idea\libraries\R_User_Library.xml
D:\Python\projects\hw5\.idea\modules.xml
D:\Python\projects\hw5\.idea\workspace.xml
D:\Python\projects\hw5\hw5
D:\Python\projects\hw5\OStest1\test1.txt
D:\Python\projects\hw5\OStest2\test2.txt
D:\Python\projects\hw5\OStest3\test3.txt