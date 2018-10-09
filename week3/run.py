from utils.task1 import create_dirs, create_files, pretty_print
from utils.task2 import csv_file
from utils.task3 import save_pic

# some data for input -> task1
dir2create = ['demo_dir1', 'demo_dir2/demo_dir3', 'demo_dir4/demo_dir5/demo_dir6']
file2create = ['file1.txt', 'file2.xml', 'file3.jpeg', 'file4.sh', 'file5.pdf']

# list of members for task2
group_members = [{'First name': 'Alexandr', 'Last name': 'Klimach', 'Telegram tag': '@klimach'},
                  {'First name': 'Alexander', 'Last name': 'Kozhokar', 'Telegram tag': '@hey_alex'},
                  {'First name': 'Viktor', 'Last name': 'B.', 'Telegram tag': '@sancheezzz'},
                  {'First name': 'Roman', 'Last name': 'Rodomansky', 'Telegram tag': '@romanrodomansky'},
                  {'First name': 'Pavlo', 'Last name': 'Kandiak', 'Telegram tag': '@kandiak_ps'},
                  {'First name': 'Eugene', 'Last name': 'Zabolotny', 'Telegram tag': '@eugenezabolotny'},
                  {'First name': 'Дмитро', 'Last name': 'Bragarnik', 'Telegram tag': '@Sarbai'},
                  {'First name': 'Ostap', 'Last name': 'Rodomansky', 'Telegram tag': '@ostap_rodomansky'},
                  {'First name': 'Igor', 'Last name': 'Tagintsev', 'Telegram tag': '@Ingvar1390'},
                  {'First name': 'Maxim', 'Last name': 'Poleshko', 'Telegram tag': '@Maxsim_P'},
                  {'First name': 'Misha', 'Last name': 'Antonkin', 'Telegram tag': '@Cosmander'}]


if __name__ == "__main__":
    # creating directories and files for task1
    create_dirs(dir2create, '/tmp/demo')
    create_files(file2create, '/tmp/demo')
    # printing pretty tree for task1
    pretty_print('/tmp/demo')

    csv_file('file.csv', group_members)

    save_pic('https://dummyimage.com/600x400/000/fff', 'mypic.png')
