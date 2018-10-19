from math import sqrt, floor
from decimal import Decimal
from fractions import Fraction


class CFraction(list):
    """
    A continued fraction, represented as a list of integer terms.
    """

    def __init__(self, value, maxterms=15, cutoff=1e-10):
        remainder = floor(sqrt(value))
        d = value
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
        print(self)

    def __str__(self):
        return "[%s]" % ", ".join([str(x) for x in self])


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
    s += "{| l |"
    for i in range(2*p+1):
        s += "| r "
    s += "|}\n\hline\n"

    s += "$a_s$ & $*$ "
    for i in range(1, 2*p+1):
        s += "& $a_{}$".format(i)
    s += "\\\\\n\hline\n"
    
    s += "$P_s$ "
    for i in range(2*p+1):
        s += "& {}".format(P[i])
    s += "\\\\\n\hline\n"

    s += "$Q_s$ "
    for i in range(2*p+1):
        s += "& {}".format(Q[i])
    s += "\\\\\n\hline\n"

    s += "Diff "
    for i in range(2*p+1):
        s += "& {}".format(diff[i])
    s += "\\\\\n\hline\n"

    s += "\end{tabular}\n"
    return s


d = 60

print(table(d))
