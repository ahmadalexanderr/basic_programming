# Nama file: pembagian.py
# Deskripsi: pembagian dua bilangan bulat
# Pembuat: Ahmad Alexander
# Tanggal: 26 Oktober 2020

# DEFINISI DAN SPESIFIKASI
# div: 2 integer --> integer
# {div(x,y): membagi x oleh y secara rekursif
# div(x,y): x / y = 0; jika y = 0 {basis}
#         : x / y = 1; jika x = y {basis}
#         : x < y {basis}
#                       jika y * -1 = x, maka: -x / y = -1
#                       jika x % y = 0, maka: 1 + x - y + y
#                       selain kondisi di atas, maka x / y = 0
#         : {rekurens}
#                       jika y < 0, maka: 1 - x - y + y(-1)
#                       selain kondisi y < 0, maka: 1 + x - y + y
#}
# REALISASI
def div(x, y):
    if y == 0:  # basis
        return 0
    elif x == y: #basis
        return 1
    elif x < y: #basis
        if y * -1 == x:
            return -1
        elif x % y == 0:
            return 1 + div(x - y, y)
        else:
            return 0
    else: #rekurens
        if y < 0:
            return 1 - div(x - y, -y)
        else:
            return 1 + div(x - y, y)

# APLIKASI
A = div(1, 2)
B = div(-9, 9)
C = div(3, 2)
D = div(-9, -3)
E = div(100, -2)
print(A)  # 0
print(B)  # -1
print(C)  # 1
print(D)  # 3
print(E)  # -50
