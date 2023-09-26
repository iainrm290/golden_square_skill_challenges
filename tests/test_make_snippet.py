# from lib.make_snippet import *
# import pytest

# def test_return_empty_string_given_empty_string():
#     result = make_snippet("")
#     assert result == ""

# def test_return_single_word():
#     result = make_snippet("yes")
#     assert result == "yes"

# def test_return_fewer_than_five_words():
#     result = make_snippet("one two three")
#     assert result == "one two three"

# def test_return_just_five_words():
#     result = make_snippet("one two three four five")
#     assert result == "one two three four five"

# def test_return_elipsis_after_five_words_given_string_over_five_words():
#     result = make_snippet(("one two three four five six"))
#     assert result == "one two three four five..."
