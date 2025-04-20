# Node represents an element in a singly linked list.
class Node:
    def __init__(self, value):
        # Store the data value for this node
        self.value = value
        # Pointer to the next node in the list (None if no next)
        self.next = None


class Stack:
    """
    A Stack data structure (LIFO) implemented via a singly linked list.
    Supports O(1) push and pop operations.
    """
    def __init__(self, value):
        # Initialize the stack with a single node containing the provided value
        new_node = Node(value)
        # 'top' always points to the topmost node in the stack
        self.top = new_node
        # Track number of elements in the stack
        self.height = 1
        
    def print_stack(self):
        """
        Traverse from the top of the stack downwards,
        printing each node's value.
        """
        temp = self.top
        # Continue until end of the linked list
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def push(self, value):
        """
        Add a new value to the top of the stack.
        """
        new_node = Node(value)
        
        # If stack is empty, new node becomes the top
        if self.height == 0:
            self.top = new_node
        else:
            # Otherwise, link new node to current top and update top pointer
            new_node.next = self.top
            self.top = new_node
        
        # Increase the count of elements
        self.height += 1
    
    def pop(self):
        """
        Remove and return the top node from the stack.
        Returns None if the stack is empty.
        """
        # Nothing to pop if stack is empty
        if self.height == 0:
            return None
        
        # Hold reference to the node being removed
        temp = self.top
        # Move top pointer to the next node down
        self.top = self.top.next
        # Detach popped node from the list
        temp.next = None
        # Decrease the count of elements
        self.height -= 1
        # Return the removed node
        return temp


# Example usage:
my_stack = Stack(4)    # Stack: [4]
my_stack.push(4)       # Stack: [4, 4]
my_stack.push(11)      # Stack: [11, 4, 4]
my_stack.push(22)      # Stack: [22, 11, 4, 4]
my_stack.push(12)      # Stack: [12, 22, 11, 4, 4]

# Pop the top element (12) and print its value
print(my_stack.pop().value, "\n")  # Output: 12

# Print remaining stack contents from top to bottom:
my_stack.print_stack()  
# 22
# 11
# 4
# 4
