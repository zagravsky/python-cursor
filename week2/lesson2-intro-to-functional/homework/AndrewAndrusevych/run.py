from utils.task_1 import members_list as MEMBERS
from utils.task_3 import add_load
from utils.task_2 import upper_name
from utils.task_4 import get_member_with_symbol_in_name
from utils.task_5 import get_summery_age_youngest_and_oldest_member
from utils.task_6 import sort_members_by_len_name
from utils.task_7 import to_roman


if __name__ == "__main__":
    import copy
    members = copy.deepcopy(MEMBERS)
    print('Task_1\n',members)
    members = copy.deepcopy(MEMBERS)
    print('Task_2\n',upper_name(members))
    members = copy.deepcopy(MEMBERS)
    print('Task_3\n', add_load(members))
    members = copy.deepcopy(MEMBERS)
    print('Task_4\n', get_member_with_symbol_in_name(members,'o'))
    members = copy.deepcopy(MEMBERS)
    print('Task_5\n', get_summery_age_youngest_and_oldest_member(members))
    members = copy.deepcopy(MEMBERS)
    print('Task_6\n', sort_members_by_len_name(members))
    print('Task_7\n', to_roman(4999))