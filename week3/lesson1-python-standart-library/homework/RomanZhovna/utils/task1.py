import os
import random


def create_dirs(l: list, p: str):
    os.makedirs(p)
    os.chdir(p)
    for d in l:
        os.makedirs(d)


def create_files(l: list, p: str):
    for d in os.listdir(p):
        c = random.choice(range(1, 6))
        while c > 0:
            f = open(os.path.join(d, random.choice(l)), "w")
            f.close()
            c -= 1


def pretty_print(p: str, ind=0):
    print((u'\u2503' + ' ') * ind + u'\u2523' + os.path.basename(p))
    if os.path.isdir(p):
        for f in os.listdir(p):
            pretty_print(os.path.join(p, f), ind+1)
