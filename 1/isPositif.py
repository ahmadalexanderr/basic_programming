#Nama file: isPositif.py
#Pembuat : Ahmad Alexander
#Tanggal: 31 Agustus 2020
#Deskripsi: Sebuah predikat yang menerima sebuah bilangan bulat dan bernilai benar jika bilangan tersebut positif.

# DEFINISI DAN SPESIFIKASI
# isPositif? : integer --> boolean
# isPositif? (x) benar jika x positif

# Realisasi
def isPositif(x):
    return x >= 0


# Aplikasi
print(isPositif(1))
print(isPositif(0))
print(isPositif(-1))