# Nama file: kuadrat.py
# Pembuat: Ahmad Alexander
# Tanggal: 29 September 2020
# Deskripsi: menghitung hasil pembagian antara akar-akar persamaan kuadrat

# Definisi dan spesifikasi dari fungsi kuadrat adalah:
# kuadrat: 3 real --> real
# kuadrat(a,b,c) menghitung hasil-hasil pembagian antara akar-akar persamaan kuadrat ax^2+bx+c = 0 menggunakan rumus abc dengan masukan tiga buah koefisien a, b, c
# pembagian dihitung dari akar persamaan kuadrat yang lebih besar dibagi dengan akar persamaan kuadrat yang lebih kecil

# Realisasi
import math as m


def kuadrat(a, b, c):
    return (-b + m.sqrt(b ** 2 - 4 * a * c)) / 2 * a


# Aplikasi
A = kuadrat(1, -4, 2)
print("{:.2f}".format(A))  # 3.41
