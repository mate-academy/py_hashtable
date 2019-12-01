"""module"""


class HashTable:
    """hashtable"""
    def __init__(self):
        self.table = [None] * 100

    def hash_(self, item: int) -> int:
        """generate hash"""
        return item % len(self.table)

    def get(self, key: int) -> int:
        """get item"""
        hash_key = self.hash_(key)
        return self.table[hash_key]

    def set(self, key: int, value: int) -> None:
        """set item"""
        hash_key = self.hash_(key)
        self.table[hash_key] = value
