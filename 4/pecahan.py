#Nama file: pecahan.py
#Deskripsi: membuat tipe bentukan pecahan beserta selektor dan konstruktornya
#Pembuat: Ahmad Alexander
#Tanggal: 6 Oktober 2020

#Definisi dan spesifikasi type
#type Pecahan: <n: integer >= 0, d: integer > 0>
#{<n: integer >= 0, d: integer > 0> n adalah pembilang (numerator) dan d adalah penyebut (denumerator. Penyebut sebuah
# Pecahan tidak boleh nol)}
#Realisasi type Pecahan
class Pecahan:
    def __init__(self, a, b):
        a >= 0
        b > 0
        self.n = a
        self.d = b

    def __repr__(self):
        return "<__main__.Pecahan: " + str(self.n) +"/"+ str(self.d) + ">"

#Definisi dan spesifikasi selektor dengan fungsi
#Pemb: Pecahan --> integer >= 0
#{Pemb(P) memberikan numerator pembilang n dari Pecahan tersebut}
#Realisasi selektor Pemb(P)
def Pemb(P):
    return P.n

#Peny: Pecahan --> integer > 0
#{Peny(P) memberikan denumerator penyebut d dari Pecahan tersebut}
#Realisasi selektor Peny(P)
def Peny(P):
    return P.d

#Definisi dan spesifikasi konstruktor
#MakeP: integer >= 0, integer > 0 --> Pecahan
#{MakeP(x,y) membentuk sebuah pecahan dari pembilang x dan penyebut y, dengan x dan y integer}
#Realisasi konstruktor MakeP(x,y)
def MakeP(x,y):
    if (x >= 0 and y > 0):
        return Pecahan(x,y)
    elif (x < 0 and y < 0):
        return Pecahan(abs(x),abs(y))
    elif y < 0 or y == 0:
        print("Denumerator tidak valid")
    elif x < 0:
        print("Numerator tidak valid")

#Definisi dan spesifikasi operator terhadap Pecahan
#{Operator aritmatika Pecahan}
#AddP: 2 Pecahan --> Pecahan
#{AddP(P1,P2): Menambahkan dua buah pecahan P1 dan P2: n1/d1 + n2/d2 = (n1*d2+n2*d1)/d1*d2}
#Realisasi operator AddP(P1,P2)
def AddP(P1,P2):
    P3 = MakeP(Pemb(P1)*Peny(P2)+Pemb(P2)*Peny(P1), Peny(P1)*Peny(P2))
    return P3

#SubP: 2 Pecahan --> Pecahan
#{SubP(P1,P2): Mengurangkan dua buah pecahan P1 dan P2
#Mengurangkan dua pecahan: n1/d1 - n2/d2 = (n1*d2-n2*d1)/d1*d2}
#Realisasi operator SubP(P1,P2)
def SubP(P1,P2):
    P3 = MakeP(Pemb(P1)*Peny(P2)-Pemb(P2)*Peny(P1), Peny(P1)*Peny(P2))
    return P3

#MulP: 2 Pecahan --> Pecahan
#{MulP(P1,P2): Mengalikan dua buah Pecahan P1 dan P2
#Mengalikan dua pecahan: n1/d1 * n2/d2 = n1*n2/d1*d2}
#Realisasi operator MulP(P1,P2)
def MulP(P1,P2):
    P3 = MakeP(Pemb(P1) * Pemb(P2), Peny(P1)*Peny(P2))
    return P3

#DivP: 2 Pecahan --> Pecahan
#{DivP(P1,P2): Membagi dua buah Pecahan P1 dan P2
#Membagi dua Pecahan: (n1/d1)/(n2/d2) = n1*d2/d1*n2}
#Realisasi operator DivP(P1,P2)
def DivP(P1,P2):
    P3 = MakeP(Pemb(P1) * Peny(P2), Peny(P1) * Pemb(P2))
    return P3

#RealP: Pecahan --> real
#{RealP(P): Menuliskan Pecahan dalam notasi desimal}
#Realisasi operator RealP(P1,P2)
def RealP(P):
    R = Pemb(P)/Peny(P)
    return R

#Definisi dan spesifikasi predikat
#{Operator relasional Pecahan}
#IsEqP?: 2 Pecahan --> boolean
#{IsEqP?(P1,P2) true jika P1 = P2
# Membandingkan apakah dua buah Pecahan sama nilainya n1/d1 = n2/d2 jika dan hanya jika n1*d2 = n2*d1}
#Realisasi predikat IsEqP?(P1,P2)
def IsEqP(P1,P2):
    return Pemb(P1) * Peny(P2) == Pemb(P2) * Peny(P1)

#IsLtP?: 2 Pecahan --> boolean
#{IsLtP?(P1,P2) true jika P1 < P2
#Membandingkan dua buah Pecahan, apakah P1 lebih kecil nilainya dari P2:
#n1/d1 < n2/d2 jika dan hanya jika n1*d2 < n2*d1}
#Realisasi predikat IsLtP?(P1,P2)
def IsLtP(P1,P2):
    return Pemb(P1) * Peny(P2) <  Pemb(P2) * Peny(P1)

#IsGtP?: 2 Pecahan --> boolean
#{IsGtP?(P1,P2) true jika P1 > P2
#Membandingkan nilai dua buah Pecahan, apakah P1 lebih besar nilai dari P2:
#n1/d1 > n2/d2 jika dan hanya jika n1*d2 > n2*d1}
#Realisasi predikat IsGtP?(P1,P2)
def IsGtP(P1,P2):
    return Pemb(P1) * Peny(P2) > Pemb(P2) * Peny(P1)

#Aplikasi
A = MakeP(1,2)
print("Pecahan A = ",A, "dalam desimal menjadi = {0:.2f}".format(RealP(A)))
B = MakeP(5,13)
print("Pecahan B = ",B,"dalam desimal menjadi = {0:.2f}".format(RealP(B)))
C = MakeP(-2,-10)
print("Pecahan C = ",C,"dalam desimal menjadi = {0:.2f}".format(RealP(C)))
D = MakeP(0,3)
print("Pecahan D = ",D,"dalam desimal menjadi = {0:.2f}".format(RealP(D)))
E = MakeP(-1,10)
print("Pecahan E = ",E)
F = MakeP(10,0)
print("Pecahan F = ",F)
G = MakeP(3,-5)
print("Pecahan G = ",G)
T = AddP(A,B)
print("Pecahan T = Pecahan A + Pecahan B = ",T,"dalam desimal menjadi = {0:.2f}".format(RealP(T)))
K = SubP(A,B)
print("Pecahan K = Pecahan A - Pecahan B = ",K,"dalam desimal menjadi = {0:.2f}".format(RealP(K)))
X = MulP(A,B)
print("Pecahan X = Pecahan A * Pecahan B = ", X,"dalam desimal menjadi = {0:.2f}".format(RealP(X)))
V = DivP(A,B)
print("Pecahan V = Pecahan A / Pecahan B = ", V, "dalam desimal menjadi = {0:.2f}".format(RealP(V)))
Z = MakeP(1,5)
print("Pecahan Z = ",Z,"dalam desimal menjadi = {0:.2f}".format(RealP(Z)))
print("Apakah Pecahan C sama dengan Pecahan Z?", IsEqP(C,Z))
print("Apakah Pecahan K lebih kecil dari Pecahan X?", IsLtP(K,X))
print("Apakah Pecahan T lebih besar dari Pecahan V?", IsGtP(V,T))
