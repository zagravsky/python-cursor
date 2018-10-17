import os


def make_change_dir(dir_path: str):
    os.mkdir(dir_path)
    os.chdir(dir_path)
    pass


root_dir_path = os.path.expanduser('~') + '/Test_dir_tree'
make_change_dir(root_dir_path)
for i in range(0, 3):
    make_change_dir(root_dir_path+'/Dir'+str(i))

    for _ in range(0, 2):
        file = open("file"+str(_)+".txt", "tw")
        file.close()
    make_change_dir('Sub_Dir_' + str(i))

    for _ in range(0, 3):
        file = open("file"+str(_)+"_"+str(_)+".txt", "tw")
        file.close()

print(os.path.abspath(root_dir_path))

for d_p, d_n, files in os.walk(root_dir_path):
    print(' '*len(os.path.abspath(d_p))+'/'+'-'*3, os.path.basename(d_p))
    for f in files:
        print(' '*len(d_p)+'!'+'-'*(len(os.path.basename(d_p))+4), f)
