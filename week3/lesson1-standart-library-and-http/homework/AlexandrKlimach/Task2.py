import csv


def create_csv_file(lst: list, file_name: str):
    with open(file_name + ".csv", 'w', newline='') as csv_file:
        columns = ['First name', 'Last name', 'Telegram tag']
        file_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        file_writer.writerow(column for column in columns)
        for member in lst:
            file_writer.writerow(member)


if __name__ == "__main__":
    group_list = [['Alexandr', 'Klimach', '@klimach'],
                  ['Alexander', 'Kozhokar', '@hey_alex'],
                  ['Viktor', 'B.', '@sancheezzz'],
                  ['Anton', 'Ivanov', None],
                  ['Roman', 'Rodomansky', '@romanrodomansky'],
                  ['Pavlo', 'Kandiak', '@kandiak_ps'],
                  ['Eugene', 'Zabolotny', '@eugenezabolotny'],
                  ['Дмитро', 'Bragarnik', '@Sarbai'],
                  ['Eugene', 'Semanyshyn', None],
                  ['Anton', 'Dotsenko', None],
                  ['Ruslan', 'Karelov', None],
                  ['Ostap', 'Rodomansky', '@ostap_rodomansky'],
                  ['Igor', 'Tagintsev', '@Ingvar1390'],
                  ['Maxim', 'Poleshko', '@Maxsim_P'],
                  ['Misha', 'Antonkin', '@Cosmander'],
                  ['Андрій', 'Станішевський', '@xlibchyk'],
                  ['Olga', 'Tregub', None],
                  ['Roman', 'Zhovna', None],
                  ['Yevheniia', 'Kyryliuk', '@EvgeniaCURSOR'],
                  ['Roman', 'Buryy', None],
                  ['Almost wise', 'Dragon', '@AlmostWise'],
                  ['Natali', 'Maslova', None],
                  ['Andrii', 'Homeniuk', '@AlmostWise'],
                  ['Arthur', 'Veres', '@Artooi'],
                  ['Dmytro', 'Melnyk', '@Ekut_v'],
                  ['Albert', 'Li', None],
                  ['Bohdan', 'Novakivskyy', '@AlmostWise'],
                  ['Igor', None, '@siriusnlo'],
                  ['Anna', None, None],
                  ['Igorosha', 'Prorochuk', None],
                  ['Jenia', 'Trofimenko', '@jeniaTrofimenko'],
                  ['Alina', 'Brygas', None],
                  ['Eugen', None, None]]

    create_csv_file(group_list, 'study_group_batman')
