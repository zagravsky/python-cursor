import os
import pprint


def task1(your_path: str):
    tree = []
    for path, directory, file in os.walk(your_path):
        for f in file:
            tree.append(path + '/' + f)
    return tree


pprint.pprint(task1('/home/ruslan/jupyter project'))
