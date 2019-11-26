"""
module hashtable
"""


class HashTable:
    """
    Implementation of hash table.
    """

    def __init__(self):
        self.size = 100
        self.table = [None] * self.size

    def hash_(self, key: int) -> int:
        """

        :param key: int
        :return: int
        """
        return id(key) % len(self.table)

    def get(self, key: int) -> None:
        """
        Get object with key from hash table.
        :param key: int
        :return: None
        """
        hash_key = self.hash_(key)
        return self.table[hash_key]

    def set(self, key: int, value: int) -> None:
        """
        Insert object with key into hash table.
        :param key: int
        :param value: int
        :return: None
        """
        hash_key = self.hash_(key)
        self.table[hash_key] = value
