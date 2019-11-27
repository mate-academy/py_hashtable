"""
module hashtable
"""


class HashTable:
    """
    Implementation of hash table.
    """

    def __init__(self):
        self.table = [[] for _ in range(10)]

    @staticmethod
    def hash_(key: int) -> int:
        """
        Hashing key value.
        :param key: int
        :return: int
        """
        return key % 10

    def get(self, key: int):
        """
        Get object with key from hash table.
        :param key: int
        :return: None
        """
        index = self.hash_(key)
        for keys, val in self.table[index]:
            if keys == key:
                return val
        return "No such key."

    def set(self, key: int, value: int) -> None:
        """
        Insert object with key into hash table.
        :param key: int
        :param value: int
        :return: None
        """
        index = self.hash_(key)
        self.table[index].append((key, value))
