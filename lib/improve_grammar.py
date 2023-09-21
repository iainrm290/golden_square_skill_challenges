# Parameters: A str
# Return: A verification as True or False
# Side effects: None

def improve_grammar(text):
    symbols = ".!?"
    return text[0].isupper() and text[-1] in symbols
        