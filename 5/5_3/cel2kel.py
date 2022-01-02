# Nama file: cel2kel.py
# Pembuat: Ahmad Alexander
# Tanggal: 10 September 2020
# Deskripsi: Mengonversi suatu besaran dalam derajat Celcius ke derajat Kelvin

# Definisi dan spesifikasi dari fungsi cel2kel adalah:
# cel2kel : real-->real
# cel2kel (x) adalah fungsi yang menerima sebuah masukan bilangan real yang menyatakan suhu dalam satuan derajad Celcius dan mengubahnya ke dalam satuan derajad Kelvin

# Realisasi
def cel2kel(x):
    return x + 273.15


# Aplikasi
A = cel2kel(73)
print("{:.2f}".format(A))
