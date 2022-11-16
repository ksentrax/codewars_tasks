"""
Write a function, that returns an array of all variations for an observed PIN with a length of 1 to 8 digits.
All PINs, the observed one and also the results, must be strings, because of potentially leading '0's.

The keypad has the following layout:
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘

Note: each of the digits could be another adjacent digit (horizontally or vertically, but not diagonally).
E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.
"""

import itertools

PIN_DICT = {'1': ['1', '2', '4'],
            '2': ['1', '2', '3', '5'],
            '3': ['2', '3', '6'],
            '4': ['1', '4', '5', '7'],
            '5': ['2', '4', '5', '6', '8'],
            '6': ['3', '5', '6', '9'],
            '7': ['4', '7', '8'],
            '8': ['5', '7', '8', '9', '0'],
            '9': ['6', '8', '9'],
            '0': ['8', '0']}


def get_pins(observed):
    tmp = [PIN_DICT[i] for i in observed]
    return [''.join(i) for i in list(itertools.product(*tmp))]
