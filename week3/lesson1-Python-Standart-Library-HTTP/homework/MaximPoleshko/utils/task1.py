import os
import pprint

def make_dirs(dirs):
    if not "first" in os.listdir():
        os.makedirs(dirs, exist_ok=True)

def dir_tree_func(path: str):
    tree_dirs = []
    for root, dirs, files in os.walk(path):
        space = root.count('/')
        spl = root.split('/')[-1]
        tree_dirs.append(" " * space + "| " + spl)
        for name in files:
            tree_dirs.append(" " * space * 2 + "| " + name)
    pprint.pprint(tree_dirs)





