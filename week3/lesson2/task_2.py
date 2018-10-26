import csv
from external_list import memb_list



with open('membership.csv', 'w', newline='') as csvfile:
    fieldnames = ['First name', 'Last name', 'Telegram tag']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(memb_list)
    csvfile.close()
