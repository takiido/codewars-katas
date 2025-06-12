def duplicate_count(text):
    duplicates = []
    for i in text.lower():
        if text.lower().count(i) > 1 and i not in duplicates:
            duplicates.append(i)

    return len(duplicates)


def test():
    print(duplicate_count("") == 0)
    print(duplicate_count("abcde") == 0)
    print(duplicate_count("abcdeaa") == 1)
    print(duplicate_count("abcdeaB") == 2)
    print(duplicate_count("Indivisibilities") == 2)