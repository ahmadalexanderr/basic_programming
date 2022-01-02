#Nama file: tanggal.py
#Deskripsi: membuat tipe bentukan tanggal beserta selektor dan konstruktornya
#Pembuat: Ahmad Alexander
#Tanggal: 6 Oktober 2020

#Definisi dan spesifikasi type
#type Hr: integer[1...31]
#{definisi ini hanyalah untuk "menamakan" type integer dengan nilai tertentu supaya mewakili harim sehingga jika mempunyai
# suatu nilai integer, kita dapat memeriksa apakah nilai integer tersebut mewakili Hari yang absah}
#Realisasi type Hr
class Hr:
    def __init__(self,a):
        a >= 1 and a <= 31
        self.d = a

    def __str__(self):
        return '{0}' .format(self.d)

#type Bln: integer[1...12]
#{definisi ini hanyalah untuk "menamakan" type integer dengan daerah nilai tertentu supaya mewakili Bulan}
#Realisasi type Bln
class Bln:
    def __init__(self,b):
        b >= 1 and b <= 12
        self.m = b

    def __str__(self):
        return '{0}' .format(self.m)

#type Thn: integer > 0
#{definisi ini hanyalah untuk "menamakan" type integer dengan daerah nilai tertentu supaya mewakili Tahun}
#Realisasi type Thn
class Thn:
    def __init__(self,c):
        c > 0
        self.y = c

    def __str__(self):
        return '{0}' .format(self.y)

#type Date: <d: Hr, m: Bln, y: Thn>
#{<d,m,y> adalah tanggal d bulan m tahun y}
#Realisasi type Date
class Date:
    def __init__(self, Hr, Bln, Thn):
        self.d = Hr
        self.m = Bln
        self.y = Thn

    def __str__(self):
        return '({0},{1},{2})' .format(self.d, self.m, self.y)

#Definisi dan spesifikasi selektor
#Day: Date --> Hr
#{Day(D) memberikan hari d dari D yang terdiri dari <d,m,y>}
#Realisasi selektor Day(D)
def Day(D):
    return D.d

#Month: Date --> Bln
#{Month(D) memberikan bulan m dari D yang terdiri dari <d,m,y>}
#Realisasi selektor Month(D)
def Month(D):
    return D.m

#Year: Date --> Thn
#{Year(D) memberikan tahun y dari D yang terdiri dari <d,m,y>}
#Realisasi selektor Year(D)
def Year(D):
    return D.y

#Definisi dan spesifikasi konstruktor
#MakeDate:<h,b,t> --> Date
#{MakeDate<h,b,t>-->tanggal pada hari,bulan,tahun yang bersangkutan}
#Realisasi konstruktor MakeDate(h,b,t)
def MakeDate(h,b,t):
    return Date(h,b,t)

#Definisi dan spesifikasi operator/fungsi lain terhadap Date
#NextDay: Date --> Date
#{NextDay(D): menghitung Date yang merupakan keesokan hari dari Date D yang diberikan:
# NextDay(<1,1,80>) adalah (<2,1,80>)
# NextDay(<31,1,80>) adalah (<1,2,80>)
# NextDay(<30,4,80>) adalah (<1,5,80>)
# NextDay(<31,12,80>) adalah (<1,1,81>)
# NextDay(<28,2,80>) adalah (<29,2,80>)
# NextDay(<28,2,81>) adalah (<1,3,82>)
# }
#Realisasi operator NextDay(D)
def NextDay(D):
    if Month(D) == 1 or Month(D) == 3 or Month(D) == 5 or Month(D) == 7 or Month(D) == 8 or Month(D) == 10:
        if Day(D) < 31:
            return MakeDate(Day(D)+1,Month(D),Year(D))
        else:
            return MakeDate(1,Month(D)+1,Year(D))
    elif Month(D) == 4 or Month(D) == 6 or Month(D) == 9 or Month(D) == 11:
        if Day(D) < 30:
            return MakeDate(Day(D)+1,Month(D),Year(D))
        else:
            return MakeDate(Day(D),Month(D)+1,Year(D))
    elif Month(D) == 2:
        if Day(D) < 28:
            return MakeDate(Day(D)+1,Month(D),Year(D))
        elif IsKabisat(Year(D)):
            if Day(D) == 28:
                return MakeDate(Day(D)+1,Month(D),Year(D))
            else:
                return MakeDate(1, Month(D)+1, Year(D))
        else:
            return MakeDate(1,Month(D)+1,Year(D))
    else:
        if Day(D) < 31:
            return MakeDate(Day(D)+1,Month(D),Year(D))
        else:
            return MakeDate(1,1,Year(D)+1)

