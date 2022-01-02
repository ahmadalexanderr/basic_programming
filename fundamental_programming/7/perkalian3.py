# Nama file: perkalian3.py
# Deskripsi: perkalian 3 dengan bilangan bulat
# Pembuat: Ahmad Alexander
# Tanggal: 26 Oktober 2020

# DEFINISI DAN SPESIFIKASI
# mul3: integer = 3, integer --> integer
# mul3(x,y): mengalikan 3 dengan x secara rekursif
# { mul3(x,y): 3 * x = 0 {basis, x = 0}
#         : 3 * x = 3 {basis, x = 1}
#         : 3 + 3 + x(-1) {rekurens}
# }
#REALISASI
def mul3(x):
    if x == 0: #basis
        return 0
    else: #rekurens
        if x < 0:
            return 3 - mul3(-x+1)
        else:
            return 3 + mul3(x-1)

#APLIKASI
A = mul3(0)
B = mul3(1)
C = mul3(4)
D = mul3(9)
E = mul3(12)
F = mul3(-15)
print(A) #0
print(B) #3
print(C) #12
print(D) #27
print(E) #36
print(F) #-45