class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Print list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            # Set the pointer to the next node
            temp = temp.next

    # Add an item at the end of the list BigO(n)
    def append(self, value):
        new_node = Node(value)
        # Edge case: List is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
        
    # Pop an item of the end of a list
    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        # Edge case: Only 1 item in the list
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
        
    # Add an item to the beggining of the list
    def prepend(self, value):
        new_node = Node(value)
        # Edge case: No items in the list
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True # Optional
    
    # Pop first item from the list
    def pop_first(self):
        # Edge case: No item in the list
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        # Edge case: there was only one item in the list
        # tail still pointed to the last node
        if self.length == 0:
            self.tail = None
        return temp
            
    # Get item at a given index
    def get(self, index):
        # Edge case: provided index is out of range
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    # Set new value at a given index
    def set_value(self, index, value):
        temp = self.get(index)
        # index exists
        if temp:
            temp.value = value
            return True
        return False
    
    # Insert a node at a given index
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.head
        # Get a pointer before required index
        for _ in range(index - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    # Remove an item at a particural index
    def remove(self, index):
        if index < 0 or index >= self.length:
            # Expected to return a node, so False will not satisfy 
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        # Assign a pointer to previous node
        prev = self.get(index - 1)
        temp = prev.next # O(1) way of setting the temp variable
        
        # Remove the required node and set the index-1 pointer to index+1 node
        prev.next = temp.next
        temp.next = None
        self.length -=1
        return temp
    
    # Reverse
    def reverse(self):
        #pointers -> (before)(temp)(after)
        # Set temp to the head pointer
        temp = self.head
        # Switch head with tail
        self.head = self.tail
        self.tail = temp
        # Initialize after pointer 
        after = temp.next
        # Initialize before pointer
        before = None
        # Traverse through linked list
        for _ in range (self.length):
            # Revert the node pointers while traversing the loop 
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
# Write and Run your tests here

# my_linked_list = LinkedList(4)
# my_linked_list.append(2)
# my_linked_list.prepend(1)

# # print(my_linked_list.pop())
# # print(my_linked_list.pop())

# # print(my_linked_list.pop_first())
# my_linked_list.print_list()
