from queue import LinkedQueue

class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # Check if both left child and right child have no value
        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # Check if either left child or right child has a value
        return self.left is not None or self.right is not None

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Best case: O(1) if the height is 0
        Worst case: O(n) if we start from the root"""
        left_height = -1
        right_height = -1
        if self.left is not None: # Check if left child has a value 
            left_height = self.left.height() # if so calculate its height
        if self.right is not None: # Check if right child has a value 
            right_height = self.right.height() # if so calculate its height
        if self.right == None and self.left == None:
            return 0
        # Return one more than the greater of the left height and right height
        # return left_height + 1 if left_height >= right_height else right_height + 1
        return max(left_height, right_height) + 1
    
    def left(self):
        if self.left is not None:
            return True
        return False
    
    def right(self):
        if self.right is not None:
            return True
        return False
        
class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None or self.size == 0

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        Best and worst case: O(n)"""
        # Check if root node has a value and if so calculate its height
        if self.root is not None:
            return self.root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        Best case: O(1) if the item is the root
        Worst case: O(n) if the tree is very unbalanced
        Worst cast with balanced tree: o(log(n))"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        Best case: O(1) if the item is the root
        Worst case: O(n) if the tree is very unbalanced
        Worst cast with balanced tree: o(log(n))"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # TODO: Return the node's data if found, or None
        return node.data if self.contains(item) else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        Best case: O(1) if the tree is empty
        Worst case: O(n) if the tree is very unbalanced
        Worst cast with balanced tree: o(log(n))"""
        if self.is_empty(): # Handle the case where the tree is empty
            self.root = BinaryTreeNode(item) # Create a new root node
            self.size += 1 # Increase the tree size
            return 
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item, self.root)
        if item < parent.data and parent.left == None: # Check if the given item should be inserted left of parent node
            parent.left = BinaryTreeNode(item)  # Create a new node and set the parent's left child
            self.size += 1 # Increase the tree size
        elif item > parent.data and parent.right == None: # Check if the given item should be inserted right of parent node
            parent.right = BinaryTreeNode(item) # Create a new node and set the parent's right child 
            self.size += 1 # Increase the tree size

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        Best case: O(1) if the tree is empty
        Worst case: O(n) if the tree is very unbalanced
        Worst cast with balanced tree: o(log(n))"""
        node = self.root # Start with the root node
        while node is not None: # Loop until we descend past the closest leaf node
            if node.data == item: # Check if the given item matches the node's data
                return node # Return the found node
            elif item < node.data: # Check if the given item is less than the node's data
                node = node.left # Descend to the node's left child
            elif item > node.data:  # Check if the given item is greater than the node's data
                node = node.right # Descend to the node's right child
        return None # Not found

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        Best case: O(1) if the tree is empty
        Worst case: O(n) if the tree is very unbalanced
        Worst cast with balanced tree: o(log(n))"""
        if node is None: # Check if starting node exists
            return None # Not found (base case)
        elif node.data == item: # Check if the given item matches the node's data
            return node # Return the found node
        elif item < node.data:  # Check if the given item is less than the node's data
            return self._find_node_recursive(item, node.left) # Recursively descend to the node's left child, if it exists
        elif item > node.data: # Check if the given item is greater than the node's data
            return self._find_node_recursive(item, node.right) # Recursively descend to the node's right child, if it exists

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        Best case: O(1) if the tree is empty
        Worst case: O(n) if the tree is very unbalanced
        Worst cast with balanced tree: O(log(n))"""
        node = self.root # Start with the root node and keep track of its parent
        parent = None 
        while node is not None: # Loop until we descend past the closest leaf node
            if node.data == item: # Check if the given item matches the node's data
                return parent # Return the parent of the found node
            elif item < node.data: # Check if the given item is less than the node's data
                parent = node # Update the parent
                node = node.left # descend to the node's left child
            elif item > node.data:  # Check if the given item is greater than the node's data
                parent = node # Update the parent
                node = node.right # descend to the node's right child
        return parent # Not found

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        if node is None: # Check if starting node exists
            return parent # Not found (base case)
        if item == node.data: # Check if the given item matches the node's data
            return parent  # Return the parent of the found node
        elif item < node.data: # Check if the given item is less than the node's data
             # Recursively descend to the node's left child, if it exists
            return self._find_parent_node_recursive(item, node.left, node)
        elif item > node.data: # Check if the given item is greater than the node's data
            # Recursively descend to the node's right child, if it exists
            return self._find_parent_node_recursive(item, node.right, node)

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        Best case: O(1) if the tree is empty
        Worst case: O(n) if the tree is very unbalanced
        Worst cast with balanced tree: O(log(n))"""
        # TODO: Use helper methods and break this algorithm down into 3 cases
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases
        parent = self._find_parent_node_recursive(item, self.root)
        if parent is None:
            raise ValueError("Item not found")
        
        if item < parent.data: # check if the item is on the left of the parent
            node = parent.left # store the value of our deleted item
            if node.left is None and node.right is None:
                parent.left = None
            elif node.left is None:
                parent.left = node.right
            elif node.right is None:
                parent.left = node.left
            else:
                parent.left = node.left # add the left side of our node to the parent
                # add the right side of the node to the rightmost decendant of our deleted node
                new_parent = self._find_parent_node_recursive(node.data, parent.left)
                new_parent.left = node.left 
        elif item > parent.data: # check if the item is on the right of the parent
            node = parent.right # store the value of our deleted item
            if node.left is None and node.right is None:
                parent.right = None
            elif node.left is None:
                parent.right = node.right
            elif node.right is None:
                parent.right = node.left
            else:
                parent.right = node.left # add the right side of our node to the parent
                # add the left side of the node to the leftmost decendant of our deleted node
                new_parent = self._find_parent_node_recursive(node.data, parent.right)
                new_parent.right = node.right
    
    def remove(self, item):
        parent = self._find_parent_node_recursive(item, self.root) # find the parent of the node containing item
        if parent is None: # if not found  
            raise ValueError("Item not found") # raise value err
        if item < parent.data: # check if the item is on the left of the parent
            node = parent.left # store the value of our deleted item
        elif item > parent.data: # check if the item is on the right of the parent
            node = parent.right # store the value of our deleted item
        if node.is_leaf():
            if item < parent.data: # check if the item is on the left of the parent
                parent.left = None
            else:
                parent.right = None
        elif node.right == None:
            if item < parent.data: # check if the item is on the left of the parent
                parent.left = node.left
            else: # otherwise item is on the right of the parent
                parent.right = node.left
        elif node.left == None:
            if item < parent.data: # check if the item is on the left of the parent
                parent.left = node.right
            else: # otherwise item is on the right of the parent
                parent.right = node.right
        else: # node has 2 children
            nodes_right_child = node.right
            # 
            # find the parent of the leftmost node

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) because we must visit each node
        Memory usage: O(h) where h is the height of the tree"""
        # Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_in_order_recursive(node.left, visit)
        # Visit this node's data with given function
        visit(node.data)
        # Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_in_order_recursive(node.right, visit)    

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) because we must visit each node
        Memory usage: O(h) where h is the height of the tree"""

        # TODO: Traverse in-order without using recursion (stretch challenge)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) because we must visit each node
        Memory usage: O(h) where h is the height of the tree"""
        # Visit this node's data with given function
        visit(node.data)
        # Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_pre_order_recursive(node.left, visit)
        # Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_post_order_recursive(node.left, visit)
        # Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_post_order_recursive(node.right, visit)
        # Visit this node's data with given function
        visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        Running time: ??? Why and under what conditions?
        Memory usage: ??? Why and under what conditions?"""
        # Create queue to store nodes not yet traversed in level-order
        queue = LinkedQueue()
        # Enqueue given starting node
        queue.enqueue(start_node)
        # Loop until queue is empty
        while not queue.is_empty():
            # Dequeue node at front of queue
            node = queue.dequeue()
            # Visit this node's data with given function
            visit(node.data)
            # Enqueue this node's left child, if it exists
            if node.left is not None:
                queue.enqueue(node.left)
            # Enqueue this node's right child, if it exists
            if node.right is not None:
                queue.enqueue(node.right)

def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
