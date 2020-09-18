# TODO a class that represent the individual elements in our LL

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    def get_value(self):
        return self.value
    def get_next_node(self):
        return self.next_node
    def set_next_node(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None
    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            #update head and tail attributes
            self.head = new_node
            self.tail = new_node
        else:
            # TODO time permitting
            # set next_node of my new Node to the head
            new_node.set_next_node(self.head)
            # Update the head attribute
            self.head = new_node
    def add_to_tail(self, value):
        # Create a new node
        new_node = Node(value)
        #1. LL is emplty
        if self.head is None:
            #update head and tail attribute
            self.head = new_node
            self.tail = new_node
        #2. LL is not empty
        else:
            #update next_node of our tail
            self.tail.set_next_node(new_node)
            #update self.tail
            self.tail = new_node
    def remove_head(self):
        # Empty List
        if self.head == None:
            return None
        else: #Return value of the old head
            ret_value = self.head.get_value()
            #list with 1 element
            if self.head == self.tail:
              self.head = None
              self.tail = None
            else:#list with 2+ elements
              self.head = self.head.get_next_node()
            return ret_value
    def remove_tail(self):
        if self.head == None: #Is the list empty?
            return None
        ret_value = self.tail.get_value()
        if self.head == self.tail:#If there is only one item in the list
            self.head = None
            self.tail = None
        else:
            curr_node = self.head
            while curr_node.get_next_node() is not self.tail:
                curr_node = curr_node.get_next_node()
            #update pointer of temp node (prev_tail) to None
            curr_node.set_next_node(None)
            self.tail = curr_node

        return ret_value

    def contains(self, value):
        #loop through ll until next pointer is None
        cur_node = self.head
        while cur_node.get_value() == value:
            return True
        return False
    def get_max(self):
        # TODO time permitting
        pass