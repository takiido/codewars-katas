from string import capwords


def to_jaden_case(string):
    return capwords(string, " ")


def test():
    quote = "How can mirrors be real if our eyes aren't real"
    print(to_jaden_case(quote) == "How Can Mirrors Be Real If Our Eyes Aren't Real")
