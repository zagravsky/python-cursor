import csv


def create_csv_file(lst: list, file_name: str):
    with open(file_name + ".csv", 'w') as csv_file:
        columns = ['First name', 'Last name', 'Telegram tag']
        file_writer = csv.DictWriter(csv_file, fieldnames=columns)
        file_writer.writeheader()
        file_writer.writerows(lst)


if __name__ == "__main__":
    group_list = [
        {'First name': 'Alexandr', 'Last name': 'Klimach', 'Telegram tag': '@klimach'},
        {'First name': 'Alexander', 'Last name': 'Kozhokar', 'Telegram tag': '@hey_alex'},
        {'First name': 'Viktor', 'Last name': 'B.', 'Telegram tag': '@sancheezzz'},
        {'First name': 'Anton', 'Last name': 'Ivanov', 'Telegram tag': None},
        {'First name': 'Roman', 'Last name': 'Rodomansky', 'Telegram tag': '@romanrodomansky'},
        {'First name': 'Pavlo', 'Last name': 'Kandiak', 'Telegram tag': '@kandiak_ps'},
        {'First name': 'Eugene', 'Last name': 'Zabolotny', 'Telegram tag': '@eugenezabolotny'},
        {'First name': 'Дмитро', 'Last name': 'Bragarnik', 'Telegram tag': '@Sarbai'},
        {'First name': 'Eugene', 'Last name': 'Semanyshyn', 'Telegram tag': None},
        {'First name': 'Anton', 'Last name': 'Dotsenko', 'Telegram tag': None},
        {'First name': 'Ruslan', 'Last name': 'Karelov', 'Telegram tag': None},
        {'First name': 'Ostap', 'Last name': 'Rodomansky', 'Telegram tag': '@ostap_rodomansky'},
        {'First name': 'Igor', 'Last name': 'Tagintsev', 'Telegram tag': '@Ingvar1390'},
        {'First name': 'Maxim', 'Last name': 'Poleshko', 'Telegram tag': '@Maxsim_P'},
        {'First name': 'Misha', 'Last name': 'Antonkin', 'Telegram tag': '@Cosmander'},
        {'First name': 'Андрій', 'Last name': 'Станішевський', 'Telegram tag': '@xlibchyk'},
        {'First name': 'Olga', 'Last name': 'Tregub', 'Telegram tag': None},
        {'First name': 'Roman', 'Last name': 'Zhovna', 'Telegram tag': None},
        {'First name': 'Yevheniia', 'Last name': 'Kyryliuk', 'Telegram tag': '@EvgeniaCURSOR'},
        {'First name': 'Roman', 'Last name': 'Buryy', 'Telegram tag': None},
        {'First name': 'Almost wise', 'Last name': 'Dragon', 'Telegram tag': '@AlmostWise'},
        {'First name': 'Natali', 'Last name': 'Maslova', 'Telegram tag': None},
        {'First name': 'Andrii', 'Last name': 'Homeniuk', 'Telegram tag': '@AlmostWise'},
        {'First name': 'Arthur', 'Last name': 'Veres', 'Telegram tag': '@Artooi'},
        {'First name': 'Dmytro', 'Last name': 'Melnyk', 'Telegram tag': '@Ekut_v'},
        {'First name': 'Albert', 'Last name': 'Li', 'Telegram tag': None},
        {'First name': 'Bohdan', 'Last name': 'Novakivskyy', 'Telegram tag': '@AlmostWise'},
        {'First name': 'Igor', 'Last name': None, 'Telegram tag': '@siriusnlo'},
        {'First name': 'Anna', 'Last name': None, 'Telegram tag': None},
        {'First name': 'Igorosha', 'Last name': 'Prorochuk', 'Telegram tag': None},
        {'First name': 'Jenia', 'Last name': 'Trofimenko', 'Telegram tag': '@jeniaTrofimenko'},
        {'First name': 'Alina', 'Last name': 'Brygas', 'Telegram tag': None},
        {'First name': 'Eugen', 'Last name': None, 'Telegram tag': None}]

    create_csv_file(group_list, 'study_group_batman')
