import math

#Nama file: ls.py
#Pembuat : Ahmad Alexander
#Tanggal 31 Agustus 2020

#DEFINISI DAN SPESIFIKASI
#LS : 4 real -> real
#LS(x1,x2,y1,y2) adalah jarak antara dua buah titik (x1,x2) dengan (y1,y2)

#DEFINISI DAN SPESIFIKASI FUNGSI ANTARA
#dif2 : 2 real --> real
#dif(x,2) adalah kuadrat dari selisih antara x dan y
#FX2 : real --> real
#FX2(x) adalah hasil kuadrat dari x

#REALISASI
def fx2(x):
    return (x * x)
``
def dif2(x, y):
    return fx2(x - y)

def ls(x1, y1, x2, y2):
    return math.sqrt(dif2(y2, y1) + dif2(x2, x1))

# Aplikasi
print(ls(1, 3, 5, 6))

