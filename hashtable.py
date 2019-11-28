'''
Module
'''


class HashTable:
    '''
    HashTabl
    '''
    def __init__(self):
        '''
        Initial matrix
        '''
        self.matrix = [[] for _ in range(10)]

    @staticmethod
    def hash_(key: int) -> int:
        '''

        :param key:
        :return:
        '''
        return key % 10

    def get(self, key: int):
        '''

        :param key:
        :return:
        '''
        index = self.hash_(key)
        for keys, val in self.matrix[index]:
            if keys == key:
                return val
        return "Key not found"

    def set(self, key: int, value: int) -> None:
        '''

        :param key:
        :param value:
        :return:
        '''
        index = self.hash_(key)
        self.matrix[index].append((key, value))
