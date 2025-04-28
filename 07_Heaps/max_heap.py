class MaxHeap:
    """
    A Max-Heap implementation using a Python list.
    Supports insert (heapify-up) and remove (extract max with heapify-down).
    The largest element is always at index 0.
    """
    def __init__(self):
        # Initialize an empty list to hold heap elements
        self.heap = []
        
    def _left_child(self, index):
        # Return index of left child for given parent index
        return 2 * index + 1
    
    def _right_child(self, index):
        # Return index of right child for given parent index
        return 2 * index + 2
    
    def _parent(self, index):
        # Return index of parent for given child index
        return (index - 1) // 2
    
    def _swap(self, index1, index2):
        # Swap two elements in the heap by index
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        
    def _sink_down(self, index):
        """
        Move element at index down to its correct position to maintain max-heap property.
        Repeatedly swap with the larger of its children if needed.
        """
        # Track position that may need to move
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            # Compare left child
            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            # Compare right child
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            # If a child is larger, swap and continue sinking
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                # Correct position found
                return
        
    def insert(self, value):
        """
        Insert a new value into the heap.
        Append at end then "heapify-up" by swapping with parent while larger.
        """
        # Add new value at the end
        self.heap.append(value)
        # Start at the new element's index
        current = len(self.heap) - 1
        # While not at root and current is greater than its parent, swap up
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            parent_idx = self._parent(current)
            self._swap(current, parent_idx)
            current = parent_idx
    
    def remove(self):
        """
        Remove and return the max element (root of the heap).
        Replace root with last element, pop it, then sink-down to restore heap.
        Returns None if heap is empty.
        """
        # Empty heap case
        if not self.heap:
            return None
        # Single element case
        if len(self.heap) == 1:
            return self.heap.pop()
        # Store max to return
        max_value = self.heap[0]
        # Move last element to root and shrink list
        self.heap[0] = self.heap.pop()
        # Restore max-heap property by sinking root down
        self._sink_down(0)
        return max_value

# Example usage:
if __name__ == "__main__":
    myheap = MaxHeap()
    # Insert multiple values
    for val in [95, 75, 80, 55, 60, 50, 65]:
        myheap.insert(val)
    # Heap list representation
    print("Heap array after inserts:", myheap.heap)
    # Remove top two elements
    print("Removed max:", myheap.remove())  # 95
    print("Heap array:", myheap.heap)
    print("Removed max:", myheap.remove())  # 80
    print("Heap array:", myheap.heap)
