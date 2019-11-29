"""Implement hash table using suggested hash function"""


class HashTable:
    """HashTable Class"""
    def __init__(self):
        self.hash_table = [[] for _ in range(10)]

    @staticmethod
    def hash_(key: int) -> int:
        """Hash funct"""
        return key%10

    def get(self, key: int) -> int:
        """Get value by key"""
        hash_key = self.hash_(key)
        return self.filter_hash(self.hash_table[hash_key], key)

    def set(self, key: int, value: int) -> None:
        """Set tuple of key, value"""
        hash_key = self.hash_(key)
        self.hash_table[hash_key].append((key, value))

    @staticmethod
    def filter_hash(arr, key):
        """Filter value of hash"""
        for i in arr:
            if i[0] == key:
                return i[1]
        return None
