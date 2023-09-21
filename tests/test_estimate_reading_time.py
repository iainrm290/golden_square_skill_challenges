from lib.estimate_reading_time import *

def test_estimate_reading_time_200_words():
    result = estimate_reading_time("hello " * 200)
    assert result == 1


def test_estimate_reading_time_400_words():
    result = estimate_reading_time("hello " * 400)
    assert result == 2

def test_estimate_reading_time_300_words():
    result = estimate_reading_time("hello " * 300)
    assert result == 1.5

def test_estimate_reating_time_empty_text():
    pass
