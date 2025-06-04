# Simple hash function: key mod table size
def hash_func(key, size):
    return key % size

table_size = 10
hash_table = [None] * table_size

def insert(key, value):
    index = hash_func(key, table_size)
    hash_table[index] = value

# Insert data
insert(15, "Apple")
insert(25, "Banana")

print(hash_table)