#Yesterday: Date --> Date
#{Yesterday(D): menghitung Date yang merupakan 1 hari sebelum Date DD yang diberikan:
# Yesterday(<1,1,80>) adalah <31,12,79>
# Yesterday(<31,1,80>) adalah <30,1,80>
# Yesterday(<1,5,80>) adalah <30,4,80>
# Yesterday(<29,2,80>) adalah <28,2,80>
# Yesterday(<1,3,80>) adalah <29,2,80>
# }
# Realisasi operator Yesterday(D)
def Yesterday(D):
    if Month(D) == 1:
        if Day(D) > 1:
            return MakeDate(Day(D)-1, Month(D), Year(D))
        else:
            return MakeDate(31,12,Year(D)-1)
    elif Month(D) == 3:
        if Day(D) > 1:
            return MakeDate(Day(D)-1, Month(D), Year(D))
        else:
            if IsKabisat(Year(D)):
                return MakeDate(29, Month(D)-1, Year(D))
            else:
                return MakeDate(28, Month(D)-1, Year(D))
    elif Month(D) == 2 or Month(D) == 4 or Month(D) == 6 or Month(D) == 9 or Month(D) == 11:
        if Day(D) > 1:
            return MakeDate(Day(D)-1, Month(D), Year(D))
        else:
            return MakeDate(31, Month(D)-1, Year(D))
    else:
        if Day(D) > 1:
            return MakeDate(Day(D)-1, Month(D), Year(D))
        else:
            return MakeDate(30, Month(D)-1, Year(D))

#NextNDay: Date, integer --> integer
#{NextNDay(D,N): menghitung Date yang merupakan N hari (N adalah nilai integer) sesudah dari date D yang diberikan}
#Realisasi operator NextNDay(D,N)
def NextNDay(D,N):
    if N == 1:
        return NextDay(D)
    else:
        return NextNDay(NextDay(D), N-1)
#HariKe1900: Date --> integer[0...366]
#{HariKe1900(D): menghitung jumlah hari terhadap 1 Januari pada tahun y, dengan memperhitungkan apakah y adalah
# tahun kabisat}
#Realisasi operator HariKe1900(D)
def HariKe1900(D):
    return dpm(Month(D)) + Day(D) - 1 + (1 if Month(D) > 2 and IsKabisat(Year(D)) else 0)

#Definisi dan spesifikasi fungsi perantara
# dpm : integer[1..12] --> integer[1..36]
# {dpm(B) adalah jumlah hari pada tahun yang bersangkutan pada tanggal 1 bulan B terhitung mulai 1 januari:
# kumulatif jumlah hari dari tanggal 1 Januari s/d tanggal 1 bulan B, tanpa memperhitungkan tahun kabisat }
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

#Definisi dan spesifikasi predikat
#IsEqD?: 2 Date --> boolean
#{IsEqD?(D1,D2) benar jika D1=D2, mengirimkan true jika d1 = d2 dan m1 = m2 dan y1 = y2.
# Contoh:   IsEqD?(<1,1,90>,<1,1,90>) adalah true
#           IsEqD?(<1,2,90>,<1,1,90>) adalah false
# }
#Realisasi predikat IsEqD?(D1,D2)
def IsEqD(D1,D2):
    return Day(D1) == Day(D2) and Month(D1) == Month(D2) and Year(D1) == Year(D2)

#IsBefore? 2 Date --> boolean
#{IsBefore?(D1,D2) mengirimkan true jika D1 adalah sebelum D2:
# Contoh:   IsBefore?(<1,1,80>,<1,2,80>) adalah true
#           IsBefore?(<1,1,80>,<2,1,80>) adalah true
#
# }
#Realisasi predikat IsBefore?(D1,D2)
def IsBefore(D1,D2):
    if Day(D1) < Day(D2):
        return True
    elif Day(D1) >= Day(D1):
        if Month(D1) < Month(D2):
            return True
        elif Month(D1) >= Month(D2):
            if Year(D1) < Year(D2):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

