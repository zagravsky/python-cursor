import csv


def create_file_csv(data: dict):
    with open ('cursor.csv', 'w') as file_csv:
        fields = ['First name', 'Last name', 'Telegram tag']
        writer = csv.DictWriter(file_csv, fieldnames = fields)
        writer.writeheader()
        writer.writerows(data)
