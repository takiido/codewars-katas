def filter_list(l):
    new_list = []

    for i in l:
        if isinstance(i, int):
            new_list.append(i)

    return new_list
