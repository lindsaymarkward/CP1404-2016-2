"""
CP14040 Recursion demo
"""


def count_down(n):
    for i in range(n, -1, -1):
        print(i)


# count_down(5)


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(4))
