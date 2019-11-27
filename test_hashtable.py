"""
docstring
"""


import hashtable


def test_hashtable1():
    """

    :return:
    """
    h = hashtable.HashTable()
    h.set(1, 1)
    h.set(11, 2)
    h.set(2, 3)
    assert h.get(1) == 1


def test_hashtable2():
    """

    :return:
    """
    h = hashtable.HashTable()
    h.set(1, 1)
    h.set(11, 2)
    h.set(2, 3)
    assert h.get(11) == 2


def test_hashtable3():
    """

    :return:
    """
    h = hashtable.HashTable()
    h.set(1, 1)
    h.set(11, 2)
    h.set(2, 3)
    assert h.get(2) == 3
