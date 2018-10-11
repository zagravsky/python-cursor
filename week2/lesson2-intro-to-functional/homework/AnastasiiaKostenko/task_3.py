from task_1 import members

def load_key_to_dict(members:list):
    for i in members:
        load=int(i['age']*100/200)
        new_key={"load":load}
        i.update(new_key)
    print(members)

load_key_to_dict(members)

