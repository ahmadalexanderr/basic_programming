# Nama file: wujudAir.py
# Pembuat: Ahmad Alexander
# Tanggal: 29 September 2020
# Deskripsi: Menyatakan wujud temperatur air dalam derajat celcius pada tekanan 1 ATM

# Definisi dan spesifikasi dari fungsi WujudAir adalah:
# WujudAir : real-->character
# WujudAir(x) adalah fungsi yang menerima sebuah masukan bilangan real yang menyatakan temperatur air dalam satuan derajad Celcius pada tekanan 1 atm
# dan menghasilkan wujudnya, apakah berwujud es (padat), cair, ATAU uap

# Realisasi
def WujudAir(x):
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
A = WujudAir(281.23)
print(A)  # uap
B = WujudAir(-1000)
print(B)  # es (padat)
C = WujudAir(7.3)
print(C)  # cair
