import csv


def telegram_group_csv(data: dict):
    with open('telegram_group_list.csv', 'w') as group:
        fields = ['First name', 'Last name', 'Telegram tag']
        writer = csv.DictWriter(group, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)
