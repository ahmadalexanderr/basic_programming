# Nama file: selisihTanggal.py
# Pembuat: Ahmad Alexander
# Tanggal: 16 September 2020
# Deskripsi: Menghitung selisih dari antara <d1,m1> dan <d2,m2> bukan tahun kabisat

# Definisi dan spesifikasi dari fungsi selisihTgl adalah:
# selisihTgl : integer[1..31], integer[1..12], integer[1..31], integer[1..12] --> integer
# {selisihTgl(d1,m1,d2,m2) menerima empat masukan dengan ketentuan: d1 dan m1 adalah tanggal dan bulan awal dalam suatu tahun, sedangkan d2 dan m2 adalah tanggal dan bulan tujuan dalam suatu tahun yang sama
# Asumsi: 1) Tanggal dan bulan awal harus lebih dahulu daripada tanggal dan bulan akhir; 2) Tahun tersebut bukan tahun kabisat.}

# Definisi dan spesifikasi dari fungsi HariKe1900 adalah:
# {HariKe1900(d,m,y) dari suatu tanggal <d,m,y> adalah hari 'absolut' dihitung mulai 1 Januari 1900+y: 1 Januari tahun 1900+y adalah hari ke 1}

# Definisi dan spesifikasi dari fungsi dpm adalah:
# dpm : integer[1..12] --> integer[1..36]
# {dpm(B) adalah jumlah hari pada tahun yang bersangkutan pada tanggal 1 bulan B terhitung mulai 1 januari: kumulatif jumlah hari dari tanggal 1 Januari s/d tanggal 1 bulan B, tanpa memperhitungkan tahun kabisat }

# Realisasi
def selisihTgl(d1, m1, d2, m2):
    if m1 < m2:
        return abs(HariKe1900(d1, m1) - HariKe1900(d2, m2)) + 1
    elif m1 == m2 and d1 < d2:
        return abs(HariKe1900(d1, m1) - HariKe1900(d2, m2))
    else:
        return 0


def HariKe1900(d, m):
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
# <1,1,10,3> selisih antara tanggal 1 Januari dengan tanggal 10 Maret, hasilnya adalah 31 + 28 + 10 = 69.
a = selisihTgl(1, 1, 10, 3)
print(a)

# <10,2,1,2> selisih antara tanggal 10 Februari dengan tanggal 1 Februari, hasilnya adalah 0 karena tanggal dan bulan awal setelah tanggal dan bulan tujuan.
b = selisihTgl(10, 2, 1, 2)
print(b)

# <10,3,31,3> selisih antara tanggal 10 Maret dengan tanggal 31 Maret, hasilnya adalah 21.
c = selisihTgl(10, 3, 31, 3)
print(c)
