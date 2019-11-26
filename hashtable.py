"""docstring"""


class HashTable:
    """hash table implementation"""
    def __init__(self):
        self.hash_table = [[]] * 10

    @staticmethod
    def hash_(val: int) -> int:
        """hash function"""
        return val%10

    def get(self, key: int) -> int:
        """get value from table by key"""
        hashed = self.hash_(key)
        for element in self.hash_table[hashed]:
            if element[0] == key:
                return element[1]
        #  for mypy
        return False

    def set(self, key: int, value: int) -> None:
        """add value by key"""
        hashed = self.hash_(key)
        self.hash_table[hashed].append((key, value))
