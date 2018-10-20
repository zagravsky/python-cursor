from utils.task_1 import dir_files
from utils.task_2 import create_file_csv
from utils.task_3 import save_data


if __name__ == "__main__":

    # Task_1
    dir_path = "/home/holly/Projects/hw5"
    dir_files(dir_path)

    # Task_2
    cursor_group = [
        {'First name': 'Arthur', 'Last name': 'Veres', 'Telegram tag': '@Artooi'},
        {'First name': 'Alexander', 'Last name': 'Kozhokar', 'Telegram tag': '@hey_alex'},
        {'First name': 'Pavlo', 'Last name': 'Kandiak', 'Telegram tag': '@kandiak_ps'},
        {'First name': 'Volodymyr', 'Last name': 'Laško', 'Telegram tag': None},
        {'First name': 'Misha', 'Last name': 'Antonkin', 'Telegram tag': '@Cosmander'},
        {'First name': 'Roman', 'Last name': 'Zolotukha', 'Telegram tag': None},
        {'First name': 'Viktor', 'Last name': 'B.', 'Telegram tag': '@sancheezzz'},
        {'First name': 'Ostap', 'Last name': 'Rodomansky', 'Telegram tag': '@ostap_rodomansky'},
        {'First name': 'Almost', 'Last name': 'wise Dragon', 'Telegram tag': '@AlmostWise'},
        {'First name': 'Eugene', 'Last name': 'Zabolotny', 'Telegram tag': '@eugenezabolotny'},
        {'First name': 'Alexandr', 'Last name': 'Klimach', 'Telegram tag': '@klimach'},
        {'First name': 'Roman', 'Last name': 'Rodomansky', 'Telegram tag': '@romanrodomansky'},
        {'First name': 'Yevheniia', 'Last name': 'Kyryliuk', 'Telegram tag': '@EvgeniaCURSOR'},
        {'First name': 'Anna', 'Last name': None, 'Telegram tag': None},
        {'First name': 'Igor', 'Last name': 'Tagintsev', 'Telegram tag': '@Ingvar1390'},
        {'First name': 'Albert', 'Last name': 'Li', 'Telegram tag': None},
        {'First name': 'Anton', 'Last name': 'Ivanov', 'Telegram tag': '@Aersum'},
        {'First name': 'Bohdan', 'Last name': 'Novakivskyy', 'Telegram tag': None},
        {'First name': 'Olga', 'Last name': 'Tregub', 'Telegram tag': '@HollyTregy'},
        {'First name': 'Ruslan', 'Last name': 'Karelov', 'Telegram tag': None},
        {'First name': 'Андрій', 'Last name': 'Станішевський', 'Telegram tag': '@xlibchyk'},
        {'First name': 'Roman', 'Last name': 'Zhovna', 'Telegram tag': None},
        {'First name': 'Roman', 'Last name': 'Buryy', 'Telegram tag': None},
        {'First name': 'Maxim', 'Last name': 'Poleshko', 'Telegram tag': '@Maxsim_P'},
        {'First name': 'Eugene', 'Last name': 'Semanyshyn', 'Telegram tag': None},
        {'First name': 'Eugen', 'Last name': None, 'Telegram tag': None},
        {'First name': 'Andrii', 'Last name': 'Homeniuk', 'Telegram tag': None},
        {'First name': 'Andriy', 'Last name': 'Furhalo', 'Telegram tag': None},
        {'First name': 'Mykhailo', 'Last name': None, 'Telegram tag': None},
        {'First name': 'Igor', 'Last name': None, 'Telegram tag': '@siriusnlo'},
        {'First name': 'Jenia', 'Last name': 'Trofimenko', 'Telegram tag': '@jeniaTrofimenko'},
        {'First name': 'Igorosha', 'Last name': 'Prorochuk', 'Telegram tag': None}]

    create_file_csv(cursor_group)

    # Task 3
    save_data('https://dummyimage.com/600x400/000/fff')



