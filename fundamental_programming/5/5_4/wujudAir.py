# Nama file: wujudAir.py
# Pembuat: Ahmad Alexander
# Tanggal: 10 September 2020
# Deskripsi: Mengonversi suatu besaran dalam derajat Celcius ke derajat Kelvin

# Definisi dan spesifikasi dari fungsi wujudAir adalah:
# wujudAir : real-->character
# wujudAir(x) adalah fungsi yang menerima sebuah masukan bilangan real yang menyatakan temperatur air dalam satuan derajad Celcius pada tekanan 1 atm dan menghasilkan wujudnya, apakah berwujud es (padat), cair, atau uap

# Realisasi
def wujudAir(x):
    if x < 0:
        s = "air berwujud es (padat)"
        return s
    elif x > 100:
        u = "air berwujud uap"
        return u
    else:
        c = "air berwujud cair"
        return c


# Aplikasi
C = wujudAir(281.23)
A = wujudAir(-1000)
B = wujudAir(7.3)
print(A)
print(B)
print(C)
