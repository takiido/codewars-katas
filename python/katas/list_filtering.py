def filter_list(l):
    new_list = []

    for i in l:
        if isinstance(i, int):
            new_list.append(i)

    return new_list


def test():
    print(filter_list([1, 2, 'a', 'b']) == [1, 2])
    print(filter_list([1, 'a', 'b', 0, 15]) == [1, 0, 15])
    print(filter_list([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123])
