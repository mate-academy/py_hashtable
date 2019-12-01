"""module docstring"""
from typing import List

class HashTable:
    """class docstring"""

    hash_index = 10
    hashtable = [[] for x in range(hash_index)] # type: List[List[int]]

    def hash(self, key):
        """docstring"""
        return key % self.hash_index

    def get(self, key):
        """docstring"""
        return [x[1] for x in self.hashtable[self.hash(key)] if x[0] == key][0]

    def set(self, key, value):
        """docstring"""
        self.hashtable[self.hash(key)].append((key, value))
