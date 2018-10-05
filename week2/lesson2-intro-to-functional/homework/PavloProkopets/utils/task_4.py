def func_4(list_4: list) -> list:
  for x in list_4[:]:
    if not 'O' in x["name"]:
        list_4.remove(x)
  return list_4




