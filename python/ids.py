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

Yol = list()

def ids (MevcutDugum, Hedef, Graf, maxD, MevcutListe):
    MevcutListe.append(MevcutDugum)
    if MevcutDugum == Hedef:
        return True
    if maxD<=0:
        Yol.append(MevcutListe)
        return False
    for Dugum in Graf[MevcutDugum]:
        if ids(Dugum, Hedef, Graf, maxD-1, MevcutListe):
            return True
        else:
            MevcutListe.pop()
    return False
def re_ids(MevcutDugum, Hedef, Graf, maxD):
    for i in range(maxD):
        MevcutListe = list()
        if ids(MevcutDugum, Hedef, Graf, i, MevcutListe):
            return True
    return False
if not re_ids("A","E",Graf,3):
    print("Uygun yol yok!")
else:
    print("Uygun yol var!")
    print(Yol.pop())
