"""
Middle Earth is about to go to war. The forces of good will have many battles with the forces of evil.
Different races will certainly be involved. Each race has a certain worth when battling against others.

The function will be given two parameters. Each parameter will be a string of multiple integers
separated by a single space. Each string will contain the count of each race on the side of good and evil.

The first parameter will contain the count of each race on the side of good. The second parameter will contain
the count of each race on the side of evil. All values are non-negative integers.
The resulting sum of the worth for each side will not exceed the limit of a 32-bit integer.
"""


def good_vs_evil(good, evil):
    good_list = [1, 2, 3, 3, 4, 10]
    evil_list = [1, 2, 2, 2, 3, 5, 10]

    good_total = sum([int(x)*y for x, y in zip(good.split(), good_list)])
    evil_total = sum([int(x)*y for x, y in zip(evil.split(), evil_list)])

    if good_total > evil_total:
        return 'Battle Result: Good triumphs over Evil'
    elif evil_total > good_total:
        return 'Battle Result: Evil eradicates all trace of Good'
    else:
        return 'Battle Result: No victor on this battle field'
