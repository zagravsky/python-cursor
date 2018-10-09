import csv

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

file = open('test.csv', 'w')
fieldname = ['First name', 'Last name', 'Telegram tag']
group_dict = [dict(zip(fieldname, i)) for i in group_list]
writer = csv.DictWriter(file, fieldname)
writer.writeheader()
writer.writerows(group_dict)
file.close()