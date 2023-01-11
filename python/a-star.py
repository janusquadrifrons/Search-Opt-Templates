# A* search

# 2D array representing the graph
Graf = [
    ["A","B",1,3],
    ["A","C",2,4],
    ["B","D",4,2],
    ["B","E",6,6],
    ["C","F",3,3],
    ["C","G",2,1],
    ["D","E",7,6],
    ["D","H",5,0],
    ["F","H",1,0],
    ["G","H",2,0]]

# Temporary lists to store all unique nodes in the graph
Gecici = []
Gecici1 = []

# Add all unique nodes to the list
for i in Graf:
    Gecici.append(i[0])
    Gecici1.append(i[1])

# Create a set of unique nodes
Dugumler = set(Gecici).union(set(Gecici1))


def A_star(Graf, Maliyet, Acik, Kapali, cur_node):
    # Remove current node from open set, add to closed set
    if cur_node in Acik:
        Acik.remove(cur_node)
    Kapali.add(cur_node)

    # Iterate over edges of the graph
    for i in Graf:
        # Check if current edge is from the current node
        if(i[0] == cur_node and Maliyet[i[0]] + i[2] + i[3] < Maliyet[i[1]]):
            # Add end point of the edge to the open set
            Acik.add(i[1])
            # Update cost and path to the end point
            Maliyet[i[1]] = Maliyet[i[0]] + i[2] + i[3]
            Yol[i[1]] = Yol[i[0]] + " → " + i[1]
    # set the cost of reaching current node as high value
    Maliyet[cur_node] = 999999
    # Choose the node with the lowest cost from the open set
    Kucuk = min(Maliyet, key = Maliyet.get)


    # If the chosen node is not in the closed set, call the function again with that node as the current node
    if Kucuk not in Kapali:
        A_star(Graf, Maliyet, Acik, Kapali, Kucuk)

# Cost dictionary to store cost of reaching each node
Maliyet = dict()
Gecici_cost = dict()

# Dictionary to store path from start to end point
Yol = dict()

# initialize all cost as high value and path as empty
for i in Dugumler:
    Maliyet[i] = 999999
    Yol[i] = " "

# Create open and closed set
Acik = set()
Kapali = set()

# Prompt user for start and end point
BaslangicDugumu = input("Başlangıç Durumunu Girin : ")
Acik.add(BaslangicDugumu)
Yol[BaslangicDugumu] = BaslangicDugumu
Maliyet[BaslangicDugumu] = 0

# Call the function with the starting node as the current node
A_star(Graf, Maliyet, Acik, Kapali, BaslangicDugumu)
HedefDugum = input("Hedef Durumu Girin : ")

# Print the path from the starting node to the goal node
print("En uygun yol : ", Yol[HedefDugum])