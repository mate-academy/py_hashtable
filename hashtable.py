"""
Implement hash table using suggested hash function
"""


class HashTable:
    """
    Class
    """
    def __init__(self):
        self.hash_table = [[] for _ in range(10)]

    def hash_(self, num: int) -> int:
        """Func"""
        return num % 10

    def get(self, key: int) -> int:
        """Get value"""
        hash_key = self.hash_(key)
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v

    def set(self, key: int, value: int) -> None:
        """Set value"""
        print('key: ', key, 'value: ', value)
        hash_key = self.hash_(key)
        key_exists = False
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))
