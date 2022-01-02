def konso(L, x):
    return [x] + L


def kons(L, x):
    return L + [x]


def FirstElmt(L):
    return L[0]


def Tail(L):
    return L[1:]


def Head(L):
    return L[:-1]


def LastElmt(L):
    return L[-1]


def KonsLo(L, S):
    return [L] + S


def KonsL(S, L):
    return S + [L]


def IsMember(X, L):
    if EmptyList(L):
        return False
    elif FirstElmt(L) == X:
        return True
    else:
        return IsMember(X, Tail(L))


def IsMember(X, L):
    if IsEmpty(L):
        return False
    elif FirstElmt(L) == X:
        return True
    else:
        return IsMember(X, Tail(L))


"""List of List"""
list1 = [1, [2], 3, 4, [5, 6]]
list2 = [1, [2, 3, 4], 3, 4, [4, 5, 6]]
list3 = 1
list4 = [2, 3, 4]

Matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Matrix2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


def IsEmpty(L):
    return L == []


# IsAtom : list -> boolean
# IsAtom(e) benar jika elemen list sebuah atom
def IsAtom(e):
    if type(e) == int:
        return True
    else:
        return False


def SumAtom(L):
    if IsAtom(FirstElmt(L)):
        return 1 + Tail(L)
    else:
        return Tail(L)


def SumList(L):
    if IsList(FirstElmt(L)):
        return 1 + Tail(L)
    else:
        return Tail(L)


# IsList : List -> boolean
# IsList(e) benar jika elemen list adalah sebuah list / LIST DALAM LIST
def IsList(e):
    if type(e) == list:
        return True
    else:
        return False


# NbElmt : list -> integer
# NbElmt(L) banyaknya elemen dalam list
def NbElmt(L):
    if IsEmpty(L):
        return 0
    elif IsList(FirstElmt(L)):  #
        return NbElmt(FirstElmt(L)) + NbElmt(Tail(L))
    else:
        return 1 + NbElmt(Tail(L))


# Jumlah : list -> integer
# Jumlah(L) : jumlah seluruh elemen dalam list
def Jumlah(L):
    if IsEmpty(L):
        return 0
    elif IsList(FirstElmt(L)):  # ngecek apakah elemen dalam list adlh list
        return Jumlah(FirstElmt(L)) + Jumlah(Tail(L))
    else:
        return FirstElmt(L) + Jumlah(Tail(L))


L1 = [1, 2, 3, 4, 4, 4, 5, 5, 6]
print(Jumlah(L1))


def IsEqS(S1, S2):
    if IsEmpty(S1) and IsEmpty(S2):
        return True
    elif not IsEmpty(S1) and IsEmpty(S2):
        return False
    elif IsEmpty(S1) and not IsEmpty(S2):
        return False
    elif not IsEmpty(S1) and not IsEmpty(S2):
        if IsAtom(FirstElmt(S1)) and IsAtom(FirstElmt(S2)):
            return FirstElmt(S1) == FirstElmt(S2) and IsEqS(Tail(S1), Tail(S2))
        elif IsList(FirstElmt(S1)) and IsList(FirstElmt(S2)):
            return IsEqS(FirstElmt(S1), FirstElmt(S2)) and IsEqS(Tail(S1), Tail(S2))
        else:
            return False


def IsEqual(L1, L2):
    if IsEmpty(L1) and IsEmpty(L2):
        return True
    elif not IsEmpty(L1) and IsEmpty(L2):
        return False
    elif IsEmpty(L1) and not IsEmpty(L2):
        return False
    elif not IsEmpty(L1) and not IsEmpty(L2):
        return (FirstElmt(L1) == FirstElmt(L2)) and IsEqual(Tail(L1), Tail(L2))


def IsMemberS(A, S):
    if IsEmpty(S):
        return False
    elif not IsEmpty(S):
        if IsAtom(FirstElmt(S)):
            return (A == FirstElmt(S)) or (IsMemberS(A, Tail(S)))
        elif IsList(FirstElmt(S)):
            return (IsMember(A, FirstElmt(S))) or (IsMemberS(A, Tail(S)))


def IsMemberLS(L, S):
    if IsEmpty(L) and IsEmpty(S):
        return True
    elif not IsEmpty(L) and IsEmpty(S):
        return False
    elif IsEmpty(L) and not IsEmpty(S):
        return False
    elif not IsEmpty(L) and not IsEmpty(S):
        if IsAtom(FirstElmt(S)):
            return IsMemberLS(L, Tail(S))
        else:
            if IsEqual(L, FirstElmt(S)):
                return True
            else:
                return IsMemberLS(L, Tail(S))


def RemberL(A, S):
    if IsEmpty(S):
        return S
    elif IsList(FirstElmt(S)):
        return KonsLo(RemberL(A, FirstElmt(S)), RemberL(A, Tail(S)))
    else:
        if FirstElmt(S) == A:
            return RemberL(A, Tail(S))
        else:
            return KonsLo(FirstElmt(S), RemberL(A, Tail(S)))
