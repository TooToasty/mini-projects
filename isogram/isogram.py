def is_isogram(string):
    if len(string) == 0:
        return True
    letters = []
    count = len(string)
    string = string.lower().strip(' ')
    while count > 1:
        letter = string[-1]
        string = string[:-1]
        print(string)
        print(letter)
        if letter in string:
            return False
        print(string)
        count -= 1
    return True


print(is_isogram("apple"))
