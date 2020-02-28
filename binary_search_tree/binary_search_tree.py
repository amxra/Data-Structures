import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # LEFT CASE
        # check if our new nodes value is less than the current nodes value
            # does it have a child to the left?
                # place our new node here
            # otherwise
                # repeat process for the left

        if value < self.value:
            if not self.left:
                node = BinarySearchTree(value)
                self.left = node
            else:
                self.left.insert(value)

        # RIGHT CASE
        # check if the new nodes value is greater than or equal to the current nodes value
            # does it have a child to the right?
                # place our new node here
            # otherwise
                # repeat the process for the right
        
        if value >= self.value:
            if not self.right:
                node = BinarySearchTree(value)
                self.right = node
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # BASE CASE
        if self.value == target:
            return True
        
        # LEFT CASE
        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)

        # RIGHT CASE
        if target > self.value:
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # base case
        # if empty tree
            # return none
        if not self.value:
            return None

        # recursive case
        # if there is no right value 
            # return the root node value

        if not self.right:
            return self.value
        else:
            return self.right.get_max()
        # otherwise
            # return get max of the right hand child
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)

        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
    if node.left:
            self.in_order_print(node.left)

        print(node.value)

        if node.right:
            self.in_order_print(node.right)

            # Print the value of every node, starting with the given node,
            # in an iterative breadth first traversal
    def bft_print(self, node):
            # create an empty queue
        q = Queue()
         # add the starting node to the queue
        q.enqueue(node)

                # iterate over the queue
        while q.len() > 0:
             # set the current_node to the first item in the q
            current_node = q.dequeue()
                # then print the current value
            print(current_node.value)
                # if the current node has a left child
            if current_node.left:
                # call enqueue on the current left
                q.enqueue(current_node.left)
                # if the current node has a right child
            if current_node.right:
                # call enqueue on the current right
                q.enqueue(current_node.right)

            # Print the value of every node, starting with the given node,
            # in an iterative depth first traversal
    def dft_print(self, node):
            # create an empty stack
        s = Stack()
            # add the starting node to the stack
        s.push(node)

            # iterate over the stack
        while s.len() > 0:
                # set the current_node to the first item in the stack
            current_node = s.pop()
                # then print the current value
            print(current_node.value)
                # if the current node has a left child
            if current_node.left:
                # call push on the current left
                s.push(current_node.left)
             # if the current node has a right child
            if current_node.right:
                # call push on the current right
                s.push(current_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass