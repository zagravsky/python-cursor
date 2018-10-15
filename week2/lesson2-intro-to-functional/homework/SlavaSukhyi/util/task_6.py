def sort_names(members):
    return sorted(members, key=lambda x: (len(x.get("name")), x.get('age')))

