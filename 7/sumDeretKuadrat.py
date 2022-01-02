# Nama file: sumDeretKuadrat.py
# Deskripsi: menhitung deret kuadrat
# Pembuat: Ahmad Alexander
# Tanggal: 27 Oktober 2020

#DEFINISI DAN SPESIFIKASI
#sumKua: integer >= 0 --> integer > 0
#sumKua(x): x = 0 maka hasilnya 0 {basis}
#           x = 1 maka hasilnya 1 {basis}
#           x^2 + x(-1)^2 {rekurens}

#REALISASI
def sumKua(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return pow(x,2) + sumKua(x-1)

#APLIKASI
A = sumKua(1)
print(A) #1
B = sumKua(2)
print(B) #5
C = sumKua(3)
print(C) #14
D = sumKua(4)
print(D) #30