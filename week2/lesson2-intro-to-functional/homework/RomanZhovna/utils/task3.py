import copy


def filtered_list(l: list) -> list:
    def addload(d: dict)-> dict:
        d['load'] = d['age']*100/200
        return d
    return list(filter(lambda x: x['load'] < 100, list(map(addload, copy.deepcopy(l)))))
