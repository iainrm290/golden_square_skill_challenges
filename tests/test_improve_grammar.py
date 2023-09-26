# from lib.improve_grammar import *

# '''
# 1.
# As a user
# So that I can improve my grammar
# I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.
# '''


# # returns True if sentence starts with capital and ends with "."

# def test_sentence_starts_with_capital_and_ends_with_period():
#     result = improve_grammar("It is raining.")
#     assert result == True

    
# # returns True if sentence starts with capital and ends with "!"

# def test_sentence_starts_with_capital_and_ends_with_exclamation():
#     result = improve_grammar("It is not raining!")
#     assert result == True


# # returns True if sentence starts with capital and ends with "?"

# def test_sentence_starts_with_capital_and_ends_with_question_mark():
#     result = improve_grammar("Is it raining?")
#     assert result == True

# # returns False if sentence starts with capital but doesn't end with correct punctuation

# def test_sentence_starts_with_capital_but_does_not_end_with_correct_punctuation():
#     result = improve_grammar("It is raining")
#     assert result == False
# # returns False if sentence doesn't start with capital but ends with correct punctuation

# # raises an error if text is empty