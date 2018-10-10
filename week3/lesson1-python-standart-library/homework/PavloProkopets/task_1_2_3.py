import os
import csv
import requests

# Task 1
# Usage of os module. Create a tree of directories (any depth, any names).
# Create files in some of directories (how many. and where - up to you).
# Using recursive function and os module, pretty print the tree with directory and file names.

rootDir = (r'C:\Users\Pvlo\Desktop\untitled')
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)

# Task 2
# This is a test of your googling skills :D Using csv module from Standard Library,
# create a simple csv file of your study group (field names would be "First name", "Last name", "Telegram tag").
# You need to use csv.DictWriter class. All the necessary data can be found in documentation.
# To check how the file looks - open it in excel or any similar program.

with open('simple.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name', 'Telegram tag']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans', 'Telegram tag': 'dfg'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam', 'Telegram tag': 'dfg'})

with open('simple.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# Task 3
# Using requests library, download image from this url https://dummyimage.com/600x400/000/fff
# and save it as a file on your device.

with open('newfile.jpg','wb') as target:
    a = requests.get('https://dummyimage.com/600x400/000/fff')
    target.write(a.content)

