# Nama file: penanggalan_1.py
# Pembuat: Ahmad Alexander
# Tanggal: 9 September 2020
# Deskripsi: Penanggalan versi 1 (tanpa memperhitungkan tahun kabisat)

# Definisi dan spesifikasi dari fungsi penanggalan versi 1 adalah:
# Harike1900: integer[1..31], integer[1..12] integer[0..99] --> integer[1..366]
# {Harike1900(d,m,y) dari suatu tanggal <d,m,y> adalah hari 'absolut' dihitung mulai 1 Januari 1900+y. 1 Januari tahun 1900+y adalah hari ke 1}
# dpm: integer[1..12]-->integer[1..36]
# {dpm(B) adalah jumlah hari pada tahun ybs pada tanggal 1 bulan B. terhitung mulai satu januari: kumulatif jumlah hari tanggal 1 Januari s/d tanggal 1 bulan B, tanpa memperhitungkan tahun kabisat}

# Realisasi {tanpa kabisat}
def Harike1900(d, m, y):
    if (m < 1) or (m > 12):
        x = "bulan tidak valid"
        return x
    else:
        return dpm(m) + d - 1


def dpm(B):
    # {analisis kasus terhadap B}
    if B == 1:
        return 1
    elif B == 2:
        return 32
    elif B == 3:
        return 60
    elif B == 4:
        return 91
    elif B == 5:
        return 121
    elif B == 6:
        return 121
    elif B == 7:
        return 182
    elif B == 8:
        return 213
    elif B == 9:
        return 244
    elif B == 10:
        return 274
    elif B == 11:
        return 305
    elif B == 12:
        return 335


# Aplikasi
A = Harike1900(3, 11, 2020)
B = Harike1900(9, 9, 2020)
C = Harike1900(8, 12, 2099)
D = Harike1900(2, 20, 1830)
print(A)
print(B)
print(C)
print(D)
