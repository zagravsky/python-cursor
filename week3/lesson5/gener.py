import os


def crate_file (filepath, name):
    file = open(filepath+'/'+name, "a")
    file.write("new file")
    file.close()


dirs = ['dir1', 'dir2', 'dir3', 'dir1/dir1_1']

n = 1

for dir in dirs:
    os.mkdir(dir)
    crate_file(os.path.abspath(dir), 'ddd'+str(n))
    n  += 1
    os.listdir(dir)
