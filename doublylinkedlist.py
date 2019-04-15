#!python
'''
### Stretch Challenges
- Implement `DoublyLinkedList` class with `BinaryNode` objects, which have both `next` and `previous` properties
- Write unit tests for to ensure the `DoublyLinkedList` class is robust
    - Include test cases for each class instance method and property
- Annotate methods with complexity analysis of running time and space (memory)
'''

class DoublyNode(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class DoublyLinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes

        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False.
        Best and worst case running time: O(1)"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Best and worst case running time: O(1)"""
        return self.size

    def get_at_index(self, index): 
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) when n == 0 or n is out of range
        Worst case running time: O(n) 
        with doubly linked list the time is cut in half"""
        # Check if the given index is out of range and if so raise an error
        if not (-1 < index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # checks if the index is in the frist half of the list
        if self.size / 2 > index:
            node_index = 0  # this will increment till we reach our index
            node = self.head # start at first node
            while node_index != index: # traverse the list till node_index == index
                node = node.next
                node_index += 1
            return node.data # we've found it! Now we can return its data
        # the index is in the second half of the linked list start from the end
        else:
            node_index = self.size - 1
            node = self.tail
            while node_index != index:
                node = node.prev
                node_index -= 1
            return node.data
            

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) when n == 0 or n is out of range
        Worst case running time: O(n)
        With doubly linked list time is really half O(n) but constants are dropped"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # if index is 0 we can call our prepend method to do work for us
        if index == 0:
            self.prepend(item)
            return
        # if index is the same as the size call our append method
        elif index == self.size:
            self.append(item)
            return
        else:
            if self.size / 2 > index:
                node_index = 0 # this will increment till we reach our index
                node = self.head # start at first node
                new_node = DoublyNode(item) # create an instance of node with item
                while node_index != index: # traverse the list till node_index == index
                    node_index += 1
                    node = node.next
                # we've found the insert location
                new_node.next = node.next # now the new node is pointing to the next node
                new_node.prev = node
                node.next.prev = new_node # now the next node is pointing back to the new node
                node.next = new_node # now the node is pointing towards our new node
                self.size += 1
            else: # if the index is in the second half of the list
                node_index = self.size -1
                node = self.tail
                new_node = DoublyNode(item)
                while node_index != index:
                    print(node.next, node, node.prev)
                    print(node_index, index + 1)
                    node = node.prev
                    node_index -= 1
                new_node.next = node
                new_node.prev = node.prev
                node.prev.next = new_node
                node.prev = new_node

                # new_node.next = node.next # now the new node is pointing to the next node
                # new_node.prev = node 
                # node.next.prev = new_node # now the next node is pointing back to the new node
                # node.next = new_node # now the node is pointing towards our new node
                self.size += 1
                
    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst case running time: O(1)"""
        # Create a new node to hold the given item
        new_node = DoublyNode(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node
        else:
            # Otherwise insert new node after tail
            new_node.prev = self.tail
            self.tail.next = new_node
        # Update tail to new node regardless
        self.tail = new_node
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and worst case running time: ??? under what conditions? [TODO]"""

        # Create a new node to hold the given item
        new_node = DoublyNode(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
            self.head.prev = new_node
        # Update head to new node regardless
        self.head = new_node
        self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Up to n iterations if we don't exit early
            # Check if this node's data satisfies the given quality function
            if quality(node.data):  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return node.data  # Constant time to return data
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case running time: O(1) when old_item is the first in the list
        Worst case running time: O(n) when old_item is the last or not found """

        node = self.head # start with the first node
        while node is not None: # traverse the linked list till our data mathches
            if node.data == old_item: # if the data matches replace the data and end the loop
                node.data = new_item
                return 
            node = node.next
        raise ValueError('Item not found: {}'.format(old_item)) # old item was not found raise error

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Start at the head node
        node = self.head
        # Create a flag to track if we have found the given item
        found = False
        # Loop until we have found the given item or the node is None
        while not found and node is not None:
            # Check if the node's data matches the given item
            if node.data == item:
                # We found data matching the given item, so update found flag
                found = True
            else:
                # Skip to the next node
                node = node.next
        # Check if we found the given item or we never did and reached the tail
        if found:
            # Check if we found a node in the middle of this linked list
            if node is not self.head and node is not self.tail:
                # Update the previous node to skip around the found node
                node.prev.next = node.next
                node.next.prev = node.prev
                # Unlink the found node from its next node
                node.next = None
                node.prev = None
            # Check if we found a node at the head
            elif node is self.head and node is self.tail:
                self.head = None
                self.tail = None
            elif node is self.head:
                # Update head to the next node
                self.head = node.next
                # Unlink the found node from the next node
                node.next.prev = None
                node.next = None
            # Check if we found a node at the tail
            elif node is self.tail:
                # reset the tail
                self.tail = node.prev
                # unlink the node from prev
                node.prev.next = None
                # unlink the prev node from node
                node.prev = None
            self.size -= 1
        else:
            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