#IsAfter? 2 Date --> boolean
#{IsAfter?(D1,D2) mengirimkan true jika D1 adalah sesudah D2:
# Contoh:   IsAfter(<1,11,80>,<1,2,80>) adalah true
#           IsAfter(<1,1,80>,<2,1,80>) adalah false
#           IsAfter(<1,1,80>,<1,1,80>) adalah false
#}
#Realisasi predikat IsAfter?(D1,D2)
def IsAfter(D1,D2):
    if Day(D1) > Day(D2):
        return True
    elif Day(D1) <= Day(D1):
        if Month(D1) > Month(D2):
            return True
        elif Month(D1) <= Month(D2):
            if Year(D1) > Year(D2):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

#IsKabisat?: integer --> boolean
#{IsKabisat(a) true jika tahun 1900 + a adalah tahun kabisat: habis dibagi 4 tetapi tidak habis dibagi 100 atau habis
# 400}
#Realisasi predikat IsKabisat?(a)
def IsKabisat(a):
    return ((a % 4 == 0) and (a % 100 != 0)) or (a / 400 == 0)

#Aplikasi NextDay
print("Aplikasi NextDay")
A = MakeDate(1,1,80)
B = MakeDate(31,1,80)
C = MakeDate(30,4,80)
D = MakeDate(31,12,80)
E = MakeDate(28,2,80)
F = MakeDate(28,2,81)
print("NextDay",A,"adalah",NextDay(A))
print("NextDay",B,"adalah",NextDay(B))
print("NextDay",C,"adalah",NextDay(C))
print("NextDay",D,"adalah",NextDay(D))
print("NextDay",E,"adalah",NextDay(E))
print("NextDay",F,"adalah",NextDay(F))

#Aplikasi Yesterday
print("\nAplikasi Yesterday")
A1 = MakeDate(1,1,80)
B1 = MakeDate(31,1,80)
C1 = MakeDate(1,5,80)
D1 = MakeDate(31,12,80)
E1 = MakeDate(29,2,80)
F1 = MakeDate(1,3,80)
print("Yesterday",A1,"adalah",Yesterday(A1))
print("Yesterday",B1,"adalah",Yesterday(B1))
print("Yesterday",C1,"adalah",Yesterday(C1))
print("Yesterday",D1,"adalah",Yesterday(D1))
print("Yesterday",E1,"adalah",Yesterday(E1))
print("Yesterday",F1,"adalah",Yesterday(F1))

#Aplikasi NextNDay
print("\nAplikasi NextNDay")
print("Next 4 Day",D,"adalah",NextNDay(D,4))
print("Next 30 Days",E1,"adalah",NextNDay(E1,30))
print("Next 39 Days",C1,"adalah",NextNDay(C1,39))
print("Next 23 Days",F,"adalah",NextNDay(F,23))
print("Next 69 Days",C,"adalah",NextNDay(C,69))

#Aplikasi Predikat
print("\nAplikasi Predikat")
X = MakeDate(1,1,90)
Y = MakeDate(1,1,90)
Z = MakeDate(1,2,90)
print("IsEqD?",X,Y,"adalah",IsEqD(X,Y))
print("IsEqD?",X,Y,"adalah",IsEqD(Z,Y))
X1 = MakeDate(1,1,80)
Y1 = MakeDate(1,2,80)
Z1 = MakeDate(2,1,80)
print("IsBefore?",X1,Y1,"adalah",IsBefore(X1,Y1))
print("IsBefore?",X1,Z1,"adalah",IsBefore(X1,Z1))
X2 = MakeDate(1,11,80)
Y2 = MakeDate(1,2,80)
Z2 = MakeDate(1,1,80)
print("IsAfter?",X2,Y2,"adalah",IsAfter(X2,Y2))
print("IsAfter?",Z2,Z1,"adalah",IsAfter(Z2,Z1))
print("IsAfter?",Z2,X1,"adalah",IsAfter(Z2,X1))