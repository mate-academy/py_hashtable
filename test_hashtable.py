import hashtable


def test_hashtable1():
    h = hashtable.HashTable()
    h.set(1, 1)
    h.set(11, 2)
    h.set(2, 3)
    assert h.get(1) == 1


def test_hashtable2():
    h = hashtable.HashTable()
    h.set(1, 1)
    h.set(11, 2)
    h.set(2, 3)
    assert h.get(11) == 2


def test_hashtable3():
    h = hashtable.HashTable()
    h.set(1, 1)
    h.set(11, 2)
    h.set(2, 3)
    assert h.get(2) == 3
