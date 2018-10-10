import csv

def create_csv(data: dict):
    with open('batman.csv', 'w') as csv_file:
        columns = ['First name', 'Last name', 'Telegram tag']
        writer = csv.DictWriter(csv_file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(data)