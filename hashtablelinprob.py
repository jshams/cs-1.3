from doublylinkedlist import DoublyLinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [None]*init_size
        self.size = 0  # Number of key-value entries
        self.footprint = 1

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """Return the load factor, the ratio of number of entries to buckets.
        Best and worst case running time: O(1)"""
        return self.size / len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Best and worst case running time: O(n)"""
        list_of_keys = [] # create a list to add keys to
        for bucket in self.buckets: # iterate over our buckets
            if bucket is not None and bucket != self.footprint: # check if an item exists in the bucket
                list_of_keys.append(bucket[0]) # add the item's key to our list of keys
        return list_of_keys # return our list of keys

    def values(self):
        """Return a list of all values in this hash table.
        Best and worst case running time: O(n)"""
        list_of_vals = [] # create a list to add values to
        for bucket in self.buckets: # iterate over our buckets
            if bucket is not None and bucket != self.footprint: # check if an item exists in the bucket
                list_of_vals.append(bucket[1]) # add the item's value to our list of values
        return list_of_vals # return our list of values

    def items(self):
        """Return a list of all entries (key-value pairs) in this hash table.
        Best and worst case running time: O(n)"""
        list_of_items = [] # create a list to add items to
        for bucket in self.buckets: # iterate over our buckets
            if bucket is not None and bucket != self.footprint: # check if an item exists in the bucket
                list_of_items.append(bucket) # add the item to our list of items
        return list_of_items # return our list of items

    def length(self):
        """Return the number of key-value entries by checking the size.
        Best and worst case running time: O(1)"""
        return self.size

    def contains(self, key, bucket_index = None):
        """Return True if this hash table contains the given key, or False."""

    def get(self, key, bucket_index = None):
        """Return the value associated with the given key, or raise KeyError."""

    def set(self, key, val, bucket_index = None):
        """Insert or update the given key with its associated value."""

    def delete(self, key, bucket_index = None):
        """given a key delete the item. after deleting leave a footprint"""

    def _resize(self, new_size=None):
        """Resize this hash table's buckets and rehash all key-value entries."""
