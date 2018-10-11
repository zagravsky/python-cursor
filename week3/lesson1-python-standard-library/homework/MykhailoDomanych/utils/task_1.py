import os
import pprint


def pr_list_dir(path: str):
    dir_list = []
    for root, dirs, files in os.walk(path):
        add_symbol = root.count('/')
        new_root = root.split('/')[-1]
        dir_list.append(" " * add_symbol + new_root)
        for name in files:
            dir_list.append(" " * add_symbol * 4 + " $$$ " + name)
    pprint.pprint(dir_list)




