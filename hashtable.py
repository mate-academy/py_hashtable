"""
Implement hash table using suggested hash function
"""


class HashTable:
    """
    Class
    """
    def __init__(self):
        self.hash_table = [[] for _ in range(10)]

    @staticmethod
    def hash_(num: int) -> int:
        """Func"""
        return num % 10

    def get(self, key):
        """Get value"""
        hash_key = self.hash_(key)
        bucket = self.hash_table[hash_key]
        for _, key_value in enumerate(bucket):
            bucket_key, bucket_value = key_value
            if key == bucket_key:
                return bucket_value
        return None

    def set(self, key: int, value: int) -> None:
        """Set value"""
        print('key: ', key, 'value: ', value)
        hash_key = self.hash_(key)
        key_exists = False
        bucket = self.hash_table[hash_key]
        count = 0
        for count, key_value in enumerate(bucket):
            bucket_key, _ = key_value
            if key == bucket_key:
                key_exists = True
                break
        if key_exists:
            bucket[count] = ((key, value))
        else:
            bucket.append((key, value))
