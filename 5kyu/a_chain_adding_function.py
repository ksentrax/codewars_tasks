"""
Write a function that will add numbers together when called in succession.
add(1)(2)   # equals 3

We also want to be able to continue to add numbers to our chain.

add(1)(2)(3)   # 6
add(1)(2)(3)(4)   # 10
add(1)(2)(3)(4)(5)   # 15
and so on.

A single call should be equal to the number passed in.
"""


class add(int):
    def __call__(self, n):
        return add(self + n)
