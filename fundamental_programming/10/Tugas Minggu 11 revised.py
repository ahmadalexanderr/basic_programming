# Nama      : Ahmad Alexander
# NIM		: 24010316140048
# Tanggal	: 19 November 2020
# Deskripsi	: Tugas List

from ListofList import *
from ListOfInt import *
import numpy as np

L1 = [1, 2, 3, 4, 4, 4, 5, 5, 6]
L2 = ["I", "n", "f", "o", "r", "m", "a", "t", "i", "k", "a"]
L3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
L4 = [2, 3, [1, 2, 4], [6, 7, 8]]

# 1
# DefSpek
# IsVokal : char --> boolean
# IsVokal (V) bernilai benar jika V adalah huruf vokal
# Realisasi
def IsVokal(V):
    return (
        V.lower() == "a"
        or V.lower() == "e"
        or V.lower() == "i"
        or V.lower() == "o"
        or V.lower() == "u"
    )


# aplikasi
print(IsVokal("a"))  # True
print(IsVokal("O"))  # True
print(IsVokal("B"))  # False

# 2
# DefSpek
# KaliMatrix : Integer, list of list --> list
# KaliMatrix (k, L) menghasilkan matrix dalama bentuk list
# yang telah dikali dengan suatu konstanta K
def KaliMatrix(k, L):
    if IsList(L):
        if not IsEmpty(L):
            return k * np.array(L)
        else:
            return L
    else:
        return 0


def KaliMatrix2(k, L):
    if IsEmpty(L):
        return []
    else:
        if IsAtom(FirstElmt2(L)):
            return Konso(FirstElmt2(L) * k, KaliMatrix2(k, Tail2(L)))
        elif IsList(FirstElmt2(L)):
            return Konso(KaliMatrix2(k, FirstElmt2(L)), KaliMatrix2(k, Tail2(L)))


# aplikasi : KaliMatrix(2, L3) --> [[2,4,6],[8,10,12],[14,16,18]]
print(KaliMatrix(2, L3))  # [[2,4,6],[8,10,12],[14,16,18]]
print(KaliMatrix2(2, L3))  # [[2,4,6],[8,10,12],[14,16,18]]
# 3
# DefSpek
# SumElmtX : Integer, list --> integer
# SumElmtX (X, L) menjumlahkan nilai elemen matrix tanpa elemen bernilai X
def SumElmtX(X, L):
    if IsList(L):
        if IsEmpty(L):
            return 0
        elif IsList(FirstElmt(L)):  # ngecek list of list
            return SumElmtX(X, FirstElmt(L)) + SumElmtX(X, Tail(L))
        elif FirstElmt(L) == X:
            return 0 + SumElmtX(X, Tail(L))
        else:
            return FirstElmt(L) + SumElmtX(X, Tail(L))
    else:
        return 0


# aplikasi : SumElmtX(5, L1) --> 24
print(SumElmtX(5, L1))  # 24

# 4
# DefSpek
# NbList : list of list --> integer
# NbList (L) menghitung jumlah list dalam list L
def NbList(L):
    if IsList(L):
        if IsEmpty(L):
            return 0
        elif IsList(FirstElmt(L)):
            return 1 + NbList(Tail(L))
        elif type(FirstElmt(L)) == int:
            return NbList(Tail(L))
        else:
            return 0
    else:
        return 0


# aplikasi : NbList(L4) --> 2
#            NbList(L3) --> 3
#            NbList(L2) --> 0
print(NbList(L4))  # 2
print(NbList(L3))  # 3
print(NbList(L2))  # 0

# 5
# DefSpek
# NbVokal : list of char --> integer
# NbVokal(l) menghitung banyak elemen vokal dalam list
def NbVokal(l):
    vokal = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    if IsList(l):
        if IsEmpty(l):
            return 0
        else:
            if IsMember(FirstElmt(l), vokal):
                return 1 + NbVokal(Tail(l))
            else:
                return NbVokal(Tail(l))
    else:
        return 0


# aplikasi: NbVokal(L2) --> 5
print(NbVokal(L2))  # 5

# 6
# DefSpek
# SumElmtExceptX : Integer, list of integer --> integer
# SumElmtExceptX(x,L) menjumlahkan nilai elemen list tanpa elemen bernilai x
def SumElmtExceptX(x, L):
    if IsListInt(L):
        if IsEmpty(L):
            return 0
        elif FirstElmt(L) == x:
            return 0 + SumElmtExceptX(x, Tail(L))
        else:
            return FirstElmt(L) + SumElmtExceptX(x, Tail(L))
    else:
        return 0


# aplikasi SumElmtExceptX(4, L1) --> 22
print(SumElmtExceptX(4, L1))  # 22

# 7
# DefSpek
# SetElmtXzero : Integer, list of integer --> list of integer
# SetElmtXzero(x,L) menghasilkan list baru yang mengganti setiap elemen x menjadi 0
def SetElmtXzero(x, L):
    if IsListInt(L):
        if not IsEmpty(L):
            if FirstElmtI(L) == x:
                return Konso(FirstElmtI(L) * 0, SetElmtXzero(x, TailI(L)))
            else:
                return Konso(FirstElmtI(L), SetElmtXzero(x, TailI(L)))
        else:
            return L
    else:
        return 0


# aplikasi SetElmtXzero(5, L1)
print(SetElmtXzero(5, L1))  # [1,2,3,4,4,4,0,0,6]

# 8
# DefSpek
# IsListPrime(L) : list of integer --> boolean
# IsListPrime(L) bernilai true jika setiap elemen list adalah bilangan prima
def IsListPrime(L):
    if IsListInt(L) or not IsEmpty(L):
        if FirstElmtI(L) <= 2:
            if FirstElmtI(L) == 2:
                return True
            else:
                return False
        elif FirstElmtI(L) % 2 == 0:
            return False
        else:
            return IsListPrime(TailI(L))
    else:
        return False


# aplikasi IsListPrime(L)
print(IsListPrime([3, 2, 5, 7, 11]))
print(IsListPrime([1, 2, 3, 4, 7, 8, 9]))

# 9
# DefSpek
# InsertAfter(x,L,e) : list --> list
# InsertAfter(x,L,e) menghasilkan list baru dimana menambahkan elemen x setelah elemen e
def InsertAfter(x, L, e):
    if IsList(L):
        if IsEmpty(L) or IsAtom(L):
            return L
        else:
            if FirstElmt(L) == e:
                return konso(konso(Tail(L), x), FirstElmt(L))
            else:
                return konso(InsertAfter(x, Tail(L), e), FirstElmt(L))
    else:
        return 0


# aplikasi
print(InsertAfter(17, [3, 2, 5, 7, 11], 5))

# 10
# DefSpek
# SortMax(L) : list of integer --> list of integer
# SortMax(L) menghasilkan list baru dimana mengurutkan elemen dari yang terbesar ke terkecil
def SortMax(L):
    if len(L) < 2:
        return L
    else:
        i = L.index(max(L))
        return [L[i]] + SortMax(L[:i] + L[i + 1 :])


print(SortMax(L1))

