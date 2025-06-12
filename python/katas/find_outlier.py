def find_outlier(integers):
    evens = [e for e in integers if e % 2 == 0]
    odds = [o for o in integers if o % 2 == 1]
    return odds[0] if len(evens) > len(odds) else evens[0]


def test():
    print(find_outlier([2, 4, 6, 8, 10, 3]) == 3)
    print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11)
    print(find_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160)
