"""
Imagine that you have a pyramid built of numbers, like this one here:

   /3/
  \7\ 4
 2 \4\ 6
8 5 \9\ 3

Let's say that the 'slide down' is the maximum sum of consecutive numbers from the top to the bottom of the pyramid.
As you can see, the longest 'slide down' is 3 + 7 + 4 + 9 = 23

Write a function that takes a pyramid representation as argument and returns its' largest 'slide down'. For example:

* With the input `[[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]`
* Your function should return `23`.
"""


def longest_slide_down(pyramid):
    res = pyramid.pop()

    while pyramid:
        tmp = pyramid.pop()
        res = [tmp[i] + max(res[i], res[i+1]) for i in range(len(tmp))]

    return res.pop()
