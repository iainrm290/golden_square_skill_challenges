# Name: task_tracker
# Parameters: text type=str
# Returns: True or False type=bool

def task_tracker(text):
    if type(text) != str:
        raise Exception("Must be string!")
    elif text == "":
        raise Exception("Text is empty!")
    return "#TODO" in text