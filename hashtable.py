"""docstring"""


class HashTable:
    """hash tabe implementation"""
    def __init__(self):
        self.hash_table = [None] * 20

    @staticmethod
    def hash_(val: int) -> int:
        """hash function"""
        return val%10

    def get(self, key: int) -> int:
        """get value from table by key"""
        return self.hash_table[key]

    def set(self, key: int, value: int) -> None:
        """add value by key"""
        self.hash_table[key] = value
