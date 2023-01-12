# Traveler Salesman with Random Hill Climbing

# Implement necessary libraries
import random
import numpy as np
import networkx as nx

# The array of x,y coordinates for each city
Coor = np.array([[1,2], [30,22], [56,23], [8,18], [20,50], [3,4], [11,6], [6,7], [15,20], [10,9], [12,12], [46,17], [60,55], [100,80], [16,12]])

# Generate distance matrice from coordinates
def MatrisUret(Coor):
    Matris=[]
    for i in range(len(Coor)):
        for j in range(len(Coor)):
            p = np.linalg.norm(Coor[i] - Coor[j]) # Euclidean distance between city pairs
            Matris.append(p)
    Matris = np.reshape(Matris, (len(Coor), len(Coor)))
    print(" Matris : ")
    print(Matris)
    return Matris

# Take the distance matrice and return a random initial solution
def Cozum(Matris):
    Noktalar = list(range(0, len(Matris)))
    Cozum = []
    for i in range(0, len(Matris)):
        RastgeleNokta = Noktalar[random.randint(0, len(Noktalar) - 1)]
        Cozum.append(RastgeleNokta)
        Noktalar.remove(RastgeleNokta)
    return Cozum

# Take the disatnce matrice and the solution then calculate total distance of the route
def YolUzunlugu(Matris, Cozum):
    DonguUzunlugu = 0
    for i in range(0, len(Cozum)):
        DonguUzunlugu += Matris[Cozum[i]][Cozum[i-1]]
    return DonguUzunlugu

# Take the distance matrice and the the solution then generate all possible neighboring solutions
# by swapping two cities in the current solution. Then calculate the total distance of each neighboring solution
# Then return the best one.
def Komsular(Matris, Cozum):
    Komsular = []
    for i in range(len(Cozum)):
        for j in range(i+1, len(Cozum)):
            Komsu = Cozum.copy()
            Komsu[i] = Cozum[j]
            Komsu[j] = Cozum[i]
            Komsular.append(Komsu)

    EnIyiKomsu = Komsular[0]
    EnIyiYol = YolUzunlugu(Matris, EnIyiKomsu)

    for Komsu in Komsular:
        MevcutYol = YolUzunlugu(Matris, Komsu)
        if MevcutYol < EnIyiYol:
            EnIyiYol = MevcutYol
            EnIyiKomsu = Komsu
    
    return EnIyiKomsu, EnIyiYol

# Take coordinates and call helper functions defined to generate an initial solution and its neighboring solutions.
# Then iterate for a better solution until no better one can be found.
def TepeTırmanma(Kordinat):
    Matris = MatrisUret(Kordinat)

    MevcutCozum = Cozum(Matris)
    MevcutYol = YolUzunlugu(Matris, MevcutCozum)
    Komsu = Komsular(Matris, MevcutCozum)[0]
    EnIyiKomsu, EnIyiKomsu_path = Komsular(Matris, Komsu)

    return MevcutYol, MevcutCozum

# Generate final solution then visualize
def Graf(Kordinat):
    SonCozum = TepeTırmanma(Kordinat)
    G = nx.DiGraph()
    Gecici = SonCozum[1]
    G.add_nodes_from(SonCozum[1])

    for i in range(1, len(SonCozum[1])):
        G.add_edge(Gecici[i-1], Gecici[i])
    G.add_edge(Gecici[len(Gecici) - 1], Gecici[0])

    RenkliHarita = []

    for Dugum in G:
        if Dugum == SonCozum[1][0]:
            RenkliHarita.append("lime")
        else:
            RenkliHarita.append("plum")

    nx.draw(G, with_labels = True, node_color = RenkliHarita, node_size = 1000)

    print("Bulunan Çözüm = \n", SonCozum[1], "\n Bulunan Yol Uzunluğu : ", SonCozum[0])

    return

# Run
Graf(Coor)
