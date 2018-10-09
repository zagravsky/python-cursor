import csv


def csv_file(name: str, l: list):
    with open(name, 'w', newline='') as myfile:
        columns = ['First name', 'Last name', 'Telegram tag']
        writer = csv.DictWriter(myfile, fieldnames=columns)

        writer.writeheader()
        for e in l:
            writer.writerow(e)
