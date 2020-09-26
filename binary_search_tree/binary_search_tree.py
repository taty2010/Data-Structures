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
from collections import deque
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
               self.left = BSTNode(value)
            else:
                self.left.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        print(self.value)
        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        else:
            return True

    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        while current.right:
            current = current.right
        return current.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        #base case = no children
        if self.left is None and self.right is None:
            return
        #go left, call fn(value)
        if self.left:
            self.left.for_each(fn)
        #go right, call fn(value)
        if self.right:
            self.right.for_each(fn)
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.value is None:
            return
        if self.left is not None:    
            self.left.in_order_print()
        print(self.value)
        if self.right is not None:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # Create a queue to keep track of nodes we are processing
        # add 'self' to front of the queue
        queue = deque([])
        queue.append(self)
        # while something is still in the queue
        while len(queue) > 0:
            current = queue.popleft()
            print(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        # (not done processing all nodes)
            #dequueue node from the front of the queue
            # call 'print()'
            #enqueue its left and right children

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        #Create a STACK to keep track of nodes we are processing
        # push 'self' into stack
        stack = []
        stack.append(self)
        #while something still in the stack
        # not done processing all nodes
        while len(stack) > 0:
            # pop the node off the top of the stack
            node = stack.pop()
            #call 'print()'
            print(node.value)
            # push it left and right children onto the stack
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        #-----------------------------------
        # RECURSIVE
        print(self.value)
        # base case - self has no children (no, left or right)
        #recursive case - self has +1 children
        if self.left:
            self.left.dft_print()
        if self.right:
            self.right.dft_print()
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)
        if self.left is not None:
            self.left.pre_order_dft()
        if self.right is not None:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.value is None:
            return
        if self.left is not None:    
            self.left.post_order_dft()
        if self.right is not None:
            self.right.post_order_dft()
        print(self.value)

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
bst.in_order_print()
print("post order")
bst.post_order_dft()  
