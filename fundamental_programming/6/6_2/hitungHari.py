# Nama file: hitungHari.py
# Pembuat: Ahmad Alexander
# Tanggal: 16 September 2020
# Deskripsi: menghasilkan hari absolut tanpa memperhitungkan tahun kabisat

# Definisi dan spesifikasi dari fungsi HariKe1900 adalah:
# {HariKe1900(d,m,y) dari suatu tanggal <d,m,y> adalah hari 'absolut' dihitung mulai 1 Januari 1900+y: 1 Januari tahun 1900+y adalah hari ke 1}

# Definisi dan spesifikasi dari fungsi dpm adalah:
# dpm : integer[1..12] --> integer[1..36]
# {dpm(B) adalah jumlah hari pada tahun yang bersangkutan pada tanggal 1 bulan B terhitung mulai 1 januari: kumulatif jumlah hari dari tanggal 1 Januari s/d tanggal 1 bulan B, tanpa memperhitungkan tahun kabisat }

# Realisasi
def HariKe1900(d, m, y):
    return dpm(m) + d - 1


def dpm(B):
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
        return 152
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
    else:
        return 335


# Aplikasi
# Menghitung 20 Maret 1999 = 79
a = HariKe1900(20, 3, 1999)
print(a)

# Menghitung 16 September 2021 = 259
b = HariKe1900(16, 9, 2021)
print(b)

# Menghitung 8 Desember 1914 = 342
c = HariKe1900(8, 12, 1914)
print(c)
