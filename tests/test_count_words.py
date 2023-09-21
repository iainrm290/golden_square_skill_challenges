from lib.count_words import *
import pytest

def test_takes_string_as_arg():
    result = count_words("one")
    assert result == 1

def test_returns_result_from_empty_string():
    result = count_words("")
    assert result == 0

def test_returns_type_error():
    with pytest.raises(Exception) as e:
        count_words(34)
    error_message = str(e.value)
    assert error_message == "Must be a string!"

