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
        """Return True if this hash table contains the given key, or False.
        Best case running time: O(1) most cases.
        Worst case: O(n), really .75 * O(n) when CLUSTERS occur
        The probablity of our best case is len(buckets) - 1/len(buckets)
        The larger our HT the faster it will be"""
        if bucket_index is None: # on the first iteration give bucket_index a value 
            bucket_index = self._bucket_index(key) # find the bucket index
        if self.buckets[bucket_index] is None: # if nothing is in the bucket we can return false
        # is this unclear? we'll see how this works in the delete method
            return False
        # check if buckets at index bucket index's key equals our key
        # we must first make sure theres no footprint because we can't access the 0th index of an int
        elif self.buckets[bucket_index] != self.footprint and self.buckets[bucket_index][0] == key:
            return True # if it does return True
        else: # otherwise call this method again at the next index
            if bucket_index == len(self.buckets) - 1: # if we just checked the last index go to the 0th
                bucket_index = -1 # set bucket_index to -1 because we'll increment to 0
            return self.contains(key, bucket_index + 1)

    def get(self, key, bucket_index = None):
        """Return the value associated with the given key, or raise KeyError.
        best time: O(1)
        worst time: O(n)"""
        if bucket_index is None: # on the first iteration give bucket_index a value
            bucket_index = self._bucket_index(key) # find the bucket index
        if self.buckets[bucket_index] is None: # if nothing is in the bucket we can raise a key error
        # is this unclear? we'll see how this works in the delete method
            raise KeyError('Key not found: {}'.format(key))
        # check if buckets at index bucket index's key equals our key
        # we must first make sure theres no footprint because we can't access the 0th index of an int
        elif self.buckets[bucket_index] != self.footprint and self.buckets[bucket_index][0] == key:
            return self.buckets[bucket_index][1] # if it does return the key's value
        else: # otherwise call this method again at the next index
            if bucket_index == len(self.buckets) - 1: # if we just checked the last index go to the 0th
                bucket_index = -1 # set bucket_index to -1 because we'll increment to 0
            return self.get(key, bucket_index + 1)

    def set(self, key, val, bucket_index = None):
        """Insert or update the given key with its associated value.
        best time: O(1)
        worst time: O(n), really 0.75 O(n)
        """
        if bucket_index is None: # on the first iteration give bucket_index a value
            bucket_index = self._bucket_index(key) # find the bucket index
        # check if there is None or a footprint in the bucket
        if self.buckets[bucket_index] is None or self.buckets[bucket_index] == self.footprint:
            self.buckets[bucket_index] = (key, val) # set the value of the bucket to out item
            self.size += 1 # increment the size by 1
        elif self.buckets[bucket_index][0] == key: # check if the key already exists
            self.buckets[bucket_index] = (key, val) # no we can update it
        else: # otherwise call this method again and maybe it'll work at the next index
            if bucket_index == len(self.buckets) - 1: # if we just checked the last index go to the 0th
                bucket_index = -1 # set bucket_index to -1 because we'll increment to 0
            return self.set(key, val, bucket_index + 1)
        #Check if the load factor exceeds a threshold such as 0.75
        if self.load_factor() > 0.75:
            # If so, automatically resize to reduce the load factor
            self._resize()

    def delete(self, key, bucket_index = None):
        """given a key delete the item. after deleting leave a footprint
        best time: O(1)
        worst time: O(n)"""
        if bucket_index is None: # on the first iteration give bucket_index a value
            bucket_index = self._bucket_index(key) # find the bucket index
        if self.buckets[bucket_index] is None: # check if the bucket is empty
            raise KeyError('Key not found: {}'.format(key)) # if it is raise an error
        # check if buckets at index bucket index's key equals our key
        # we must first make sure theres no footprint because we can't access the 0th index of an int
        elif self.buckets[bucket_index] != self.footprint and self.buckets[bucket_index][0] == key:
            '''if we find the key we want to delete we must leave a footprint. why? when we insert an item we 
            place it in it's hashed keys index. if something exists in that bucket we keep moving forward till 
            we find a bucket for it. this means to find an item we must find its bucket index and if the key is 
            there, we found it. but if the key isn't there we must keep moving forward until we find an empty 
            space. we can stop here once we found an empty space because when we added the item it must have
            claimed an empty bucket. right? not really. because what if we deleted an item in between? 
            this is why we add a footprint, so we know that there was once something in this bucket
            and when we search we can stop when we find an empty bucket and skip over ones with footprints
            without a footprint, we'd need to traverse the entire table when we run get or contains'''
            self.buckets[bucket_index] = self.footprint
            self.size -= 1 # decrement the size by 1
        else: # otherwise call this method again and maybe it'll work at the next index
            if bucket_index == len(self.buckets) - 1: # if we just checked the last index go to the 0th
                bucket_index = -1 # set bucket_index to -1 because we'll increment to 0
            self.delete(key, bucket_index + 1)

    def _resize(self, new_size=None):
        """Resize this hash table's buckets and rehash all key-value entries."""
