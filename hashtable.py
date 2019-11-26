"""
Implement hash table using suggested hash function
"""


def hash_(num: int) -> int:
    """Func"""
    return num % 10


class HashTable:
    """
    Class
    """
    def __init__(self):
        self.hash_dict = {}

    def get(self, key: int) -> int:
        """Get value"""
        return self.hash_dict[key]

    def set(self, key: int, value: int) -> None:
        """Set value"""
        self.hash_dict[key] = value
