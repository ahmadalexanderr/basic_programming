# Nama file: segitiga.py
# Pembuat: Ahmad Alexander
# Tanggal: 10 September 2020
# Deskripsi: Menentukan jika segitiga merupakan sama sisi, sama kaki, atau sembarang

# Definisi dan spesifikasi dari fungsi segitiga adalah:
# segitiga: 3 integer > 0 --> character
# segitiga(a,b,c) adalah fungsi yang menerima tiga buah integer lebih besar dari 0 yang merepresentasikan setiap sisi segitiga dan menghasilkan jika segitiga merupakan sama sisi, sama kaki, atau sembarang

# Realisasi
def segitiga(a, b, c):
    if (a <= 0) or (b <= 0) or (c <= 0):
        x = "sisi segitiga tidak valid, coba lagi"
        return x
    elif (a == b) and (a == c):
        s = "segitiga sama sisi"
        return s
    elif (
        ((c > a) and (c > b) and (a == b))
        or ((a > b) and (a > c) and (b == c))
        or ((b > a) and (b > c) and (a == c))
    ):
        k = "segitiga sama kaki"
        return k
    else:
        y = "segitiga sembarang"
        return y


# Aplikasi
A = segitiga(0, -1, 20)
B = segitiga(10, 10, 10)
C = segitiga(100, 40, 40)
D = segitiga(20, 95, 20)
E = segitiga(1, 1, 80000)
F = segitiga(42, 69, 14)
print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
