# Nama file: IsAnA.py
# Pembuat: Ahmad Alexander
# Tanggal: 22 September 2020
# Deskripsi: Menerima sebuah karakter dan bernilai benar jika karakter tersebut adalah huruf 'A'

# Definisi dan Spesifikasi dari fungsi IsAnA adalah:
# IsAnA: character --> boolean
# {IsAnA(C) benar jika c adalah karakter (huruf) 'A'}

# Realisasi
def IsAnA(c):
    return c == "A"

# Aplikasi
x = 'A'
y = 'a'
z = 'g'
print(IsAnA(x)) #True
print(IsAnA(y)) #False
print(IsAnA(z)) #False