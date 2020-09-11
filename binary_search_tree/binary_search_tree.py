from collections import deque

"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # No node exists
        if not self.value:
            self.value = BSTNode(value)
        # General Case
        else:
            # Left subtree case
            if value < self.value:
                # No child node exists
                if not self.left:
                    # If no child node, set self.left to new node
                    self.left = BSTNode(value)
                # Child node exists
                else:
                    # If child exists, recursively loop
                    self.left.insert(value)
            # Right subtree case
            else:
                # No child node exists
                if not self.right:
                    # If no child node, set self.right to new node
                    self.right = BSTNode(value)
                # Child node exists
                else:
                    self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Root node = Target
        if self.value == target:
            return True
        elif target < self.value:
            # No child node to check
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # Only need to check right subtrees for max value
        if not self.right:
            # If no right child exists, current value is greatest value
            return self.value
        else:
            # Recursive
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Perform function on current node
        fn(self.value)

        # If a left child exists, perform recursion
        if self.left:
            self.left.for_each(fn)

        # If a right child exists, perform recursion
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # If left child exists
        if self.left:
            # Recursively move through left children
            # Call function on left child (makes the new self current self.left)
            self.left.in_order_print()
        # Once there are no left children, print current node value
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # use deque to handle queue

    def bft_print(self, node):
        # Create a queue
        q = deque()
        # Add root to queue
        q.append(node)
        # Iterate over queue, adding children of current_node to queue
        while len(q) > 0:
            # Use dual functionality of popleft() to dequeue and retrieve first position node
            current_node = q.popleft()
            # Add children of current node to queue if exist
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            # Print current node value
            print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Proceed similarly as the bft but use stack
        s = deque()
        s.append(node)

        while len(s) > 0:
            current_node = s.pop()
            if current_node.left:
                s.append(current_node.left)
            if current_node.right:
                s.append(current_node.right)
            print(current_node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()
