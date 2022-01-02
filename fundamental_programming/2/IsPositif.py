# Nama file: IsPositif.py
# Pembuat: Ahmad Alexander
# Tanggal: 22 September 2020
# Deskripsi: Sebuah predikat yang menerima sebuah bilangan bulat dan bernilai benar jika bilangan tersebut positif.

# Definisi dan Spesifikasi dari fungsi IsPositif? adalah:
# IsPositif? : integer --> boolean
# {IsPositif? (x) benar jika x positif}

# Realisasi
def IsPositif(x):
    return x >= 0


# Aplikasi
A = 1
B = 0
C = -1
print(IsPositif(A)) #True
print(IsPositif(B)) #True
print(IsPositif(C)) #False