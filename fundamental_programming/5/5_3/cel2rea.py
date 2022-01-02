# Nama file: cel2rea.py
# Pembuat: Ahmad Alexander
# Tanggal: 10 September 2020
# Deskripsi: Mengonversi suatu besaran dalam derajat Celcius ke derajat Reamur

# Definisi dan spesifikasi dari fungsi cel2rea adalah:
# cel2rea: real --> real
# cel2rea(x) adalah fungsi yang menerima sebuah masukan bilangan real yang menyatakan suhu dalam satuan derajad Celcius dan mengubahnya ke dalam satuan derajad Reamur

# Realisasi
def cel2rea(x):
    return x * 0.8


# Aplikasi
A = cel2rea(19)
print("{:.2f}".format(A))
