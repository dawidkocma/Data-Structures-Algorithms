class HashTable:
    """
    A simple hash table implementation using separate chaining for collision resolution.
    Keys are strings; values can be of any type.
    """
    def __init__(self, size=7):
        # Initialize the backing array (data_map) with the given size.
        # Each slot will hold either None or a list of [key, value] pairs.
        self.data_map = [None] * size
        
    def __hash(self, key):
        """
        Compute a hash for the given string key.
        Uses a basic polynomial rolling hash:
          - Multiply each character's ASCII code by 23, add to accumulator,
            then mod by the array length to wrap within bounds.
        Returns an index between 0 and len(data_map) - 1.
        """
        my_hash = 0
        for letter in key:
            # ord(letter) gets ASCII code; multiply to spread values out
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
        
    def print_table(self):
        """
        Print the internal state of the hash table.
        Shows each index and its contents (either None or a list of pairs).
        """
        for i, val in enumerate(self.data_map):
            print(i, ":", val)
            
    def set_item(self, key, value):
        """
        Insert or update the (key, value) pair in the hash table.
        1. Compute the index using the hash function.
        2. If there's no list at that index yet, create one.
        3. Append the new [key, value] pair to the list.
           (This implementation does not check for duplicate keys;
            duplicates will coexist in the same bucket.)
        """
        index = self.__hash(key)  # Find bucket index
        # If this bucket is empty, initialize it to an empty list
        if self.data_map[index] is None:
            self.data_map[index] = []
        # Store the key/value pair
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        """
        Retrieve the value associated with the given key.
        1. Compute the index via the hash function.
        2. If the bucket is not empty, iterate through its pairs.
        3. Return the value when the key matches.
        Returns None if the key is not found.
        """
        index = self.__hash(key)  # Locate correct bucket
        bucket = self.data_map[index]
        if bucket is not None:
            # Search through all [key, value] pairs in this bucket
            for k, v in bucket:
                if k == key:
                    return v
        # Key not found
        return None
    
    def keys(self):
        """
        Return a list of all keys stored in the hash table.
        Iterates over each bucket and collects the key from each pair.
        """
        all_keys = []
        # Scan every bucket
        for bucket in self.data_map:
            if bucket is not None:
                # Extract each key in this bucket
                for k, _ in bucket:
                    all_keys.append(k)
        return all_keys


# Example usage:
my_hash_table = HashTable()              # Create a table with default size 7

# Insert some inventory items
my_hash_table.set_item('bolts', 9000)
my_hash_table.set_item('washers', 3000)
my_hash_table.set_item('lumber', 70)

# Display the table's buckets
my_hash_table.print_table()

# Lookup existing and missing keys
print(my_hash_table.get_item('washers'))  # Expected output: 3000
print(my_hash_table.get_item('nails'))    # Expected output: None

# List all stored keys
print(my_hash_table.keys())               # E.g.: ['bolts', 'washers', 'lumber']
