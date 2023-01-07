# iterative deepening search

Graf = {
    "A" : ["B","C"],
    "B" : ["D","E"],
    "C" : ["F","G"],
    "D" : [],
    "E" : [],
    "F" : [],
    "G" : []
}

ZiyaretEdildi = []
Kuyruk = []
Hedef = "F"

def bfs(ZiyaretEdildi, Graf, Dugum):
    ZiyaretEdildi.append(Dugum)
    Kuyruk.append(Dugum)
    while Kuyruk:
        s = Kuyruk.pop(0)
        print(s + "--->", end = "")
        for Komsu in Graf[s]:
            if Komsu in Graf[s]:
                if Komsu not in  ZiyaretEdildi:
                    ZiyaretEdildi.append(Komsu)
                    Kuyruk.append(Komsu)
                    if Hedef in ZiyaretEdildi:
                        break

bfs(ZiyaretEdildi, Graf, "A")