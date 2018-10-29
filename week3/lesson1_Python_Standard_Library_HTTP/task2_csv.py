import csv

data_cvs = [
    {'first_name': 'Bob', 'last_name': 'Dilan', 'telegram_tag': '@123'},
    {'first_name': 'Jhon', 'last_name': 'Carter', 'telegram_tag': '@124'},
    {'first_name': 'Luk', 'last_name': 'Radson', 'telegram_tag': '@125'}
]

def create_csv (data):
    with open('peoples.csv', 'w') as my_file:
        field_name = ['first_name', 'last_name', 'telegram_tag']
        add_data = csv.DictWriter(my_file,fieldnames=field_name)
        add_data.writeheader()
        add_data.writerows(data)

create_csv(data_cvs)