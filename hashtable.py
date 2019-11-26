"""module docstring"""
class HashTable:
    """class docstring"""
    def __init__(self):
        """docstring"""
        self.hashtable = {}

    @staticmethod
    def hash(init_value):
        """docstring"""
        return init_value % 10

    def get(self, key):
        """docstring"""
        return self.hashtable[hash(key)]

    def set(self, key, value):
        """docstring"""
        self.hashtable[hash(key)] = value
