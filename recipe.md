# Reading Time Function Design Recipe

## 1. Describe the problem

> as a user
> So that I can manage my time
> I want to get an estimate reading time for a text at a speed
  of 200 words a minute.

## Design the Function Signature

def reading_time(text):
    '''Calculates reading time for a text

    Parameters: A text

    Returns: A duration time

    Side effects: None
    pass
    '''

## Create Examples as Tests

> given a text of 200 words it returns a reading time of 1

estimate_reading_time_200_words("200 words")
# => 1.0

> given a text of 400 words it returns 2

estimate_reading_time_400_words("400 words")
# => 2.0

> given a text of 300 words it returns 1.5

estimate_reading_time_300_words("3000 words")
# => 1.5

> given an empty text it raises an error

estimate_reading_time_empty_text("")
# => raises error