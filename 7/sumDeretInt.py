# Nama file: sumDeretInt.py
# Deskripsi: menghitung deret bilangan integer
# Pembuat: Ahmad Alexander
# Tanggal: 27 Oktober 2020

# DEFINISI DAN SPESIFIKASI
# seq: integer >= 0 --> integer > 0
# { seq(x,y): menghitung deret bilangan 1 + 2 + 3 + ... + n
# seq(x,y): x = 0 maka hasilnya 0 {basis}
#         : x = 1 maka hasilnya 1 {basis}
#         : x + x(-1) {rekurens}
# }
#REALISASI
def seq(x):
    if x == 0: #basis
        return 0
    elif x == 1: #basis
        return 1
    else:
        return x + seq(x-1)

#APLIKASI
A = seq(1)
B = seq(2)
C = seq(3)
D = seq(4)
print(A) #1
print(B) #3
print(C) #6
print(D) #10