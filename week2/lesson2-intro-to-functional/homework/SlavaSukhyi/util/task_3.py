
def load(members_list: list):
    for member in members_list:
        member["load"] = round(member["age"] / 200 * 100, 2)
    return members_list
