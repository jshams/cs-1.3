from hashtable import HashTable

class Set(object):
    def __init__(self, elements=None):
        """Initialize this """
        self.items = HashTable()
        self.size = 0
        for item in elements:
            self.items.set(item, item)
    def __iter__(self):
        for item in self.items:
            yield item
            
    def length(self):
        """return the length of our set"""
        return self.items.length()

    def contains(self, element):
        """ return a boolean indicating whether element is in this set"""
        return self.items.contains(element)

    def add(self, element):
        """add element to this set, if not present already"""
        self.items.set(element, element)

    def remove(self, element):
        """remove element from this set, if present, or else raise KeyError"""
        self.items.delete(element)

    def union(self, other_set):
        """return a new set that is the union of this set and other_set"""
        newSet = Set()
        for item in self:
            newSet.set(item)
        for item in other_set:
            newSet.set(item)
        return newSet

    def intersection(self, other_set):
        """return a new set that is the intersection of this set and other_set"""
        newSet = Set()
        for item in self:
            if other_set.contains(item):
                newSet.add(item)
        return newSet

    def difference(self, other_set):
        """return a new set that is the difference of this set and other_set"""
        new_set = Set()
        intersection = self.intersection(other_set)
        for item in self:
            if not intersection.contains(item):
                newSet.add(item)

    def is_subset(self, sub_set):
        """ return a boolean indicating whether other_set is a subset of this set"""

        for item in sub_set:
            if not self.contains(item):
                return False
        return True
    

class Set(HashTable):
    def __init__(self, elements=None):
        for element in elements
