# Nama file: segitiga.py
# Pembuat: Ahmad Alexander
# Tanggal: 29 September 2020
# Deskripsi: Menentukan jika segitiga merupakan sama sisi, sama kaki, atau sembarang

# Definisi dan spesifikasi dari fungsi segitiga adalah:
# Segitiga: 3 integer > 0 --> character
# segitiga(a,b,c) adalah fungsi yang menerima tiga buah integer lebih besar dari 0 yang merepresentasikan setiap sisi segitiga
# dan menghasilkan jika segitiga merupakan sama sisi, sama kaki, ATAU sembarang

# Realisasi
def Segitiga(a, b, c):
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
A = Segitiga(0, -1, 20)
print(A)  # return x
B = Segitiga(10, 10, 10)
print(B)  # return s
C = Segitiga(100, 40, 40)
print(C)  # return k
D = Segitiga(20, 95, 20)
print(D)  # return k
E = Segitiga(1, 1, 80000)
print(E)  # return k
F = Segitiga(42, 69, 14)
print(F)  # return y
