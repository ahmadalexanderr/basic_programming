# Nama file: ListOfInt.py
# Deskripsi: Membuat Tipe Bentukan List of integer
# Pembuat: Ahmad Alexander
# Tanggal: 10 November 2020

# from typing import Union, List, TypeVar

# DEFINISI DAN SPESIFIKASI TYPE
# List: kosong --> List of integer
# {List() membuat List of integer Li}
# REALISASI
# TNum = TypeVar("TNum", int, int)
def IntList():
    init_list = []
    init_list = filter(lambda i: isinstance(i, int), init_list)
    return list(init_list)


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Konso: integer, List of integer tdk kosong --> List of integer
# {Konso(e,Li): menghasilkan sebuah list dar e dan Li, dengan e sebagai elemen pertama e:
# e o L --> Li'}
# REALISASI
def Konso(E, Li):
    if IsEmpty(Li):
        if isinstance(E, int) == True:
            return [E]
        else:
            return []
    else:
        if IsListInt(Li):
            if isinstance(E, int) == True:
                return [E] + Li
            else:
                return Li
        else:
            return Li


# Kons0: List of integer tdk kosong, integer --> List of integer
# {Kons0(Li,e): menghasilkan sebuah list dari Li dan e, dengan e sebagai elemen terakhir List:
# Li 0 e --> Li'}
# REALISASI
def Kons0(Li, E):
    if IsEmpty(Li):
        if isinstance(E, int) == True:
            return [E]
        else:
            return []
    else:
        if IsListInt(Li):
            if isinstance(E, int) == True:
                return Li + [E]
            else:
                return Li
        else:
            return Li


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# FirstElmt: List of integer tidak kosong --> elemen
# {FirstElmt(Li): menghasilkan elemen pertama dari list Li}
# REALISASI
def FirstElmtI(Li):
    if not IsEmpty(Li) and IsListInt(Li):
        return Li[0]


# Tail: List of integer tidak kosong --> List of integer
# {Tail(Li): menghasilkan list tanpa elemen pertama dari list Li,
# mungkin kosong}
# REALISASI
def TailI(Li):
    if not IsEmpty(Li) and IsListInt(Li):
        return Li[1:]
    else:
        return []


# LastElmt: List of integer tidak kosong --> elemen
# {LastElmt(Li): menghasilkan element terakhir dari list Li}
# REALISASI
def LastElmtI(Li):
    if not IsEmpty(Li) and IsListInt(Li):
        return Li[-1]
    else:
        return []


# Head: List of integer tidak kosong --> List of integer
# {Head(Li): menghasilkan list tanpa elemen terakhir list Li,
# mungkin kosong}
# REALISASI
def HeadI(Li):
    if not IsEmpty(Li) and IsListInt(Li):
        return Li[:-1]


# DEFINISI DAN SPESIFIKASI PREDIKAT DASAR
# (UNTUK BASIS ANALISIS REKURENS)
# IsEmpty: List of integer --> boolean
# {IsEmpty(Li): benar jika kosong}
# REALISASI
def IsEmpty(Li):
    return Li == []


# IsOneElmt: List of integer --> boolean
# {IsOneElmt(X, Li): benar jika list Li hanya mempunyai satu elemen}
# REALISASI
def IsOneElmt(Li):
    if not IsEmpty(Li) and IsListInt(Li):
        return NbElmt(Li) == 1


# DEFINISI DAN SPESIFIKASI PREDIKAT KEABSAHAN
# IsListInt: List of integer --> boolean
# {IsListInt(Li) menghasilkan true jika Li adalah list dengan elemen integer)}
# REALISASI
def IsListInt(Li):
    if IsEmpty(Li):
        return True
    else:
        return isinstance(FirstElmt2(Li), int) and IsListInt(Tail2(Li))


# NILAI MAKSIMUM LIST INTEGER
# DEFINISI DAN SPESIFIKASI
# MaxList: list of integer tidak kosong --> integer
# {MaxList(Li): menghasilkan elemen Li yang bernilai maksimum}
# REALISASI
def MaxList(Li):
    if IsOneElmt(Li):
        return LastElmt(Li)
    else:
        return Max2(LastElmtI(Li), MaxList(HeadI(Li)))


# UKURAN LIST
# DEFINISI DAN SPESIFIKASI
# Dimensi: list of integer --> integer > 0
# {Dimensi(Li): menghasilkan banyaknya element list of integer}
# REALISASI
def Dimensi(Li):
    if IsEmpty(Li):
        return 0
    else:
        return 1 + Dimensi(TailI(Li))


# PENJUMLAHAN DUA LIST OF INTEGER
# DEFINISI DAN SPESIFIKASI
# ListPlus: 2 List of integer >= 0 --> List of integer >= 0
# {ListPlus(Li1, Li2): menjumlahkan setiap element list of integer yang berdimensi sama, hasilnya berupa list of integer berdimensi tsb.}
# REALISASI
def ListPlus(Li1, Li2):
    if Dimensi(Li1) == 0:
        return []
    else:
        return Konso(
            FirstElmtI(Li1) + FirstElmtI(Li2), ListPlus(TailI(Li1), TailI(Li2))
        )


# INSERTION SORT
# DEFINISI DAN SPESIFIKASI
# Insert: integer, List of integer, terurut membesar --> List of integer terurut membesar
# {Insert(x,Li): menghasilkan insert x ke list of integer Li terurut membesar}
# REALISASI
def Insert(x, Li):
    if IsListInt(Li):
        if IsEmpty(Li):
            return [x]
        else:
            if x <= FirstElmtI(Li):
                return Konso(x, Li)
            else:
                return Konso(FirstElmtI(Li), Insert(x, TailI(Li)))
    else:
        return 0


