# Nama		: Ahmad Alexander
# NIM		: 24010316140048
# Tanggal	: 28 November 2020
# Deskripsi	: Tugas Tree

from TreeB import *

# 1
# fungsi RepPostfix
# def spek
# RepPostfix : pohon biner --> list of element
# RepPostfix (P) memberikan representasi linier (dalam bentuk list)
# dengan urutan elemen list sesuai dengan urutan penulisan pohon secara postfix
# /L R A\
# Realisasi
def RepPostfix(P):
    if IsOneElmtPB(P):
        return [Akar(P)]
    else:
        if IsUnerLeft(P):
            return RepPostfix(Left(P)) + [Akar(P)]
        elif IsBiner(P):
            return RepPostfix(Left(P)) + RepPostfix(Right(P)) + [Akar(P)]
        elif IsUnerRight(P):
            return RepPostfix(Right(P)) + [Akar(P)]


# aplikasi 1
print(RepPostfix(P1))
print(RepPostfix(P2))

# 2
# fungsi RepInfix
# def spek
# RepInfix : pohon biner --> list of element
# RepInfix (P) memberikan representasi linier (dalam bentuk list)
# dengan urutan elemen list sesuai dengan urutan penulisan pohon secara infix
# /L A R\
# Realisasi
def RepInfix(P):
    if IsOneElmtPB(P):
        return [Akar(P)]
    else:
        if IsUnerLeft(P):
            return [Akar(P)] + RepInfix(Left(P))
        elif IsBiner(P):
            return RepInfix(Left(P)) + [Akar(P)] + RepInfix(Right(P))
        elif IsUnerRight(P):
            return [Akar(P)] + RepInfix(Right(P))


# aplikasi 2
print(RepInfix(P1))
print(RepInfix(P2))

# 3
# fungsi Tinggi
# def spek
# Tinggi : pohon biner --> integer
# Tinggi (P) memberikan banyaknya level dari pohon biner
# akar merupakan level 0
def Tinggi(P):
    if IsTreeEmpty(P) or IsOneElmtPB(P):
        return 0
    else:
        if Tinggi(Left(P)) > Tinggi(Right(P)):
            return Tinggi(Left(P)) + 1
        else:
            return Tinggi(Right(P)) + 1


# aplikasi 3
print(Tinggi(P0))
print(Tinggi(P1))
print(Tinggi(P2))


# 4
# fungsi SumLRDaun
# def spek
# SumLRDaun : pohon biner --> integer
# SumLRDaun (P) menjumlahkan daun paling kiri dan daun paling kanan
# Realisasi
def SumLRDaun(P):
    if IsOneElmtPB(P) or IsTreeEmpty(P):
        return 0
    return SumLRDaun(Left(P)) + Akar(P) + SumLRDaun(Right(P))


# Aplikasi
print(SumLRDaun(P1))

# 5
# fungsi IsMember
# def spek
# IsMember : pohon biner --> boolean
# IsMember (P,x) menentukan apakah elemen x merupakan
# anggota dari pohon biner bersangkutan
# Realisasi
def IsMember(P, x):
    if not IsTreeEmpty(P):
        if Akar(P) == x:
            return True
        elif IsMember(Left(P), x):
            return True
        else:
            return IsMember(Right(P), x)
    else:
        return False


# Aplikasi
print(IsMember(P1, 1))
print(IsMember(P1, 4))
print(IsMember(P1, 5))
print(IsMember(P1, 10))
print(IsMember(P2, "a"))
print(IsMember(P2, "X"))
