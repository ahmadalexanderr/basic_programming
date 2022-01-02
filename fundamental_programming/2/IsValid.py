# Nama file: IsValid.py
# Pembuat: Ahmad Alexander
# Tanggal: 22 September 2020
# Deskripsi: Menerima sebuah integer dan menentukan apakah integer tersebut valid

# Definisi dan Spesifikasi dari fungsi IsValid? adalah:
# IsValid? : integer --> integer
# {IsValid? (x) benar jika (x) bernilai lebih kecil 5 atau lebih besar sama dengan 500}

# Realisasi
def IsValid(x):
    return x < 5 or x >= 500


# Aplikasi
A = 5
B = 0
C = 500
D = 6000
print(IsValid(5)) #False
print(IsValid(0)) #True
print(IsValid(500)) #True
print(IsValid(6000)) # True