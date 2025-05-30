class HashTable:
    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
        
    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # Insert values into hash map
    def set_val(self, key, val):
        # Get the index from the key using hash function
        hashed_key = hash(key) % self.size
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            # Check if the bucket has same key as the key to be inserted
            if record_key == key:
                found_key = True
                break
        # If the bucket has same key as the key to be inserted, update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    # Return searched value with specific key
    def get_val(self, key):
        # Get the index from the key using hash function
        hashed_key = hash(key) % self.size
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
        for index, record in enumerate(bucket):
            record_key, record_val = record
            # Check if the bucket has same key as the key being searched
            if record_key == key:
                return record_val
        return "No record found"

    # Remove a value with specific key
    def delete_val(self, key):
        # Get the index from the key using hash function
        hashed_key = hash(key) % self.size
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
        for index, record in enumerate(bucket):
            record_key, record_val = record
            # Check if the bucket has the same key as the key to be deleted
            if record_key == key:
                bucket.pop(index)
                return
        return "No record found to delete"

    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


# Example usage
hash_table = HashTable(50)

# Insert some values
hash_table.set_val('gfg@example.com', 'some value')
print(hash_table)

hash_table.set_val('portal@example.com', 'some other value')
print(hash_table)

# Search/access a record with key
print(hash_table.get_val('portal@example.com'))

# Delete or remove a value
hash_table.delete_val('portal@example.com')
print(hash_table)
