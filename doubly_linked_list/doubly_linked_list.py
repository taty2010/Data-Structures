"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def delete(self):
        if self.prev:
            self.next.prev = self.prev
        if self.next:
            self.prev.next = self.next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        #create new_node
        new_node = ListNode(value)
        if self.head is None: #adding to an empty list
            self.head = new_node
            self.tail = new_node
        
        else:#adding to non empty list
             # head -> tail -> None    newNode 
            new_node.next = self.head # newNode -> head
            self.head.prev = new_node # newNode   <- head
            self.head = new_node # head = newNode
            # newHead -> oldHead -> tail -> None
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        old_head = self.head
        if self.head == None:# remove head from empty list
            return None   
        if self.head is self.tail:
            self.head = None
            self.tail = None 
        elif self.tail.prev is self.head:
            old_head = self.tail.prev
            self.tail.prev = None # head -> tail <-> None
            self.head.next = None
            self.head = self.tail
        else:
            self.head.next = None # head  tail <-> None
        self.length -= 1
        return old_head.value
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.tail is None:# Add tail to empty list
            self.head = new_node
            self.tail = new_node
        else:# Add tail to populated list 
            # currHead <-> currTail <-> None    NewNode
            # currTail -> newNode
            new_node.prev = self.tail
            self.tail.next = new_node  # 1 -> 30 # 1 <- 30
            self.tail = new_node
            # currTail <- newNode
            # newNode = tail     
        self.length += 1  
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        old_tail = self.tail
        if self.tail == None:# remove head from empty list
            return None    
        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.head.next is self.tail:
            self.head.next = None # head -> tail <-> None
            self.tail.prev = None
            self.head = self.tail
        else:
            curr_node = self.head
            while curr_node.next is not self.tail:
                curr_node = curr_node.next
            curr_node.next = None
            self.tail.prev = None
            self.tail = curr_node # head  tail <-> None
        return old_tail.value
        self.length -= 1     
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        #1. delete from current position
        #2. add_to_head()
        if self.head.next is self.tail: # head <-> tail <-> None
            node = self.tail # node is self.tail
            self.head.next = None # head <- tail
            self.tail.prev = None # head tail
            node.next = self.head # node -> head
            self.head.prev = node # node <-> head
            self.head = node #head(node) <-> tail(prev_head)
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node): # 40 <-> 1
        node = self.head
        if self.head.next is self.tail: # head <-> tail <-> None
            # node = self.head # node is self.tail
            self.head.next = None
            self.tail.prev = None
            self.tail.next = node
            node.prev = self.tail
            self.head = self.tail
            self.tail = node  # 1 <-> 40
        else: # 40 <-> 1 <-> 4
            curr_node = self.head # curr_node is 40
            while curr_node.next is not None:
                curr_node = curr_node.next
            #curr_node is now 4(tail)
            self.head.next = None
            self.head.next.prev = None
            curr_node.next = node
            node.prev = curr_node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        #Don't need to return value
        #Do need to update head, tail
        if self.head is None:
            return None
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head: #list has +2 nodes
            self.head = node.next
            node.delete()
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
        self.length -= 1
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is self.tail: 
            return max(self.head)
