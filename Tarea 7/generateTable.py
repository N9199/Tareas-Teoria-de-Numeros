from math import sqrt, floor
from decimal import Decimal
from fractions import Fraction


class CFraction(list):

    def __init__(self, value, maxterms=15, cutoff=1e-10):
        d = value
        # Calculo de la fracción continúa de una raíz
        self.period = None
        a = True
        P = [0]
        Q = [1]
        k = 0
        self.append(floor((P[k]+sqrt(d))/Q[k]))
        while len(self) < maxterms and a:
            k += 1
            P.append(self[k-1]*Q[k-1]-P[k-1])
            Q.append((d-P[k]*P[k])/Q[k-1])
            self.append(floor((P[k]+sqrt(d))/Q[k]))

            for i in range(1, len(self)+1):
                if self[-i:] == self[1:-i]:
                    self.period = i
                    a = False
        # Check de la fracción continúa
        print(self)

    def __str__(self):
        return "[%s]" % ", ".join([str(x) for x in self])


# Generador de la tabla
def table(d):
    a = CFraction(d, maxterms=50)
    p = a.period
    st = len(a)-2*p
    a += a[-p:]
    P = [None]*(st+3*p)
    Q = [None]*(st+3*p)
    diff = [None]*(st+3*p)

    P[0], P[1] = 1, a[0]
    Q[0], Q[1] = 0, 1

    for i in range(2):
        diff[i] = P[i]*P[i]-d*Q[i]*Q[i]

    for i in range(2, st+3*p):
        P[i] = a[i-1]*P[i-1]+P[i-2]
        Q[i] = a[i-1]*Q[i-1]+Q[i-2]
        diff[i] = P[i]*P[i]-d*Q[i]*Q[i]

    s = "\\begin{tabular}"
    s += "{| l | r | r | r |}\n\hline\n"

    s += "$a_s$ & $P_s$ & $Q_s$ & Diff\\\\\n\hline\hline\n"

    for i in range(2*p+1):
        if i == 0:
            s += "$*$ & {} & {} & {}".format(P[i], Q[i], diff[i])
        else:
            s += "{} & {} & {} & {}".format(a[i-1], P[i], Q[i], diff[i])

        s += "\\\\\n\hline\n"

    s += "\end{tabular}\n"
    return s


# Función para encontrar los primeros 5 cuadrados del Problema 3
def first_5_squares():
    c = 0
    n = 1
    while c < 5:
        if int(sqrt(n*(n+1)/2))*int(sqrt(n*(n+1)/2)) == n*(n+1)/2:
            print(n)
            c += 1
        n += 1


d = 62

print(table(d))
first_5_squares()
