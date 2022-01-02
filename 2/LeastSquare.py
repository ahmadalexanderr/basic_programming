import math

# Nama file: LeastSquare.py
# Pembuat: Ahmad Alexander
# Tanggal: 22 September 2020
# Deskripsi: Menghitung jarak 2 titik pada koordinat kartesian

# Definisi dan Spesifikasi dari fungsi LS adalah:
# LS : 4 real -> real
# {LS(x1,x2,y1,y2) adalah jarak antara dua buah titik (x1,x2) dengan (y1,y2)}

# Definisi dan Spesifikasi dari fungsi antara adalah:
# dif2 : 2 real --> real
# {DIF2(x,2) adalah kuadrat dari selisih antara x dan y}

# FX2 : real --> real
# {FX2(x) adalah hasil kuadrat dari x}

#Realisasi
def FX2(x):
    return (x * x)

def dif2(x, y):
    return FX2(x - y)

def LS(x1, y1, x2, y2):
    return math.sqrt(dif2(y2, y1) + dif2(x2, x1))

# Aplikasi
A = 1
B = 3
C = 5
D = 6
print(LS(A, B, C, D)) #5.0

