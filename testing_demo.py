import doctest

__author__ = 'Lindsay Ward'


def is_adult(age):
    """
    Determine if an age represents an adult or not
    :param age: age
    :return: Boolean for adult
    >>> is_adult(18)
    True
    >>> is_adult(17)
    False
    """
    return age > 18


def create_empty_list():
    """
    >>> create_empty_list()
    []

    :return: empty list
    """
    return []


x = create_empty_list()
# assert x == [], "create_empty_list() does not return an empty list!"

doctest.testmod()
