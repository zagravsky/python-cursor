import os
import pprint

def dir_and_files(dir_path: str):
    list_dir = []
    for root, dirs, files in os.walk(dir_path):
        some_space = root.count('/')
        new_root = root.split('/')[-1]
        list_dir.append(" " * some_space + new_root)
        for name in files:
            list_dir.append(" " * some_space * 3 + "└── " + name)
    pprint.pprint(list_dir)