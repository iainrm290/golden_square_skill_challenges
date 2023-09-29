from lib.diary import *
from lib.diary_entry import *
import pytest

def test_for_two_entries_returned_in_list():
    diary = Diary()
    entry1 = DiaryEntry("Title 1", "Entry 1")
    entry2 = DiaryEntry("Title 2", "Entry 2")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.all() == [entry1, entry2]

def test_count_diary_count_words():
    diary = Diary()
    entry1 = DiaryEntry("Title 1", "Entry 1")
    entry2 = DiaryEntry("Title 2", "Entry 2")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.count_words() == 4

def test_count_diary_reading_time():
    diary = Diary()
    entry1 = DiaryEntry("Title 1", "Entry 1")
    entry2 = DiaryEntry("Title 2", "Entry 2")
    diary.add(entry1)
    diary.add(entry2)
    diary.count_words() == 4
    pass

def test_for_reading_time_with_four_words():
    diary = Diary()
    diary_entry1 = DiaryEntry("Wednesday", "one two three four")
    diary.add(diary_entry1)
    diary_entry2 = DiaryEntry("Thursday", "one two three four")
    diary.add(diary_entry2)
    diary.count_words()
    assert diary.reading_time(4) == 2