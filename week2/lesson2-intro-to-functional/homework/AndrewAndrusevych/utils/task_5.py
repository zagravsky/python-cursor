def get_summery_age_youngest_and_oldest_member(members_list: list):
    return __get_summery_age(members_list),__get_youngest_member(members_list),__get_oldest_member(members_list)
def __get_summery_age(members_list:list):
    result = 0
    for member in members_list:
       result += member['age']
    return result
def __get_youngest_member(members_list:list):
    members_list.sort(key = lambda x:x['age'])
    return members_list[0]
def __get_oldest_member(members_list:list):
    return members_list[len(members_list)-1]
