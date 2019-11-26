"""Hash module"""

class HashTable:
    """Hash class"""
    def __init__(self):
        self.array = [None] * 10

    @staticmethod
    def hash_(key: int) -> int:
        """
        :param key: key
        :return: hashes key
        """
        result_key = 0
        for i in str(key):
            result_key += int(i)+1
        return result_key % 10

    def get(self, key: int):
        """
        :param key: key
        :return: hash element
        """
        index = self.hash_(key)
        return self.array[index]

    def set(self, key, value) -> None:
        """
        :param key: key
        :param value: value for hash table
        """
        index = self.hash_(key)
        self.array[index] = value
