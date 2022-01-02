# Nama file: cel2fah.py
# Pembuat: Ahmad Alexander
# Tanggal: 10 September 2020
# Deskripsi: Mengonversi suatu besaran dalam derajat Celcius ke derajat Fahrenheit

# Definisi dan spesifikasi dari fungsi cel2fah adalah:
# cel2fah : real-->real
# cel2fah (x) adalah fungsi yang menerima sebuah masukan bilangan real yang menyatakan suhu dalam satuan derajad Celcius dan mengubahnya ke dalam satuan derajad Fahrenheit

# Realisasi
def cel2fah(x):
    return x * 1.8 + 32


# Aplikasi
A = cel2fah(98)
print("{:.2f}".format(A))
