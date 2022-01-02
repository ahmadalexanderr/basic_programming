# Nama		: Ahmad Alexander
# NIM		: 24010316140048
# Tanggal	: 28 November 2020
# Deskripsi	: Modul Tree B

from TreeA import *

# Fungsi NbElmt
# DefSpek
# NbElmt : pohon biner --> integer >= 0
# NbElmt (P) memberikan banyaknya elemen dari pohon P
# basis : NbElmt (//\\) = 0
# rekurens : NbElmt (/L, A, R\) =  NbElmt (L) + 1 (NbElmt P)
def NbElmtPB(P):
    if IsOneElmtPB(P):
        return 1
    else:
        if IsBiner(P):
            return NbElmtPB(Left(P)) + 1 + NbElmtPB(Right(P))
        elif IsUnerLeft(P):
            return NbElmtPB(Left(P)) + 1
        elif IsUnerRight(P):
            return 1 + NbElmtPB(Right(P))


# Fungsi NbDaun
# DefSpek
# NbDaun : pohon biner --> integer
# NbDaun (P) memberikan banyaknya daun dari pohon Pohon
def NbDaunPB(P):
    if IsOneElmtPB(P):
        return 1
    else:
        if IsBiner(P):
            return NbDaunPB(Left(P)) + NbDaunPB(Right(P))
        elif IsUnerLeft(P):
            return NbDaunPB(Left(P))
        elif IsUnerRight(P):
            return NbDaunPB(Right(P))


# Fungsi RepPrefix
# DefSpek
# RepPrefix : pohon biner --> list of element
# RepPrefix (P) memberikan representasi linier (dalam bentuk list)
# dengan urutan elemen list sesuai dengan urutan penulisan pohon secara prefix
# /A L R\
def RepPrefix(P):
    if IsOneElmtPB(P):
        return [Akar(P)]
    else:
        if IsBiner(P):
            return [Akar(P)] + RepPrefix(Left(P)) + RepPrefix(Right(P))
        elif IsUnerLeft(P):
            return [Akar(P)] + RepPrefix(Left(P))
        elif IsUnerRight(P):
            return [Akar(P)] + RepPrefix(Right(P))


# Fungsi SumDaun
# DefSpek
# SumDaun : pohon biner --> integer
# SumDaun (P) memberikan jumlah daun dari pohon P
def SumDaun(P):
    if IsOneElmtPB(P):
        return Akar(P)
    else:
        if IsBiner(P):
            return SumDaun(Left(P)) + SumDaun(Right(P))
        elif IsUnerLeft(P):
            return SumDaun(Left(P))
        elif IsUnerRight(P):
            return SumDaun(Right(P))


# Fungsi SumElmt
# DefSpek
# SumElmt : pohon biner --> integer
# SumElmt (P) memberikan jumlah setiap elemen dari pohon P
def SumElmt(P):
    if IsOneElmtPB(P):
        return Akar(P)
    else:
        if IsBiner(P):
            return SumElmt(Left(P)) + Akar(P) + SumElmt(Right(P))
        elif IsUnerLeft(P):
            return SumElmt(Left(P)) + Akar(P)
        elif IsUnerRight(P):
            return Akar(P) + SumElmt(Right(P))

