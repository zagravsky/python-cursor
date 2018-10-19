def sum_young_old(members_list):
    tatal_info = []
    tatal_info.append(sum(list(map(lambda x: x["age"],members_list))))
    young_param =min(list(map(lambda x: x['age'],members_list)))
    old_param =max(list(map(lambda x: x['age'],members_list)))
    tatal_info.__iadd__(list(filter(lambda x: x['age'] == young_param,members_list)))
    tatal_info.__iadd__(list(filter(lambda x: x['age'] == old_param,members_list)))
    return tatal_info

