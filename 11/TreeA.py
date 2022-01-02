# Nama		: Ahmad Alexander
# NIM		: 24010316140048
# Tanggal	: 28 November 2020
# Deskripsi	: Modul Tree A

# Pohon Realisasi Prefix

P0 = []

P1 = [1, [2, [3, [], []], [4, [], []]], [5, [], []]]

P2 = ["a", ["i", ["u", [], []], ["e", [], []]], ["o", [], []]]

# Fungsi Akar
# DefSpek
# Akar (p) pohon biner tak kosong ---> pohon biner
def Akar(P):
    return P[0]


# Fungsi Left
# DefSpek
# Left : pohon biner tak kosong ---> pohon biner
# Left (P) adalah sub pohon kiri dari P jika /L, A, R\ maka left (P) adalah L
def Left(P):
    return P[1]


# Fungsi Right
# DefSpek
# Right : pohon biner tak kosong ---> pohon biner
# Right (P) adalah sub pohon kanan dari P jika /L, A , R\ maka right (P) adalah R
def Right(P):
    return P[2]


# Fungsi IsTreeEmpty
# DefSpek
# IsTreeEmpty : pohon biner ---> boolean
# IsTreeEmpty (P) bernilai benar jika P kosong
def IsTreeEmpty(P):
    if P:
        return False
    else:
        return True


# Fungsi IsOneElmtPB
# DefSpek
# IsOneElmtPB : poho biner --> boolean
# IsOneElmtPB (P) bernilai benar jika P hanya mempunyai satu elemen yaitu /A
def IsOneElmtPB(P):
    if not IsTreeEmpty(P) and IsTreeEmpty(Right(P)) and IsTreeEmpty(Left(P)):
        return True
    else:
        return False


# Fungsi IsUnerLeft
# DefSpek
# IsUnerLeft : pohon biner ---> boolean
# IsUnerLeft (P) bernilai benar jika P mengandung sub pohon kiri
def IsUnerLeft(P):
    if not IsTreeEmpty(P) and IsTreeEmpty(Right(P)) and not IsTreeEmpty(Left(P)):
        return True
    else:
        return False


# Fungsi IsUnerRight
# DefSpek
# IsUnerRight : pohon biner ---> boolean
# IsUnerRight (P) bernilai benar jika P mengandung sub pohon kanan
def IsUnerRight(P):
    if not IsTreeEmpty(P) and not IsTreeEmpty(Right(P)) and IsTreeEmpty(Left(P)):
        return True
    else:
        return False


# Fungsi IsBiner
# DefSpek
# IsBiner : pohon biner ---> boolean
# IsBiner (P) bernilai benar jika P mengandung sub pohon kiri dan sub pohon kanan
def IsBiner(P):
    if not IsTreeEmpty(P) and not IsTreeEmpty(Right(P)) and not IsTreeEmpty(Left(P)):
        return True
    else:
        return False


# Fungsi IsExistLeft
# DefSpek
# IsExistLeft : pohon biner tak kosong ---> boolean
# IsExistLeft (P) bernilai benar jika P mengandung sub pohon kiri
def IsExistRight(P):
    if not IsTreeEmpty(P) and not IsTreeEmpty(Right(P)):
        return True
    else:
        return False


# Fungsi IsExistRight
# DefSpek
# IsExistRight : pohon biner tak kosong ---> boolean
# IsExist (P) bernilai benar jika P mengandung sub pogon kanan
def IsExistLeft(P):
    if not IsTreeEmpty(P) and not IsTreeEmpty(Left(P)):
        return True
    else:
        return False
