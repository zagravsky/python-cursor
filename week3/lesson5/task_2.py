import csv



def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line["first_name"]+line["last_name"]+line["Telegram_tag"]),

def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "a") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


new_students=[
    ['Dmytro', 'Melnyk', '@Ekut_v'],
    ['Andrii', 'Tsybulskyi', '@ants_ua']
]

if __name__ == "__main__":
    csv_writer(new_students, "students.csv")
    with open("students.csv") as f_obj:

        csv_dict_reader(f_obj)

