>>> import csv
>>> with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name', 'telegram_tag']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first_name': 'Дмитро', 'last_name': 'Bragarnik', 'telegram_tag': '@Sarbai'})
    writer.writerow({'first_name': 'Ilya', 'last_name': 'Apestin', 'telegram_tag': '@Ilya_UA'})
    writer.writerow({'first_name': 'Roman', 'last_name': 'Tsiupka', 'telegram_tag': '@romatsp'})
    writer.writerow({'first_name': 'Alexander', 'last_name': 'Kozhokar', 'telegram_tag': '@hey_alex'})
    writer.writerow({'first_name': 'Vitalii', 'last_name': 'Kuzmynov', 'telegram_tag': '@Icet315'})

26
23
24
30
27
>>>