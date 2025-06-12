import katas.list_filtering as lf

if __name__ == '__main__':
    # https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
    # Test cases for the filter_list function
    print(lf.filter_list([1, 2, 'a', 'b']) == [1, 2])
    print(lf.filter_list([1, 'a', 'b', 0, 15]) == [1, 0, 15])
    print(lf.filter_list([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123])
