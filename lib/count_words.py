def count_words(string):
    if type(string) != str:
        raise Exception("Must be a string!")
    else:
        return len(string.split())