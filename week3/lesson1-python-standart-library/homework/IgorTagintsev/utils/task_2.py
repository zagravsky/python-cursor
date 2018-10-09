import csv

def create_csv(lst: list, file_name: str):
    with open(file_name + ".csv", 'w', newline='') as csv_file:
        colums = ['First name', 'Last name', 'Telegram tag']
        file_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        file_writer.writerow(colum for colum in colums)
        for member in lst:
            file_writer.writerow(member)