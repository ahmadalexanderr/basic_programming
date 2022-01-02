# Nama file: List.py
# Deskripsi: Membuat Tipe Bentukan List
# Pembuat: Ahmad Alexander
# Tanggal: 3 November 2020

# DEFINISI DAN SPESIFIKASI TYPE
# List: kosong --> list
# {List() membuat list L}
# REALISASI
def List():
    return []


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Konso: elemen, List --> List
# {Konso(e, L): menghasilkan sebuah list dari e dan L,
# dengan e sebagai elemen pertama e: e o L --> L'}
# REALISASI
def Konso(E, L):
    if L == []:
        return [E]
    else:
        return [E] + L


# Kons0: List, elemen --> List
# {Kons0(L,e): menghasilkan sebuah list dari L dan e,
# dengan e sebagai elemen pertama e: L 0 e --> L'}
# REALISASI
def Kons0(L, E):
    if L == []:
        return [E]
    else:
        return L + [E]


# DEFINISI DAN SPESIFIKASI SELEKTOR O
# FirstElmt: list tidak kosong --> elemen
# {FirstElmt(L): menghasilkan elemen pertama dari list L}
# REALISASI
def FirstElmt(L):
    return L[0]


# Tail: List tidak kosong --> List
# {Tail(L): menghasilkan list tanpa elemen pertama dari list L,
# mungkin kosong}
# REALISASI
def Tail(L):
    return L[1:]


# LastElmt: List tidak kosong --> element
# {LastElmt(L): menghasilkan element terakhir dari list L}
# REALISASI
def LastElmt(L):
    if not IsEmpty(L):
        return L[-1]


# Head: List tidak kosong --> List
# {Head(L): menghasilkan list tanpa elemen terakhir list L,
# mungkin kosong}
# REALISASI
def Head(L):
    return L[:1]


# DEFINISI DAN SPESIFIKASI PREDIKAT DASAR
# (UNTUK BASIS ANALISIS REKURENS)
# IsEmpty: List --> boolean
# {IsEmpty(L): benar jika kosong}
# REALISASI
def IsEmpty(L):
    return L == []


# IsOneElmt: List --> boolean
# {IsOneElmt(X, L): benar jika list L hanya mempunyai satu elemen}
# REALISASI
def IsOneElmt(L):
    if not IsEmpty(L):
        return NbElmt(L) == 1


# DEFINISI DAN SPESIFIKASI PREDIKAT RELASIONAL
# IsEqual: 2 List --> boolean
# {IsEqual(L1,L2): benar jika semua elemen list L1 sama dengan L2:
# sama urutan dan sama nilainya}
# REALISASI
def IsEqual(L1, L2):
    return (IsEmpty(L1) and IsEmpty(L2)) or (
        FirstElmt(L1) == FirstElmt(L2) and IsEqual(Tail(L1), Tail(L2))
    )


# DEFINISI DAN SPESIFIKASI FUNGSI LAIN
# NbElmt: List --> integer
# {NbElmt(L): menghasilkan banyaknya elemen list, nol jika kosong}
# REALISASI
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))


# ElmtKeN: integer >= 0, List --> element
# {ElmtKeN(N,L): mengirimkan elemen List yang ke N,
# N <= NbElmt(L) dan N >= 0}
# REALISASI CONTOH 6
def ElmtKeN(N, L):
    if N == 1:
        return FirstElmt(L)
    else:
        return ElmtKeN(N - 1, Tail(L))


# Copy: List --> List
# {Copy(L): menghasilkan list yang identik dengan list asal}
# REALISASI
def Copy(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L), Copy(Tail(L)))


# Inverse: List --> List
# {Inverse(L): menghasilkan list L yang terbalik, yaitu yang urutan elemennya adalah kebalikan dari list asal}
# REALISASI
def Inverse(L):
    if IsEmpty(L):
        return []
    else:
        return Kons0(Inverse(Tail(L)), FirstElmt(L))


# Konkat: 2 List --> List
# {Konkat(L1,L2): menghasilkan konkatenasi 2 buah list, dengan list L2 "sesudah" list L1}
# REALISASI CONTOH 7 VERSI 1
def Konkat(L1, L2):
    if IsEmpty(L1):
        return L2
    else:
        return Konso(FirstElmt(L1), Konkat(Tail(L1), L2))


# Konkat2: 2 List --> List
# {Konkat2(L1,L2): menghasilkan konkatenasi 2 buah list, dengan list L2 "sesudah" list L1}
# REALISASI CONTOH 7 VERSI 2
def Konkat2(L1, L2):
    if IsEmpty(L2):
        return L1
    else:
        return Konkat(Kons0(L1, FirstElmt(L2)), Tail(L2))


# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsMember: elemen, List --> boolean
# {IsMember(X,L): true jika X adalah elemen list L}
# REALISASI
def IsMember(X, L):
    if IsEmpty(X):
        return False
    else:
        if FirstElmt(L) == X:
            return True
        else:
            return IsMember(X, Tail(L))


