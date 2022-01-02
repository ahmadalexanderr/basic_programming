# Nama file: pembagian.py
# Deskripsi: pembagian dua bilangan bulat
# Pembuat: Ahmad Alexander
# Tanggal: 26 Oktober 2020

# DEFINISI DAN SPESIFIKASI
# power: integer, integer > 0 --> integer
# { power(x,y): x dipangkatkan dengan y secara rekursif
# power(x,y): x^y = 1, jika y = 0 {basis}
#             x^y = x * x * y(-1) {rekurens}
# }
# REALISASI
def power(x,y):
    if y == 0: #basis
        return 1
    else: #rekurens
        return x * power(x, y-1)

#APLIKASI
A = power(1,0)
B = power(5,5)
C = power(2,3)
D = power(4,10)
E = power(-8,3)
print(A) #1
print(B) #3125
print(C) #8
print(D) #1048576
print(E) #-512