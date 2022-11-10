"""
Write a function that will convert a string into title case, given an optional list of exceptions (minor words).
The list of minor words will be given as a string with each word separated by a space.
Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

Arguments:

First argument (required): the original string to be converted.
Second argument (optional): space-delimited list of minor words that must always be lowercase except for
the first word in the string. The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.

Examples:

title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'
"""


def title_case(title, minor_words=''):
    words_list = title.title().split(' ')
    minor_words_list = minor_words.title().split(' ')
    return ' '.join([words_list[0]] + [i.lower() if i in minor_words_list else i for i in words_list[1:]])
