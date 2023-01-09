from collections import deque

class Dugum:
    def __init__(self, Deger, Komsular=[]):
        self.Deger = Deger
        self.Komsular = Komsular
        self.SagZiyaret = False
        self.SolZiyaret = False
        self.SagDallar = None
        self.SolDallar = None

def CiftYonlu(s, t):
    def YolCikar(Dugum):
        DugumKopyala = Dugum

        Yol = []

        while Dugum:
            Yol.append(Dugum.Deger)
            Dugum = Dugum.SagDallar

        Yol.reverse()

        del Yol[-1]

        while DugumKopyala:
            Yol.append(DugumKopyala.Deger)
            DugumKopyala = DugumKopyala.SolDallar
        
        return Yol

    if s == t:
        return [s.Deger]

    q = deque([])
    q.append(s)
    q.append(t)
    s.SagZiyaret = True
    t.SolZiyaret = True

    while len(q) > 0:
        n = q.pop()
        if n.SolZiyaret and n.SagZiyaret:
            return YolCikar(n)
        for Dugum in n.Komsular:
            if n.SolZiyaret == True and not Dugum.SolZiyaret:
                Dugum.SolDallar = n
                Dugum.SolZiyaret = True
                q.append(Dugum)
            if n.SagZiyaret == True and not Dugum.SagZiyaret:
                Dugum.SagDallar = n
                Dugum.SagZiyaret = True
                q.append(Dugum)
    return None

n0 = Dugum("A")
n1 = Dugum("B")
n2 = Dugum("C")
n3 = Dugum("D")
n4 = Dugum("E")
n5 = Dugum("F")
n6 = Dugum("G")
n1.Komsular = [n0]
n2.Komsular = [n0]
n3.Komsular = [n1]
n4.Komsular = [n1]
n5.Komsular = [n2]
n6.Komsular = [n2]
print(CiftYonlu(n4,n6))
