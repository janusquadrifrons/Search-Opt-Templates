# greedy search

# The graph is represented as a dictionary where the keys are the nodes and the values are lists of tuples
# Each tuple represents an edge and contains the destination node and the weight of the edge

Graf = {
    "A" : [("B",12), ("C",4)],
    "B" : [("D",7), ("E",3)],
    "C" : [("F",8), ("G",2)],
    "D" : [],
    "E" : [("H",0)],
    "F" : [("H",0)],
    "G" : [("H",0)]    
}

# The EnIyi function performs a greedy search to find the shortest path 
# from the start node to the target node in the graph

def EnIyi(Baslangic, Hedef, Graf, Kuyruk=[], ZiyaretEdildi=[]):
    # If the start node has not yet been visited, add it to the list of visited nodes and print it
    if Baslangic not in ZiyaretEdildi:
        print(Baslangic + "→", end=(""))
        ZiyaretEdildi.append(Baslangic)
    # Add all the unvisited neighbors of the current node to the queue and sort them by edge weight
    Kuyruk = Kuyruk + [x for x in Graf[Baslangic] if x[0][0] not in ZiyaretEdildi]
    Kuyruk.sort(key=lambda x:x[1])
    # If the first node in the queue is the target node, print it and end the search
    if Kuyruk[0][0] == Hedef:
        print("→" + Kuyruk[0][0])
    # Otherwise, remove the first node from the queue and search from that node
    else:
        Isleniyor=Kuyruk[0]
        Kuyruk.remove(Isleniyor)
        EnIyi(Isleniyor[0], Hedef, Graf, Kuyruk, ZiyaretEdildi)

# Test the EnIyi function by searching for the shortest path from node A to node H
EnIyi("A", "H", Graf)