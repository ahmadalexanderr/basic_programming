# Nama file: pengurangan.py
# Deskripsi: pengurangan dua bilangan bulat
# Pembuat: Ahmad Alexander
# Tanggal: 26 Oktober 2020

# DEFINISI DAN SPESIFIKASI
# sub: 2 integer --> integer
# {sub(x,y): mengurangi x oleh y secara rekursif
# sub(x,y): x - y = x, {basis}
#         : x - y(-1) - 1, {rekurens, jika y>0}
#         : x + y(-1) + 1, {rekurens}
# }
# REALISASI
def sub(x, y):
    if y == 0: #basis
        return x
    else:  # rekurens
        if y > 0:
            return sub(x, y - 1) - 1
        else:
            return sub(x, y + 1) + 1

# APLIKASI
A = sub(9, 3)
print(A)  # 6
B = sub(6, 18)
print(B)  # -12
C = sub(15, 0)
print(C)  # 15
D = sub(0, 11)
print(D)  # -11
