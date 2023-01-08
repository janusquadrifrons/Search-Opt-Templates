# uniform cost search

Graf = [
    ["A","B",12],
    ["A","C",4],
    ["B","D",7],
    ["B","E",3],
    ["E","H",3],
    ["C","F",8],
    ["C","G",2],
    ["F","H",2],
    ["G","H",3]]

Gecici = []
Gecici1 = []

for i in Graf:
    Gecici.append(i[0])
    Gecici1.append(i[1])
Dugumler = set(Gecici).union(set(Gecici1))

def MaliyetOncelikli(Graf, Maliyet, Acik, Kapali, Gecerli_Dugum):
    if Gecerli_Dugum in Acik:
        Acik.remove(Gecerli_Dugum)
    Kapali.add(Gecerli_Dugum)

    for i in Graf:
        if(i[0] == Gecerli_Dugum and Maliyet[i[0]]+i[2] < Maliyet[i[1]]):
            Acik.add(i[1])
            Maliyet[i[1]] = Maliyet[i[0]]+i[2]
            Yol[i[1]] = Yol[i[0]] + "→" + i[1]
    Maliyet[Gecerli_Dugum] = 999999
    Kucuk = min(Maliyet, key=Maliyet.get)
    if Kucuk not in Kapali:
        MaliyetOncelikli(Graf, Maliyet, Acik, Kapali, Kucuk)

    Maliyet = dict()
    Gecici_cost = dict()
    Yol = dict()

    for i in Dugumler:
        Maliyet[i] = 999999
        Yol[i] = " "

    Acik = set()
    Kapali = set()
    Baslangic_Dugumu = input ("Baslangıç Düğümünü Girin : ")
    Acik.add(Baslangic_Dugumu)
    Yol[Baslangic_Dugumu] = Baslangic_Dugumu
    Maliyet[Baslangic_Dugumu] = 0

    MaliyetOncelikli(Graf, Maliyet, Acik, Kapali, Baslangic_Dugumu)

    HedefDugumu = input("Hedef Düğümü Giriniz : ")

    print("En az maliyetli yol : ", Yol[HedefDugumu])