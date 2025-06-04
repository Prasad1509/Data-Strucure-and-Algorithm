class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_func(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_func(key)
        # Update if key exists
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # Otherwise add new key-value
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_func(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

# Usage
ht = HashTableChaining(10)
ht.insert(15, "Apple")
ht.insert(25, "Banana")  
ht.insert(35, "Cherry")

print(ht.search(25))  
print(ht.table)       
