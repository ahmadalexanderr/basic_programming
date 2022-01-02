# Nama file: sumDeretGeometri.py
# Deskripsi: menghitung deret geometri
# Pembuat: Ahmad Alexander
# Tanggal: 27 Oktober 2020

#DEFINISI DAN SPESIFIKASI
#sumGeo: integer > 0 --> integer
#{sumGeo(x): menghitung deret geometri dengan y adalah common ratio
# sumGeo(x) =
#           kasus basis: jika x = 0 maka hasilnya 0
#                        jika x = 1 maka hasilnya 1
#           kasus rekurens: 3 * x^y(-1) + 1
#}
#REALISASI
def sumGeo(x):
    if x == 0: #basis
        return 0
    elif x == 1: #basis
        return 1
    else:
        return  3 * sumGeo(x-1) + 1
#APLIKASI
A = sumGeo(1)
print(A) #1
B = sumGeo(2)
print(B) #4
C = sumGeo(3)
print(C) #13
D = sumGeo(4)
print(D) #40