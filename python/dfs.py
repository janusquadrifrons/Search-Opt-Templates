Graf = {
    "A" : ["B","C"],
    "B" : ["D","E"],
    "C" : ["F","G"],
    "D" : [],
    "E" : [],
    "F" : [],
    "G" : []
}

Target = "F"
ZiyaretEdildi = set()
def dfs(ZiyaretEdildi, Graf, Dugum):
    if Dugum not in ZiyaretEdildi:
        print (Dugum+"--->", end="")
        ZiyaretEdildi.add(Dugum)
        for Komsu in Graf[Dugum]:
            if Target in ZiyaretEdildi:
                break
            else:
                dfs(ZiyaretEdildi, Graf, Komsu)
dfs(ZiyaretEdildi, Graf, "A")