# Node constructor for Doubly Linked List
class Node:
    def __init__(self, value):
        self.value = value        # Store node value
        self.next = None          # Pointer to next node
        self.prev = None          # Pointer to previous node

class DoublyLinkedList:
    def __init__(self, value):
        """
        Initialize the Doubly Linked List with a single node.
        """
        new_node = Node(value)    # Create the initial node
        self.head = new_node      # Set head to the new node
        self.tail = new_node      # Set tail to the new node
        self.length = 1           # List now contains one node

    def print_list(self):
        """
        Traverse and print all node values in the list.
        """
        temp = self.head                     # Start at the head
        while temp is not None:              # Loop until the end of the list
            print(temp.value)                # Print current node's value
            temp = temp.next                 # Move to the next node

    def append(self, value):
        """
        Add a node with the given value at the end of the list.
        
        Returns:
            True after successful append.
        """
        new_node = Node(value)               # Create a new node with the provided value
        # Check if the list is empty
        if self.head is None:
            self.head = new_node             # New node becomes head
            self.tail = new_node             # New node also becomes tail
        else:
            self.tail.next = new_node        # Link current tail's next to the new node
            new_node.prev = self.tail        # Set new node's previous to current tail
            self.tail = new_node             # Update tail to new node
        self.length += 1                     # Increment length of the list
        return True                          # Return confirmation

    def pop(self):
        """
        Remove and return the value of the last node in the list.
        
        Returns:
            The value of the removed node, or None if the list is empty.
        """
        # Check if list is empty
        if self.length == 0:
            return None

        temp = self.tail                     # Store current tail in temp for return
        # Case: Only one node in the list
        if self.length == 1:
            self.head = None                 # Reset head to None
            self.tail = None                 # Reset tail to None
        else:
            self.tail = self.tail.prev       # Update tail to previous node
            self.tail.next = None            # Sever link to removed node
            temp.prev = None                 # Clear removed node's previous pointer
        self.length -= 1                     # Decrement list length
        return temp.value                    # Return the value of removed node

    def prepend(self, value):
        """
        Add a node with the given value at the beginning of the list.
        
        Returns:
            True after successful prepend.
        """
        new_node = Node(value)               # Create a new node with the provided value
        # Check if the list is empty
        if self.length == 0:
            self.head = new_node             # New node becomes head
            self.tail = new_node             # New node also becomes tail
        else:
            new_node.next = self.head        # Point new node's next to current head
            self.head.prev = new_node        # Set current head's previous to new node
            self.head = new_node             # Update head to new node
        self.length += 1                     # Increase list length
        return True                          # Return confirmation

    def pop_first(self):
        """
        Remove and return the first node in the list.
        
        Returns:
            The removed node, or None if the list is empty.
        """
        # Return None if list is empty
        if self.length == 0:
            return None

        temp = self.head                     # Store current head in temp for return
        # Case: Only one node in the list
        if self.length == 1:
            self.head = None                 # Reset head to None
            self.tail = None                 # Reset tail to None
        else:
            self.head = self.head.next       # Update head to next node
            self.head.prev = None            # Clear new head's previous pointer
            temp.next = None                 # Clear removed node's next pointer
        self.length -= 1                     # Decrement list length
        return temp                          # Return the removed node

    def get(self, index):
        """
        Retrieve the node at the specified index.
        
        Parameters:
            index (int): Position of node to retrieve.
        
        Returns:
            The node at the given index, or None if index is out of range.
        """
        # Check if the index is out of range
        if index < 0 or index >= self.length:
            return None
        
        # Decide direction of traversal for efficiency
        if index < self.length / 2:
            temp = self.head               # Start from head if index is in the first half
            for _ in range(index):
                temp = temp.next           # Move forward node by node
        else:
            temp = self.tail               # Start from tail if index is in the latter half
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev           # Move backward node by node

        return temp                      # Return node found at index

    def set_value(self, index, value):
        """
        Set the value of the node at the specified index.
        
        Parameters:
            index (int): Position of node to update.
            value: New value to assign.
        
        Returns:
            True if successful, False if index not found.
        """
        temp = self.get(index)           # Retrieve the node at the given index
        if temp:
            temp.value = value           # Update the node's value
            return True                  # Return success flag
        return False                     # Return failure flag if no node at index

    def insert(self, index, value):
        """
        Insert a node with the given value at the specified index.
        
        Parameters:
            index (int): Position to insert the new node.
            value: Value for the new node.
        
        Returns:
            True if insertion was successful, False if index is invalid.
        """
        # Validate index bounds (index must be between 0 and length inclusive)
        if index < 0 or index > self.length:
            return False
        # If inserting at the beginning, reuse prepend method
        if index == 0:
            return self.prepend(value)
        # If inserting at the end, reuse append method
        if index == self.length:
            return self.append(value)

        new_node = Node(value)           # Create the new node
        before = self.get(index - 1)     # Retrieve node just before target index
        after = before.next              # The node currently at the target index
        
        new_node.prev = before           # Link new node's previous to before
        new_node.next = after            # Link new node's next to after
        before.next = new_node           # Update before's next to new node
        after.prev = new_node            # Update after's previous to new node

        self.length += 1                 # Increment list length
        return True                      # Confirm successful insertion

    def remove(self, index):
        """
        Remove the node at the specified index from the list.
        
        Parameters:
            index (int): Position of the node to remove.
        
        Returns:
            The removed node if successful, or False if index is invalid.
        """
        # Index out of bounds
        if index < 0 or index >= self.length:
            return False
        # If removing the first node, reuse pop_first method
        if index == 0:
            return self.pop_first()
        # If removing the last node, reuse pop method
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)            # Get the node to be removed
        # Adjust the pointers to bypass the node to be removed
        temp.prev.next = temp.next        # Link previous node to next node
        temp.next.prev = temp.prev        # Link next node back to previous node
        
        # Clear the removed node's pointers
        temp.next = None
        temp.prev = None

        self.length -= 1                  # Decrement list length
        return temp                       # Return the removed node

                
my_ddl = DoublyLinkedList(1)
my_ddl.append(2)
my_ddl.append(3)
my_ddl.print_list()
print("--------")
print("Pop:", my_ddl.pop())
my_ddl.prepend(4)
my_ddl.print_list()
print("---------")
print("Pop First:", my_ddl.pop_first().value)
my_ddl.append(3)
my_ddl.append(4)
my_ddl.append(5)

print("Print List")
my_ddl.print_list()
print("Get node:", my_ddl.get(4).value)
my_ddl.set_value(2,77)
my_ddl.print_list()

my_ddl.remove(2)
print("Get list:")
my_ddl.print_list()