def left_members(members: list):
    return list(filter(lambda x: "o" in x["name"], members))