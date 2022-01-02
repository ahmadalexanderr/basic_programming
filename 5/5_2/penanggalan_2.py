# Nama file: penanggalan_2.py
# Pembuat: Ahmad Alexander
# Tanggal: 9 September 2020
# Deskripsi: Penanggalan versi 2 (memperhitungkan tahun kabisat)

# Definisi dan spesifikasi dari fungsi penanggalan versi 2 adalah:
# Harike1900: integer[1..31], integer[1..12] integer[0..99] --> integer[1..366]
# {Harike1900(d,m,y) dari suatu tanggal <d,m,y> adalah hari 'absolut' dihitung mulai 1 Januari 1900+y. 1 Januari tahun 1900+y adalah hari ke 1}
# dpm: integer[1..12]-->integer[1..36]
# {dpm(B) adalah jumlah hari pada tahun ybs pada tanggal 1 bulan B. terhitung mulai satu januari: kumulatif jumlah hari tanggal 1 Januari s/d tanggal 1 bulan B, dengans memperhitungkan tahun kabisat}
# IsKabisat?: integer[0..99]-->boolean
# {IsKabisat?(a) true jika tahun 1990+a adalah tahun kabisat: habis dibagi 4 tetapi tidak habis dibagi 100, atau habis dibagi 400}

# Realisasi {dengan memperhitungkan tahun kabisat}
# {Realisasi dpm(B) sama dengan pada versi ke 1}
def IsKabisat(a):
    return ((a % 4 == 0) and (a % 100 != 0)) or (a / 400 == 0)


def Harike1900(d, m, y):
    if (m < 0) or (m > 12):
        x = "Bulan tidak valid"
        return x
    else:
        if (m > 2) and IsKabisat(y):
            return dpm(m) + d - 1 + 1
        else:
            return dpm(m) + d - 1 + 0


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
A = Harike1900(5, 10, 2020)
B = Harike1900(9, 9, 2020)
C = Harike1900(26, 12, 1966)
D = Harike1900(20, 111, 780)
print(A)
print(B)
print(C)
print(D)
