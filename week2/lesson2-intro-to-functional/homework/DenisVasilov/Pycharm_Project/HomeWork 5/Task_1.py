import os

def dir_and_file(user_path: str) -> list:
    tree = []
    for dir_path, dir_names, file_names in os.walk(user_path):
        lvl_dir = dir_path.replace(user_path, '').count(os.sep)
        tab = " " * 4 * lvl_dir
        tree.append(tab + os.path.basename(dir_path))
        sub_tab = ' ' * 4 * (lvl_dir + 1)
        for file in file_names:
            tree.append(sub_tab + file)
    return tree
if __name__ == "__main__":
    import pprint
    path = 'C:/Users/SancheeZzz/PycharmProjects/CURSOR/SancheeZzz'
    pprint.pprint(dir_and_file(path))
	