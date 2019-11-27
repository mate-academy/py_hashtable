"""
docstring
"""


class HashTable:
    """
    class docstring
    """
    def __init__(self):
        self.hash_table = [[]] * 10

    def hash_(self, value: int) -> int:
        """

        :param value:
        :param x:
        :return:
        """
        return value % len(self.hash_table)

    def get(self, key: int) -> int:
        """

        :param key:
        :return:
        """
        index = self.hash_(key)
        for keys, val in self.hash_table[index]:
            if keys == key:
                return val
        return False

    def set(self, key: int, value: int) -> None:
        """

        :param key:
        :param value:
        :return:
        """
        hash_key = self.hash_(key)
        self.hash_table[hash_key].append((key, value))
