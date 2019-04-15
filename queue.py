#!python

from linkedlist import LinkedList
from doublylinkedlist import DoublyLinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.list.head is None

    def length(self):
        """Return the number of items in this queue."""
        return self.list.size

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – adding a new node with a linked list takes O(1) time"""
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        return self.list.head.data

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – removing an item from the front of a linked list takes O(1)"""
        if self.is_empty():
            raise ValueError('Queue us empty')
        data = self.list.head.data
        self.list.head = self.list.head.next
        self.list.size -= 1
        return data


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        self.size = 0
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.size == 0

    def length(self):
        """Return the number of items in this queue."""
        return self.size

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – could be O(n) if list gets too big and requires reallocation"""
        self.list.append(item)
        self.size += 1

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        return self.list[0]

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(n) – When removing the zeroth element from the list each element must shift left"""
        if self.is_empty():
            raise ValueError('Queue is empty')
        self.size -= 1
        return self.list.pop(0)


class Deque(object):
    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = DoublyLinkedList()
        if iterable is not None:
            for item in iterable:
                self.push_back(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.list.head is None and self.list.tail is None

    def length(self):
        """Return the number of items in this queue."""
        return self.list.size

    def push_front(self, item):
        """Insert the given item at the front of this queue.
        Running time: O(1)"""
        self.list.prepend(item)

    def push_back(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – adding a new node with a linked list takes O(1) time"""
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        return self.list.head.data
    
    def back(self):
        """Return the item at the back of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        return self.list.tail.data

    def pop_front(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – removing an item from the front of a linked list takes O(1)"""
        if self.is_empty():
            raise ValueError('Queue us empty')
        data = self.list.head.data
        self.list.head = self.list.head.next
        self.list.size -= 1
        if self.list.size == 0:
            self.list.tail = None
            self.list.head = None
        return data

    def pop_back(self):
        """Remove and return the item at the back of this queue, 
        or raise ValueError if this queue is empty.
        Running time: O(1)"""
        if self.is_empty():
            raise ValueError('Queue is empty')
        data = self.list.tail.data
        self.list.tail = self.list.tail.prev
        self.list.size -= 1
        if self.list.size == 0:
            self.list.head = None
            self.list.tail = None
        return data




# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = ArrayQueue
# Queue = ArrayQueue
