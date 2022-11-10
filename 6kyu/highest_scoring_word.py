"""
Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.
"""

from string import ascii_lowercase


def high(x):
    x_list = x.split()
    words_dict = {}

    for word in x_list:
        words_dict[word] = sum([ascii_lowercase.index(i)+1 for i in word])

    return max(words_dict, key=words_dict.get)
