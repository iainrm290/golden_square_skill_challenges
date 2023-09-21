# Problem

# As a User
# So that I can keep track of my tasks
# i want to check if a text includes the string #TODO

# returns_true_given_text_with_hashTODO
from lib.task_tracker import *
import pytest

def test_returns_true_given_text_with_hashTODO():
    result = task_tracker("#TODO")
    assert result == True

# returns_false_given_text_without_hashTODO

def test_returns_false_given_text_without_hashTODO():
    result = task_tracker("It's not raining.")
    assert result == False

# raises_error_if_text_not_str

def test_raises_error_if_text_not_str():
    with pytest.raises(Exception) as e:
        task_tracker(123)
    error_message = str(e.value)
    assert error_message == "Must be string!"

# raises_error_given_empty_text

def test_raises_error_given_empty_text():
    with pytest.raises(Exception) as e:
        task_tracker("")
    error_message = str(e.value)
    assert error_message == "Text is empty!"
