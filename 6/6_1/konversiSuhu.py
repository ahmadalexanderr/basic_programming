# Nama file: konversiSuhu.py
# Pembuat: Ahmad Alexander
# Tanggal: 16 September 2020
# Deskripsi: Mengonversi temperatur air dalam derajat Celcius ke derajat Reamur, Fahrenheit, atau Kelvin

# Definisi dan spesifikasi dari fungsi konversiSuhu adalah:
# konversiSuhu : real, char-->real
# {konversiSuhu (x, c) adalah fungsi yang menerima sebuah masukan bilangan real yang menyatakan temperatur air dalam satuan derajad Celcius dan masukan kode konversi berupa char untuk mengirimkan perintah konversi ke dalam satuan derajad Reamur, Fahrenheit, atau Kelvin.
# char 'r' atau 'R' sebagai perintah mengonversi ke Reamur; char 'f' atau 'F' sebagai perintah mengonversi ke Fahrenheit; dan char 'k' atau 'K' sebagai perintah mengonversi ke Kelvin}

# Realisasi
def konversiSuhu(x, c):
    if c == "r" or c == "R":
        return x * 0.8
    elif c == "f" or c == "F":
        return x * 1.8 + 32
    elif c == "k" or c == "K":
        return x + 273.15
    else:
        return False


# Aplikasi
# Konversi 23 derajad Celcius ke 18.40 derajad Reamur
a = konversiSuhu(23, "r")
print("{:.2f}".format(a))

# Konversi 90 derajad Celcius ke 194.00 derajad Fahrenheit
b = konversiSuhu(90, "F")
print("{:.2f}".format(b))

# Konversi -14 derajad Celcius ke -11.20 derajad Reamur
c = konversiSuhu(-14, "r")
print("{:.2f}".format(c))

# Konversi 3 derajad Celcius dengan kode konversi invalid
d = konversiSuhu(3, "a")
print("{:.2f}".format(d))
