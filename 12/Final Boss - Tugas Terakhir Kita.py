"""
NIM             : 24010316140048
Nama            : Ahmad Alexander
Deskripsi       : Tugas Terakhir Praktikum B1
Tanggal         : 10 Desember 2020
"""

from ListofList import *
from TreeB import *

# LIST#
L1 = []
L2 = [1, 2, 3]
L3 = [1, [2, 3], [4]]
L4 = ["u", "n", "d", "i" "p"]

# MATRIX#
M2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
M1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# SET#
H1 = [4, 5, 6]
H2 = []

# TREE#
P1 = [1, [2, [3, [], []], [4, [], []]], [5, [], []]]
P2 = [2, [], []]

"""""" "LIST" """"""
"""1"""
# DefSpek
# SumElmtX : Integer, List of integer --> integer
# SumElmtX (X, L) menjumlahkan nilai elemen list tanpa elemen bernilai X
# Realisasi
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


L = [1, 2, 3, 4, 5]
# Aplikasi : SumElmtX(5, L) --> 10
print(SumElmtX(5, L))

"""2"""
# DefSpek
# MaxList : List of integer --> Integer
# MaxList(L) menghasilkan nilai elemen terbesar dari list L
# Realisasi
def MaxList(L):
    if IsOneElmt(L):
        return FirstElmt(L)
    else:
        if MaxList(Tail(L)) > FirstElmt(L):
            return MaxList(Tail(L))
        else:
            return FirstElmt(L)


L = [2, 4, 5, 1]
# Aplikasi : MaxList(L) --> 5
print(MaxList(L))


# Hint : Untuk memudahkan, buat fungsi untuk mengecek nilai maksimum

"""3"""
# DefSpek
# MinList : List of integer --> Integer
# MinList(L) menghasilkan nilai elemen terkecil dari list L
# Realisasi
def MinList(L):
    if IsOneElmt(L):
        return FirstElmt(L)
    else:
        if MinList(Tail(L)) < FirstElmt(L):
            return MinList(Tail(L))
        else:
            return FirstElmt(L)


L = [2, 4, 5, 1]
# Aplikasi : MinList(L) --> 1
print(MinList(L))

"""4"""
# DefSpek
# UraikanListOfList : List of list --> List
# UraikanListOfList(L) menghasilkan hasil penguraian dari List of list L menjadi list biasa
# Realisasi
def UraikanListOfList(L):
    if not L:
        return []
    if isinstance(FirstElmt(L), list):
        return UraikanListOfList(FirstElmt(L)) + UraikanListOfList(Tail(L))
    else:
        return [FirstElmt(L)] + UraikanListOfList(Tail(L))


L = [1, [2, 3], 4, [5]]
# Aplikasi : UraikanListOfList(L) --> [1, 2, 3, 4, 5]
print(UraikanListOfList(L))

"""5"""
# DefSpek
# ListMaxMin : List of integer --> List
# ListMaxMin(L) membuat List dengan anggotanya hanya 2 elemen yaitu elemen terbesar dan terkecil dari list L
# Realisasi
def ListMaxMin(L):
    if not IsEmpty(L):
        if not IsOneElmt(L):
            return [MinList(L)] + [MaxList(L)]
        else:
            return L
    else:
        return []


L = [4, 2, 5, 3, 7, 1]
# Aplikasi : ListMaxMin(L) ---> [1, 7]
print(ListMaxMin(L))

"""6"""
# DefSpek
# SetElmtXzero : Integer, list of integer --> list of integer
# SetElmtXzero(L,3) menghasilkan list baru yang mengganti setiap elemen x menjadi 0
# Realisasi
def SetElmtXzero(L, x):
    if IsListInt(L):
        if not IsEmpty(L):
            if FirstElmt(L) == x:
                return Konso(FirstElmt(L) * 0, SetElmtXzero(Tail(L), x))
            else:
                return Konso(FirstElmt(L), SetElmtXzero(Tail(L), x))
        else:
            return L
    else:
        return 0


L = [1, 2, 3, 4, 5]
# Aplikasi : SetElmtXzero(L,3) --> [1, 2, 0, 4, 5]
print(SetElmtXzero(L, 3))

"""7"""
# DefSpek
# XPos : List of char --> Integer
# XPos(L,X) menghasilkan posisi index dari char X yang dicari
# Realisasi
def XPos(L, X):
    if IsListChar(L) and not IsEmpty(L):
        if FirstElmt(L) == X:
            index = L.index(FirstElmt(L))
            return index
        else:
            return 1 + XPos(Tail(L), X)


L = ["j", "a", "y", "a"]
# Aplikasi : XPos(L,'a') --> 1
# Hint : Index dimulai dari 0. Huruf 'a' pada contoh di atas berada pada POSISI INDEX ke-1 dari list L
#          Jika ada lebih dari satu karakter yang sama, return index karakter pertama yang ketemu
print(XPos(L, "a"))

"""8"""
# DefSpek
# SortMax(L) : list of integer --> list of integer
# SortMax(L) menghasilkan list baru dimana mengurutkan elemen dari yang terbesar ke terkecil
# Hint : Ada di diktat, tinggal ubah sedikit
# Realisasi
def SortMax(L):
    if NbElmt(L) < 2:
        return L
    else:
        # i = L.index(max(L))
        # return [L[i]] + SortMax(L[:i] + L[i + 1 :])
        return Insort(L)


