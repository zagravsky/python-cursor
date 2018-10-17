import csv
from utils.members import *

def study_group(list_memb: list):
    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'telegram_tag']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(list_memb)
