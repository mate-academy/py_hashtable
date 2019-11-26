"""Hash module"""

class HashTable:
    """Hash class"""
    def __init__(self):
        self.array = []
        for _ in range(10):
            self.array.append({})

    @staticmethod
    def hash_(key: int) -> int:
        """
        :param key: key
        :return: hashes key
        """
        return key % 10

    def get(self, key: int):
        """
        :param key: key
        :return: hash element
        """
        index = self.hash_(key)
        print(self.array)
        if self.array[index]:
            return self.array[index][key]
        return self.array[index]


    def set(self, key, value) -> None:
        """
        :param key: key
        :param value: value for hash table
        """
        index = self.hash_(key)
        self.array[index][key] = value
