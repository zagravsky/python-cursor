import csv


def create_csv (stud_list:list, doc_name:str):
    with open(doc_name + ".csv", 'w', newline='') as csv_file:
        file_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        file_writer.writerows(stud_list)

if __name__ == '__main__':

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

	create_csv(group_list,"Csv_task_2")