# DEFINISI DAN SPESIFIKASI
# Insort: List of integer --> List of integer
# {Insort(Li): menghasilkan list of integer terurut dng metode insertion sort}
# REALISASI
def Insort(Li):
    if IsListInt(Li):
        if IsEmpty(Li):
            return []
        else:
            return Insert(FirstElmtI(Li), Insort(TailI(Li)))
    else:
        return 0


# KEMUNCULAN MAX (v1)
# DEFINISI DAN SPESIFIKASI
# MaxNb: list of integer --> <integer, integer>
# {MaxNb(Li): menghasilkan <nilai max,kemunculan nilai max> dari suatu list of integer Li; <m,n> = m adlh max x dari n # occurance m dlm list}
# REALISASI
def MaxNb(Li):
    if IsListInt(Li):
        if IsOneElmt(Li):
            return (FirstElmtI(Li), 1)
        else:
            (m, n) = MaxNb(TailI(Li))
            if m < FirstElmt(Li):
                return (FirstElmtI(Li), 1)
            elif m == FirstElmtI(Li):
                return (m, 1 + n)
            elif m > FirstElmtI(Li):
                return (m, n)
    else:
        return 0


# KEMUNCULAN MAX (v2)
# DEFINISI DAN SPESIFIKASI
# MaxNb2: list of integer --> <integer, integer>
# {MaxNb2(Li): menghasilkan <nilai max,kemunculan nilai max> dari suatu list of integer Li; <m,n> = m adlh max x dari n # occurance m dlm list}
# REALISASI
def MaxNb2(Li):
    if IsListInt(Li):
        return (Max(Li), NbOcc(Max(Li), Li))
    else:
        return 0


# DEFINISI DAN SPESIFIKASI FUNGSI LAIN/PERANTARA
# NbElmt: List of integer --> integer
# {NbElmt(L): menghasilkan banyaknya elemen list, nol jika kosong}
# REALISASI
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(TailI(L))


# FirstElmt2: List tidak kosong --> elemen
# {FirstElmt2(L): menghasilkan elemen pertama dari list L}
# REALISASI
def FirstElmt2(L):
    if not IsEmpty(L):
        return L[0]


# Tail2: List tidak kosong --> List of integer
# {Tail2(L): menghasilkan list tanpa elemen pertama dari list L,
# mungkin kosong}
# REALISASI
def Tail2(L):
    if not IsEmpty(L):
        return L[1:]
    else:
        return []


# Max2: 2 integer --> integer
# {Max2(a,b): menentukan nilai maksimum dari dua bilangan integer a dan b menggunakan short-hand if}
# REALISASI
def Max2(a, b):
    if a >= b:
        return a
    else:
        return b


# Max: List of integer --> integer
# {Max(Li): menghasilkan nilai max dari elemen suatu list of integer Li}
# REALISASI
def Max(Li):
    if IsListInt(Li):
        if IsOneElmt(Li):
            return Li
        else:
            if FirstElmtI(Li) > Max(TailI(Li)):
                return FirstElmtI(Li)
            else:
                return Max(TailI(Li))
    else:
        return 0


# NbOcc: integer, List of integer --> integer > 0
# {NbOcc(X,Li): banyaknya kemunculan nilai X pada Li}
# REALISASI
def NbOcc(X, Li):
    if IsListInt(Li):
        if IsOneElmt(Li):
            if X == FirstElmtI(Li):
                return 1
            else:
                return 0
        else:
            if X == FirstElmtI(Li):
                return 1 + NbOcc(TailI(Li))
            else:
                return NbOcc(TailI(Li))
    else:
        return 0


# Vmax: List of integer --> integer
# {Vmax(Li): adlh NbOcc(Max(Li), Li) yaitu banyaknya kemunculan nilai max dari Li, dng aplikasi terhdp NbOcc(Max(Li), Li)}
# REALISASI
def Vmax(Li):
    if IsListInt(Li):
        return NbOcc(Max(Li), Li)
    else:
        return 0


# APLIKASI
# A = [2, 3, 4, 8]
# B = [90, 20, 10, 33, 56]
# C = [2, "X", "a"]
# print("List A = ", A)
# print("List B = ", B)
# print("List C = ", C)
# print("Is A List of integer? ", IsListInt(A))
# print("Is B List of integer? ", IsListInt(B))
# print("Is C List of integer? ", IsListInt(C))
# x = 11
# y = "B"
# z = 89
# D = Konso(x, B)
# E = Kons0(A, y)
# print("Konso ", x, " and", B, " equal ", D)
# print("Konso ", E, " and", y, " equal ", E)
# print("First Element of ", D, " is ", FirstElmt(D))
# print("Tail of ", D, " is ", Tail(D))
# print("Last Element of ", D, " is ", LastElmt(D))
# print("Head of ", D, " is ", Head(D))
# F = IntList()
# print("Is", F, "an empty List?", IsEmpty(F))
# print("Konso ", x, " and List ", F, " equal")
# G = Konso(z, F)
# print("Is", G, "one element?", IsOneElmt(G))
# print("Maximum element of List ", D, " is ", MaxList(D))
# print("Dimensi dari List", E, " = ", Dimensi(E))
# i = 99
# H = Kons0(E, i)
# print(H, " + ", B, " = ", ListPlus(H, B))
# print("Insert ", i, " ke List ", B, " = ", Insert(i, B))
# print("Insort List", Insert(i, B), " = ", Insort(Insert(i, B)))
# B1 = Insort(Insert(i, B))
# print("Kemunculan Max v1 pada List", B1, " = ", MaxNb(B1))
# print("Kemunculan Max v2 pada List", B1, " = ", MaxNb(B1))

