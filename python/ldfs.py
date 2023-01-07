Graf = {
    "A" : ["B","C"],
    "B" : ["D","E"],
    "C" : ["F","G"],
    "D" : [],
    "E" : [],
    "F" : [],
    "G" : []
}

def ldfs(Baslangic, Hedef, Yol, Seviye, maxD):
    print("Geçerli Seviye --->", Seviye)
    Yol.append(Baslangic)
    if Baslangic == Hedef:
        print("Hedef deneme başarılı...")
        return Yol
    print("Hedef düğüm denemesi başarısız")
    if Seviye==maxD :
        return False
    print("Geçerli düğüm ilerletiliyor...",Baslangic)
    for Cocuk in Graf[Baslangic]:
        if ldfs(Cocuk, Hedef, Yol, Seviye+1, maxD):
            return Yol
        Yol.pop()
    return False
Baslangic = "A"
Hedef = input("Hedef düğümü girin : ")
maxD = int(input("Maximum derinlik seviyesi sınırını girin : "))
print()
Yol = list()
res = ldfs(Baslangic, Hedef, Yol, 0, maxD)
if(res):
    print("--Hedef düğüm uygun yol--")
    print("Yol", Yol)
else:
    print("--Bu derinlik seviye sınırında Hedef düğüme uygun Yol Yok")
