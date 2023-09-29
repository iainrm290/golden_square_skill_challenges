from lib.diary import *
from lib.diary_entry import *
import pytest


def test_diary_entry_count_words():
    diary_entry = DiaryEntry("Wednesday", "one two three")
    result = diary_entry.count_words()
    assert result == 3
