def func_task_6 (members:list):
    from re import findall
    members = sorted(members, key=lambda  x: (len (x['name']), x['age']))
    return members

