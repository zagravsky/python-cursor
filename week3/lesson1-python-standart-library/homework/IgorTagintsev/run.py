from utils.task_1 import dir_and_files
from utils.task_2 import create_csv
import requests

#Task_1
if __name__ == "__main__":
    dir_path = "/home/igor/Git/week_3_lesson_1_igor_tagintsev/task1"
    dir_and_files(dir_path)
#Result :  https://gist.github.com/IgorTagintsev/5c3f7ee09350a1c4a27df4192b6def9c
#Task_2
if __name__ == "__main__":
    list_of_members = [['Alexandr', 'Klimach', '@klimach'],
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

    create_csv(list_of_members, 'batman')

#Task_3
url = "https://dummyimage.com/600x400/000/fff"
response = requests.get(url)
if response.status_code == 200:
    with open("/home/igor/Git/SLandHTTP/image.png", 'wb') as f:
        f.write(response.content)