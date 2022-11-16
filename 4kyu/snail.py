"""
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element,
traveling clockwise. The idea is to traverse the 2-d array in a clockwise snailshell pattern.

array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

snail(array) #=> [1, 2, 3, 6, 9, 8, 7, 4, 5]
"""


def snail(snail_map):
    output_snail = []

    while snail_map:
        for i in snail_map[0]:
            output_snail.append(i)
        snail_map.pop(0)

        for i in snail_map:
            output_snail.append(i[-1])
            i.pop()

        if len(snail_map) > 1:
            for i in reversed(snail_map[-1]):
                output_snail.append(i)
            snail_map.pop(-1)

        for i in reversed(snail_map):
            output_snail.append(i[0])
            i.pop(0)

    return output_snail
