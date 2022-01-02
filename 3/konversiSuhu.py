# Nama file: konversiSuhu.py
# Pembuat: Ahmad Alexander
# Tanggal: 29 September 2020
# Deskripsi: Mengonversi suatu besaran dalam derajat Celcius ke derajat Reamur, derajat Fahrenheit, atau derajat Kelvin

# Definisi dan spesifikasi dari fungsi Convert adalah:
# Convert : real, char-->real
# Convert(x, y) adalah fungsi yang menerima sebuah masukan x berupa bilangan real yang menyatakan suhu dalam satuan derajad Celcius dan
# sebuah masukan y berupa string yang menyatakan kode konversi suhu sehingga mengeluarkan hasil konversi dalam derajat Reamur, derajat Fahrenheit, ATAU derajat Kelvin

# Realisasi
def Convert(x, c):
    if c == "r" or c == "R":
        return x * 0.8
    elif c == "f" or c == "F":
        return x * 1.8 + 32
    elif c == "k" or c == "K":
        return x + 273.15
    else:
        return False


# Aplikasi
# Konversi -23 derajad Celcius ke -18.40 derajad Reamur
a = Convert(-23, "R")
print("{:.2f}".format(a))

# Konversi 90 derajad Celcius ke 194.00 derajad Fahrenheit
b = Convert(90, "F")
print("{:.2f}".format(b))

# Konversi -14 derajad Celcius ke 133.15 derajad Kelvin
c = Convert(-140, "K")
print("{:.2f}".format(c))

# Konversi 3 derajad Celcius dengan kode konversi invalid, menghasilkan 0.00
d = Convert(3, "a")
print("{:.2f}".format(d))

# Aplikasi
# Konversi 10 derajad Celcius ke 8.00 derajad Reamur
e = Convert(10, "r")
print("{:.2f}".format(e))

# Konversi -100 derajad Celcius ke -148.00 derajad Fahrenheit
f = Convert(-100, "f")
print("{:.2f}".format(f))

# Konversi 78 derajad Celcius ke 351.15 derajad Kelvin
g = Convert(78, "k")
print("{:.2f}".format(g))
