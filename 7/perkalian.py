# Nama file: perkalian.py
# Deskripsi: perkalian dua bilangan bulat
# Pembuat: Ahmad Alexander
# Tanggal: 26 Oktober 2020

# DEFINISI DAN SPESIFIKASI
# mul: 2 integer --> integer
# {mul(x,y): mengalikan x dan y secara rekursif
# mul(x,y): x * y = 0 {basis}
#         : x + x + y(-1) {rekurens}
# }
# REALISASI
def mul(x, y):
    if y == 0:  # basis
        return 0
    else:  # rekurens
        return x + mul(x, y - 1)

# APLIKASI
A = mul(8, 2)
B = mul(3, 3)
C = mul(9, 0)
D = mul(-1, 2)
print(A)  # 16
print(B)  # 9
print(C)  # 0
print(D)  # -2

