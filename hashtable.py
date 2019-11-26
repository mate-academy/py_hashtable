"""doc-string"""


class HashTable:
    """
    HashTable class
    """
    def __init__(self):
        self.table = [[] for _ in range(10)]

    @staticmethod
    def hash_(key: int) -> int:
        """
        Returns coded value of the key
        :param key: int
        :return: int
        """
        return key % 10

    def get(self, key: int):
        """
        Returns value respectively to the given key
        :param key: int
        :return: int
        """
        idx = self.hash_(key)
        for keys, val in self.table[idx]:
            if keys == key:
                return val
        return "Not found!!!"

    def set(self, key: int, value: int) -> None:
        """
        Adds given key, value to the hashtable
        :param key: int
        :param value: int
        :return: None
        """
        idx = self.hash_(key)
        self.table[idx].append((key, value))
