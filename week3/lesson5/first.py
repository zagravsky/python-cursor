import os

mypath = '/home/silver/Desktop/HW/python-cursor/week3/'

def print_all(path):
    for d in os.listdir(path):
        t= os.path.join(path, d)
        if os.path.isdir(t):
            print(os.path.abspath(t)+':')
            print('---'+ str(os.listdir(os.path.abspath(t))))
            print_all(os.path.abspath(t+'/'))
            pass
    return




print("start")
print_all(mypath)
print("finish")
