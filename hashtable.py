"""
module hashtable
"""


class HashTable:
    """
    Implementation of hash table.
    """

    def __init__(self):
        self.table = []
        self.size = 10
        for _ in range(self.size):
            self.table.append({})

    def hash_(self, key: int) -> int:
        """

        :param key: int
        :return: int
        """
        return key % 10

    def get(self, key: int) -> dict:
        """
        Get object with key from hash table.
        :param key: int
        :return: None
        """
        hash_key = self.hash_(key)
        if self.table[hash_key]:
            return self.table[hash_key][key]
        return self.table[hash_key]

    def set(self, key: int, value: int) -> None:
        """
        Insert object with key into hash table.
        :param key: int
        :param value: int
        :return: None
        """
        hash_key = self.hash_(key)
        self.table[hash_key][key] = value
