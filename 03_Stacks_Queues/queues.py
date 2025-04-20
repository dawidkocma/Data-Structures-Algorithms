class Node:
    """
    A Node represents an element in a linked list.
    Each node holds a value and a reference to the next node.
    """
    def __init__(self, value):
        # Store the node’s value
        self.value = value
        # Initialize next pointer to None (no next node yet)
        self.next = None
        

class Queue:
    """
    A Queue data structure using a singly linked list.
    Supports FIFO behavior with O(1) enqueue and dequeue.
    """
    def __init__(self, value):
        # Create the first node from the initial value
        new_node = Node(value)
        # Both front and rear point to this first node
        self.first = new_node
        self.last = new_node
        # Track number of elements
        self.length = 1
        
    def print_queue(self):
        """
        Traverse the queue from front to back,
        printing each node’s value.
        """
        temp = self.first
        # Continue until we reach the end (None)
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def enqueue(self, value):
        """
        Add a new value to the end of the queue.
        """
        new_node = Node(value)
        # If the queue is empty, new node is both front and rear
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            # Link current last node to the new node
            self.last.next = new_node
            # Update last pointer
            self.last = new_node
        # Increment size counter
        self.length += 1

    def dequeue(self):
        """
        Remove and return the node at the front of the queue.
        Returns None if the queue is empty.
        """
        # Nothing to remove if empty
        if self.length == 0:
            return None
        
        # Temporarily store the node to remove
        temp = self.first
        # If there's only one element, reset queue to empty
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            # Move front pointer to next node
            self.first = self.first.next
            # Detach the removed node
            temp.next = None
            
        # Decrement size counter
        self.length -= 1
        # Return the removed node
        return temp

# Example usage:
my_queue = Queue(4)   # Queue: [4]
my_queue.enqueue(5)   # Queue: [4, 5]
my_queue.enqueue(6)   # Queue: [4, 5, 6]
my_queue.dequeue()    # Removes 4; Queue: [5, 6]
my_queue.print_queue()  # Prints:
                        # 5
                        # 6
