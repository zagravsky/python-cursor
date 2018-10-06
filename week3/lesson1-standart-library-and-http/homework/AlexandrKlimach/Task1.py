import os


def dir_and_file(user_path: str) -> list:
    pretty_tree = []
    for dir_path, dir_names, file_names in os.walk(user_path):
        lvl_dir = dir_path.replace(user_path, '').count(os.sep)
        tab = ' ' * 4 * lvl_dir
        pretty_tree.append(tab + os.path.basename(dir_path))
        sub_tab = ' ' * 4 * (lvl_dir + 1)
        for file in file_names:
            pretty_tree.append(sub_tab + file)
    return pretty_tree


if __name__ == "__main__":
    import pprint

    path = '/home/alexandr/Task1'
    pprint.pprint(dir_and_file(path))


# https://gist.github.com/klimach/1df444d0ab316b5ffae9ea28fc91dcf0
