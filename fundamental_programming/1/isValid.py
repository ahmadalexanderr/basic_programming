# Nama file: isValid.py
# Pembuat : Ahmad Alexander
# Tanggal : 31 Agustus 2020

# DEFINISI DAN SPESIFIKASI
# IsValid? : integer --> integer
# IsValid? (x) benar jika (x) bernilai lebih kecil 5 atau lebih besar dari 500

# Realisasi
def isValid(x):
    return x < 5 or x > 500


# Aplikasi
print(isValid(5))
print(isValid(0))
print(isValid(500))
print(isValid(6000))