# IsFirst: elemen, List (tidak kosong) --> boolean
# {IsFirst(X,L): true jika X adalah elemen pertama dari list L}
# REALISASI
def IsFirst(X, L):
    if not IsEmpty(L):
        return FirstElmt(L) == X


# IsLast: elemen, List (tidak kosong) --> boolean
# {IsLast(X,L): true jika X adalah elemen pertama list L}
# REALISASI
def IsLast(X, L):
    if not IsEmpty(L):
        return LastElmt(L) == X


# IsNbElmtN: List, integer --> boolean
# IsNbElmtN(L,N): true jika banyaknya elemen list sama dengan N
# REALISASI CONTOH 8 VERSI 1
def IsNbElmtN(L, N):
    if N == 0:
        if IsEmpty(L):
            return True
        else:
            return False
    else:
        return IsNbElmtN(Tail(L), N - 1)


# IsNbElmtN2: List, integer --> boolean
# IsNbElmtN2(L,N): true jika banyaknya elemen list sama dengan N
# REALISASI CONTOH 8 VERSI 2
def IsNbElmtN2(L, N):
    return NbElmt(L) == N


# IsXElmtKeN: elemen, integer >= 0, List (tidak kosong) --> boolean
# {IsXElmtKeN(X,N,L): true jika X adalah elemen ke-N list L, N >= 0, dan N <= banyaknya elemen list false jika tidak }
# REALISASI CONTOH 9
def IsXElmtKeN(X, N, L):
    if IsMember(X, L):
        if N == 1 and FirstElmt(L) == X:
            return True
        else:
            return False or IsXElmtKeN(X, N - 1, Tail(L))
    else:
        return False


# IsXElmtKeN2: elemen, integer >= 0, List (tidak kosong) --> boolean
# {IsXElmtKeN2(X,N,L): true jika X adalah elemen ke-N list L, N >= 0, dan N <= banyaknya elemen list false jika tidak }
# REALISASI CONTOH 9 VERSI 2
def IsXElmtKeN2(X, N, L):
    return ElmtKeN(N, L) == X


# IsInverse: List, List --> boolean
# {IsInverse(L1, L2): true jika L2 adalah list dengan urutan terbalik dibandingkan L1}
# REALISASI VERSI 1 -- DENGAN NAMA DAN FUNGSI PERANTARA
def IsInverse(L1, L2):
    return IsEqual(L1, Inverse(L2))


# IsInverse2: List, List --> boolean
# {IsInverse2(L1, L2): true jika L2 adalah list dengan urutan terbalik dibandingkan L1}
# REALISASI VERSI 2 -- SECARA REKURSIF
def IsInverse2(L1, L2):
    if NbElmt(L1) == NbElmt(L2):
        if IsEmpty(L1) and IsEmpty(L2):
            return True
        else:
            return FirstElmt(L1) == LastElmt(L2) and IsInverse(
                Head(Tail(L1)), Head(Tail(Inverse(L2)))
            )
    else:
        return False


# APLIKASI
A = []
B = [1, 3, "b"]
C = ["Y", 7, "L"]
print(Konso("X", B))  # ['X', 1, 3, 'b']
print(Kons0(C, 87))  # ['Y', 7, "L", 87]
print(FirstElmt(B))  # 1
print(LastElmt(C))  # L
D = Kons0(C, 87)
E = Konso("X", B)
print(Head(D))  # ['Y']
print(Tail(D))  # [7, 'L', 87]
print(IsEmpty(A))  # True
F = Kons0(A, 8)  # True
print(IsOneElmt(F))  # True
print(IsEmpty(A))  # True
G = ["Y", 7, "L"]
print(IsEqual(G, C))  # True
# APLIKASI CONTOH 6
print(NbElmt(G))  # 3
print(ElmtKeN(2, G))  # 7
print(Copy(B))  # [1,3,'b']
C1 = Inverse(C)
print(C1)  # ['L', 7, 'Y']

# APLIKASI CONTOH 7 VERSI 1
print(Konkat(F, G))  # [8, 'Y', 7, 'L']

# APLIKASI CONTOH 7 VERSI 2
T = Konkat2(G, C)
print(T)  # True

# APLIKASI CONTOH 8 VERSI 1
print(IsNbElmtN(A, 0))  # True

print(IsMember("L", C))  # True

# APLIKASI CONTOH 8 VERSI 1
print(IsNbElmtN(T, 6))  # True

# APLIKASI CONTOH 8 VERSI 2
print(IsNbElmtN2(B, 3))  # True

print(IsFirst(1, B))  # True
print(IsLast("b", B))  # True

# APLIKASI CONTOH 9 VERSI 1
print(IsXElmtKeN(1, 1, B))  # True

# APLIKASI CONTOH 9 VERSI 2
H = [7, 6, 2]
print(IsXElmtKeN2(2, 3, H))  # True

# APLIKASI CONTOH 10 VERSI 1
print(IsInverse(C, C1))  # True

# APLIKASI CONTOH 10 VERSI 2
print(IsInverse2(C1, C))  # True

