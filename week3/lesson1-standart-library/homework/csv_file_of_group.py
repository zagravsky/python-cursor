import csv


def csv_dict_writer(csv_path, csv_fieldnames, csv_data):
    with open(csv_path, "w", newline='') as my_file:
        writer = csv.DictWriter(my_file, delimiter=',', fieldnames=csv_fieldnames)
        writer.writeheader()
        writer.writerows(csv_data)


if __name__ == "__main__":
    members_list = ["First_name,Last_name,Telegram_tag".split(","),
            "Yevheniia,Kyryliuk,@EvgeniaCURSOR".split(","),
            "Anastasiia,Kostenko,@nastasiia_ko".split(","),
            "Дмитро,Bragarnik,@Sarbai".split(","),
            "Dasha,Homenko,@DariaHomenko".split(","),
            "Jenia,Trofimenko,@jeniaTrofimenko".split(","),
            "Ilya,Apestin,@Ilya_UA".split(",")
            ]
    my_list = []
    fieldnames = members_list[0]
    for values in members_list[1:]:
        member_dict = dict(zip(fieldnames, values))
        my_list.append(member_dict)

    my_path = "group_members.csv"
    csv_dict_writer(my_path, fieldnames, my_list)
