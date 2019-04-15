#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise.
        Running time O(1)"""
        return self.list.head is None


    def length(self):
        """Return the number of items in this stack.
        Running time: O(1)
        """
        return self.list.size

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – because were just creating a new node, no shifting necessary"""
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty. 
        Running time: O(1)"""
        if self.is_empty():
            return None
        return self.list.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) because were just changing the value of the head. no shift necessary"""
        if self.is_empty():
            raise ValueError('Stack is empty')
        data = self.list.head.data
        self.list.head = self.list.head.next
        self.list.size -= 1
        return data



# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        self.size = 0
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return self.size == 0

    def length(self):
        """Return the number of items in this stack."""
        return self.size

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) - but in some cases the list might grow to large and have to realocate its space in memory taking O(n) time
        this is the reason the linked list method is better, it prevents us from getting a STACK OVERFLOW"""
        self.list.append(item)
        self.size += 1

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if self.is_empty():
            return None
        return self.list[self.size - 1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – popping here is quick because we're removing the last element, so no shifting needs to happen"""
        if self.is_empty():
            raise ValueError('stack is empty')
        self.size -= 1
        return self.list.pop(self.size)


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = ArrayStack
# Stack = ArrayStack
