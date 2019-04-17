from hashtable import HashTable

class Set(object):
    def __init__(self, elements=None):
        """Initialize this """
        self.items = HashTable()
        for item in elements:
            self.items.set(item, item)
    def __iter__(self):
        for bucket in self.items.buckets:
            for item in bucket:
                yield item
    def size(self):
        return self.items.length()
    def contains(self, element):
        return self.items.contains(element)
    def add(self, element):
        self.items.set(element, element)
    def remove(self, element):
        self.items.delete(element)
    def union(self, other_set):
        new_set = 
    def intersection(self, other_set):
        newSet = Set()
        for bucket in self.items.buckets:
            if not bucket.is_empty():
                for item in bucket:
                    if other_set.contains(item):
                        newSet.add(item)
        return newSet
    def 

class Set(HashTable):
    def __init__(self, elements=None):
        for element in elements
