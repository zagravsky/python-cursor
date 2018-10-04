# 1. Summary age of members.
#
# 2. The youngest member
#
# 3. The oldest member.
def task_5_function (members:list):
    answer = []
    answer.append(sum(list(map(lambda x: x['age'],members ))))
    answer.append(min(members, key=lambda x:x['age']))
    answer.append(max(members, key=lambda x: x['age']))
    return answer

