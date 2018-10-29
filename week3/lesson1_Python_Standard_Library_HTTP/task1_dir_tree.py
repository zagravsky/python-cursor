
import os
path = '/home/body/git/python-cursor/week3'
def iter_path (path,level = '|--'):
    global files
    try:
        files = os.listdir(path)
        for name in files:
            if os.path.isdir(os.path.join(path, name)):
                print(level, name)

                files = iter_path(os.path.join(path, name), level = level + '----')
            else:
                print(level, name)
        return files
    except NotADirectoryError:
        pass
if __name__ == '__main__':
    iter_path(path)



