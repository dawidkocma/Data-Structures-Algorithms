class Graph:
    """
    A simple undirected graph implementation using an adjacency list.
    Supports adding/removing vertices and edges, and printing the graph.
    """
    def __init__(self):
        # Use a dictionary to map each vertex to a list of its neighbors
        self.adj_list = {}
    
    def print_graph(self):
        """
        Print each vertex and its adjacency list.
        """
        for vertex, neighbors in self.adj_list.items():
            # Show vertex and its list of connected vertices
            print(vertex, ":", neighbors)
            
    def add_vertex(self, vertex):
        """
        Add a new vertex to the graph if it doesn't already exist.
        Returns True if added, False if vertex already present.
        """
        # Only add if vertex is not already a key in the adjacency list
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []  # Initialize empty neighbor list
            return True
        # Vertex already exists
        return False
    
    def add_edge(self, v1, v2):
        """
        Create an undirected edge between v1 and v2.
        Returns True on success, False if one or both vertices are missing.
        """
        # Both vertices must exist in the graph
        if v1 in self.adj_list and v2 in self.adj_list:
            # Append each vertex to the other's adjacency list
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        # One or both vertices not found
        return False

    def remove_edge(self, v1, v2):
        """
        Remove the undirected edge between v1 and v2.
        Returns True if removal attempted, False if vertices missing.
        Uses try/except to handle missing edge gracefully.
        """
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                # Attempt to remove v2 from v1's list
                self.adj_list[v1].remove(v2)
                # Attempt to remove v1 from v2's list
                self.adj_list[v2].remove(v1)
            except ValueError:
                # If v2 not in v1's list (or vice versa), ignore
                pass
            return True
        # One or both vertices not found
        return False


# Example usage:
if __name__ == "__main__":
    # Instantiate a new Graph
    my_graph = Graph()
    
    # Add vertices A, B, C, D
    my_graph.add_vertex('A')  # True
    my_graph.add_vertex('B')  # True
    my_graph.add_vertex('C')  # True
    my_graph.add_vertex('D')  # True

    # Create edges: A--B, B--C, C--A
    my_graph.add_edge('A', 'B')  # True
    my_graph.add_edge('B', 'C')  # True
    my_graph.add_edge('C', 'A')  # True

    print("Graph after adding edges:")
    my_graph.print_graph()
    # A: ['B', 'C']
    # B: ['A', 'C']
    # C: ['B', 'A']
    # D: []

    # Remove an existing edge and a non-existing one
    my_graph.remove_edge('A', 'B')  # True, removes A-B connection
    my_graph.remove_edge('A', 'D')  # True, but no edge to remove (caught by exception)

    print("\nGraph after removing edges:")
    my_graph.print_graph()
    # A: ['C']
    # B: ['C']
    # C: ['B', 'A']
    # D: []
