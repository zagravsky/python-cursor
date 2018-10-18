import csv

with open('group_members.csv', 'r') as csv_file:
    fieldnames = ['First name', 'Last name', 'Telegram tag']
    csv_reader = csv.DictReader(csv_file, fieldnames = fieldnames)

    with open('new_member_file.csv', 'w', newline = '') as csv_new_file:

        csv_writer = csv.DictWriter(csv_new_file, fieldnames = 
fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
