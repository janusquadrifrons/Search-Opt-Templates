from collections import deque

"""
The CiftYonlu function first checks if s and t are the same node. 
If they are, it returns a list containing the value of s.
Otherwise, it initializes an empty queue q, and adds s and t to q. 
It sets the SagZiyaret attribute of s to True and the SolZiyaret attribute of t to True.
It then enters a loop which continues until the queue is empty. 
In each iteration of the loop, it removes a node n from the front of the queue. 
If the SolZiyaret attribute of n is True and the SagZiyaret attribute of n is True, then it means that a path has been found between s and t, so the function calls the YolCikar helper function to extract the path and return it.
If n has not been visited by both searches, the function iterates over the neighbors of n and adds them to the queue if they have not been visited by the corresponding search. It also sets the SagDallar or SolDallar attribute of the neighbor to n, depending on the search that is being conducted.
If the loop finishes without finding a path between s and t, the function returns None.
"""

# The class representing a node in a graph
class Dugum:
    def __init__(self, Deger, Komsular=[]):
        self.Deger = Deger
        self.Komsular = Komsular # --- a list of neighboring nodes
        self.SagZiyaret = False # --- a boolean indicating whether the node has been visited while searching from s
        self.SolZiyaret = False # --- a boolean indicating whether the node has been visited while searching from t
        self.SagDallar = None # --- a reference to the previous node while traversing from s
        self.SolDallar = None # --- a reference to the previous node while traversing from t

# Function that performs a bidirectional BFS to find a path between two nodes (s & t) in a graph
def CiftYonlu(s, t):
    # Helper function that extracts the path from the previous node references
    def YolCikar(Dugum):
        # Make a copy of the node        
        DugumKopyala = Dugum

        Yol = []

        # Traverse the path from s to the node
        while Dugum:
            # Add the current node to the path
            Yol.append(Dugum.Deger)
            # Move to the next node
            Dugum = Dugum.SagDallar

        # Reverse the path from s to the node
        Yol.reverse()
        # Remove the node from the path
        del Yol[-1]

        # Traverse the path from the node to t
        while DugumKopyala:
            # Add the current node to the path
            Yol.append(DugumKopyala.Deger)
            # Move to the next node
            DugumKopyala = DugumKopyala.SolDallar
        # Return the complete path
        return Yol

    # If s and t are the same node, return the value of s
    if s == t:
        return [s.Deger]

    # Initialize an empty queue and add s and t to it
    q = deque([])
    q.append(s)
    q.append(t)
    # Mark s as visited by the search from s
    s.SagZiyaret = True
    # Mark t as visited by the search from t
    t.SolZiyaret = True

    # Continue the loop until the queue is empty
    while len(q) > 0:
        # Remove a node from the front of the queue
        n = q.pop()
        # If the node has been visited by both searches, a path has been found
        if n.SolZiyaret and n.SagZiyaret:
            # Extract the path and return it
            return YolCikar(n)
        # Iterate over the neighbors of the node
        for Dugum in n.Komsular:
            # If the node was visited by the search from s, add its neighbors
            # to the queue if they have not been visited by the search from t
            if n.SolZiyaret == True and not Dugum.SolZiyaret:
                Dugum.SolDallar = n
                Dugum.SolZiyaret = True
                q.append(Dugum)
            # If the node was visited by the search from t, add its neighbors
            # to the queue if they have not been visited by the search from s
            if n.SagZiyaret == True and not Dugum.SagZiyaret:
                Dugum.SagDallar = n
                Dugum.SagZiyaret = True
                q.append(Dugum)
    # If the loop finishes without finding a path, return None
    return None

# Create some nodes
n0 = Dugum("A")
n1 = Dugum("B")
n2 = Dugum("C")
n3 = Dugum("D")
n4 = Dugum("E")
n5 = Dugum("F")
n6 = Dugum("G")

# Set the neighbors of each node
n1.Komsular = [n0]
n2.Komsular = [n0]
n3.Komsular = [n1]
n4.Komsular = [n1]
n5.Komsular = [n2]
n6.Komsular = [n2]

# Find the path between n4 and n6
print(CiftYonlu(n4,n6))
