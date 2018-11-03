import csv

with open('study_group.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name', 'Telegram tag']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Ostap',
                     'last_name': 'Rodomansky',
                     'Telegram tag': '@ostap_rodomansky'})
    writer.writerow({'first_name': 'Almost wise',
                     'last_name': 'Dragon',
                     'Telegram tag': '@AlmostWise'})
    writer.writerow({'first_name': 'Yevheniia',
                     'last_name': 'Kyryliuk',
                     'Telegram tag': '@EvgeniaCURSOR'})