print(SortMax(L2))

"""""" "SET" """"""
"""9"""
# DefSpek
# RemberAll : Set --> Empty Set
# RemberAll(H) menghapus semua elemen pada set H
# Realisasi
def RemberAll(H):
    if IsEmpty(H):
        return []
    if not IsEmpty(H):
        return Konso([], RemberAll(Tail(H)))
    else:
        return RemberAll(Tail(H))


H = [1, 2, 3, 4]
# Aplikasi : RemberAll(H) --> []
# Hint : Jangan langsung return []
print(RemberAll(H))

"""""" "TREE" """"""
"""10"""
# DefSpek
# TinggiPohon : Binary Tree --> Integer
# TinggiPohon(P) menghasilkan tinggi dari pohon P (Tinggi pohon dimulai dari 1)
#                4              --Level 1
#             /     \
#           2         5         --Level 2
#         /
#       1                       --Level 3
# Realisasi
def TinggiPohon(P):
    if IsTreeEmpty(P) or IsOneElmtPB(P):
        return 1
    else:
        if TinggiPohon(Left(P)) > TinggiPohon(Right(P)):
            return TinggiPohon(Left(P)) + 1
        else:
            return TinggiPohon(Right(P)) + 1


P = [4, [2, [1, [], []], [[], [], []]], [5, [], []]]
# Aplikasi : TinggiPohon(P) --> 3
# Hint : Hati-hati dengan perbedaan tinggi Left(P) dan Right(P)
print(TinggiPohon(P))

"""11"""
# DefSpek
# IsBalanceTree : Binary Tree  --> Boolean
# IsBalanceTree(P) mengecek apakah pohon P merupakan balance tree
#                4
#             /     \
#           2         5
#         /             \
#       1                 6
def IsBalanceTree(P):
    if IsTreeEmpty(P) or IsOneElmtPB(P):
        return True
    else:
        if TinggiPohon(Left(P)) == TinggiPohon(Right(P)):
            return True
        else:
            return False


P = [4, [2, [1, [], []], [[], [], []]], [5, [], [[6], [], []]]]
# Aplikasi : IsBalanceTree(P) --> True
# Hint : Balance tree bernilai true ketika selisih tinggi pohon Right dan Left tidak lebih dari 1
#        : ATAU selisih banyaknya node Right dan Left tidak lebih dari 1
print(IsBalanceTree(P))

"""12"""
# DefSpek
# Terkiri : Binary Search Tree --> Node dalam integer
# Terkiri(P) menghasilkan node terkiri dari pohon P
#                7
#             /     \
#           2         8
#         /   \      /
#       1       3  6
#                  /
#                 5
# Realisasi
def Terkiri(P):
    if not IsTreeEmpty(P):
        if IsExistLeft(P):
            if IsTreeEmpty(Akar(Left(P))):
                return Akar(Left(P))
            else:
                return Terkiri(Left(P))
        else:
            return Akar(P)
    else:
        return None


P = [7, [2, [1, [], []], [3, [], []]], [8, [6, [[5], [], []], []], []]]
# Aplikasi : Terkiri(P) --> 1
# Hint : Node terkiri selalu node paling kecil dari BinarySearchTree
print(Terkiri(P))

"""13"""
# DefSpek
# IsSkewRight : Binary Tree  --> Node atau integer
# IsSkewRight(P) mengecek apakah pohon P condong kanan
def IsSkewRight(P):
    if IsTreeEmpty(P):
        return False
    else:
        if IsOneElmtPB(P):
            return True
        else:
            if IsUnerRight(P):
                return IsSkewRight(Right(P))
            else:
                return False


# P1
#                7
#                  \
#                    8
#                      \
#                        9
#                         \
#                           10
P1 = [7, [], [8, [], [9, [], [10, [], []]]]]
# Aplikasi : IsSkewRight(P1) --> True
print(IsSkewRight(P1))

# P2
#                7
#             /     \
#           2         8
#         /   \      /
#       1       3  6
#                  /
#                 5
P2 = [7, [2, [1, [], []], [3, [], []]], [8, [6, [5, [], []], []], []]]
# Aplikasi : IsSkewRight(P2) --> False
print(IsSkewRight(P2))
"""""" "SOAL BONUS" """"""
"""Buat latihan aja, nggak usah dikumpulin"""
"""999"""
# DefSpek
# ReversePohon : Binary Tree  --> Tree
# ReversePohon(P) menghasilkan pohon P yang sudah di reverse
def ReversePohon(P):
    P[1], P[2] = P[2], P[1]
    if IsExistLeft(P):
        ReversePohon(P[1])
    if IsExistRight(P):
        ReversePohon(P[2])
    return P


P = [1, [2, [4, [8, [], []], [9, [], []]], [5, [], []]], [3, [6, [], []], [7, [], []]]]
print(ReversePohon(P))

#                1
#             /      \
#           2          3
#         /   \      /    \
#       4      5   6      7
#      / \
#     8   9

# Aplikasi : ReversePohon(P) -->
P = [1, [3, [7, [], []], [6, [], []]], [2, [5, [], []], [4, [9, [], []], [8, [], []]]]]

print(ReversePohon(P))

#                1
#             /      \
#           3          2
#         /   \      /    \
#       7      6   5      4
#                           / \
#                          9   8

