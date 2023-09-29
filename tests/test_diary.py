from lib.diary import *
from lib.diary_entry import *
import pytest

def test_intantiation_of_diary():
    diary = Diary()
    assert isinstance(diary, Diary)

def test_add_parameter_is_diary_entry():
    diary = Diary()
    diary_entry = DiaryEntry("Monday", "Meetings")
    diary.add(diary_entry)
    assert isinstance(diary_entry, DiaryEntry) == True

def test_is_empty_list():
    diary = Diary()
    assert diary.entries == []

def test_add_updates_entries():
    diary = Diary()
    diary_entry = DiaryEntry("Monday", "Meetings")
    diary.add(diary_entry.entry)
    diary_entry = DiaryEntry("Tuesday", "Appointments")
    diary.add(diary_entry.entry)
    result = diary.entries
    assert result == [("Monday", "Meetings"), ("Tuesday", "Appointments")]


