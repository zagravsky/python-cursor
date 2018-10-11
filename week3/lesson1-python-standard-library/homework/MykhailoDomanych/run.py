from utils.task_1 import pr_list_dir
from utils.task_2 import telegram_group_csv
from utils.task_3 import get_img
from utils.telegram_group_data import telegram_group_data
import requests


if __name__ == "__main__":
    # Task_1
    dir_path = "/Users/user/PycharmProjects/python-cursor/week3/lesson1-python-standard-library/homework/MykhailoDomanych/utils/test_dir"
    pr_list_dir(dir_path)

    #Task_2
    telegram_group_csv(telegram_group_data)
    #Task 3
    url = "https://dummyimage.com/600x400/000/fff"
    get_img(url)
