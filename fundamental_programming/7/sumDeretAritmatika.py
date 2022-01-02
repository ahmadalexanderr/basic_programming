# Nama file: sumDeretAritmatika.py
# Deskripsi: menghitung deret aritmatika
# Pembuat: Ahmad Alexander
# Tanggal: 27 Oktober 2020

# DEFINISI DAN SPESIFIKASI
# ari: 2 integer > 0, integer >= 0 --> integer > 0
# ari(x): menghitung jumlah deret aritmatika
# {ari(x): x = 0, maka hasilnya 0 {basis}
#        : x = 1, maka hasilnya 3 {basis}
#        : 3 * x + x(-1)
# }
#REALISASI
def sumAri(x):
    if x == 0:
        return 0
    elif x == 1:
        return 3
    else:
        return 3 * x + sumAri(x-1)
#APLIKASI
A = sumAri(1)
print(A) #3
B = sumAri(2)
print(B) #9
C = sumAri(3)
print(C) #18
D = sumAri(4)
print(D) #30