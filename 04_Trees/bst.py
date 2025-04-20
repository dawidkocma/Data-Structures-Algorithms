class Node:
    """
    A Node represents an element in a linked list.
    Each node holds a value and a reference to its left and right children.
    """
    def __init__(self, value):
        # Store the node's data
        self.value = value
        # Initialize lef and right child pointers to None
        self.left = None
        self.right = None
        
class BinarySearchTree:
    """
    A Binary Search Tree (BST) supporting insert and lookup operations.
    Maintains the property that for any node:
        - All values in the left subtree are less than the node's value.
        - All values in the right subtree are greater that the node's value.
        """
    def __init__(self):
        # Start with an empty tree
        self.root = None
        
    def insert(self, value):
        """
        Insert a value into the BST.
        Returns True on success.
        If the tree is empty, the new node becomes the root.
        Otherwise, taverse down the tree to find the correct spot.
        """
        
        new_node = Node(value)
        # If no root exists, set the new node as root
        if self.root == None:
            self.root = new_node
            return True
        
        temp = self.root
        # Traverse untill we insert the node or find a duplicate
        while (True):
            # If value already exists, do nothing and return True
            if new_node.value == temp.value:
                return True
            # Go left if the value is smaller than current node
            if new_node.value < temp.value:
                # If there's no left child, insert here
                if temp.left is None:
                    temp.left = new_node
                    return True
                # Otherwise, keep traversing left
                temp = temp.left
            else:
                # Go right if the value is greater
                if temp.right is None:
                    temp.right = new_node
                    return True
                # Otherwise, keep traversing right
                temp = temp.right
    
    def contians(self, value):
        """
        Check wheter a value exists in the BST.
        Returns True if found; False otherwise.
        """
        temp = self.root
        # Traverse until we exhaust the tree or find the value
        while temp is not None:
            if value < temp.value:
                # Move to left subtee for smaller values
                temp = temp.left
            elif value > temp.value:
                # Move to right subtree for larger values
                temp = temp.right
            else:
                # Found the value
                return True
            # Reached a leaf (A node without a child) without matching
        return False


# Example usage:
my_tree = BinarySearchTree()
my_tree.insert(2)      # Tree now has root = 2
my_tree.insert(1)      # 1 goes to left of 2
my_tree.insert(3)      # 3 goes to right of 2

# Verify structure by printing root and its children
print(my_tree.root.value)        # 2
print(my_tree.root.left.value)   # 1
print(my_tree.root.right.value)  # 3

# Lookup a value
print("Contains 3:", my_tree.contians(3))
