from math import sqrt

l = [2, 3, 5]


def isPrime(n):
    if n in l:
        return True
    if n > l[-1]:
        primes(sqrt(n))
    for p in l:
        if n % p == 0:
            return False
    return True


def primes(n):
    i = l[-1] - (l[-1] % 6) + 6
    print(i)
    while l[-1] < n:
        if isPrime(i-1):
            l.append(i-1)
        if isPrime(i+1):
            l.append(i+1)
        i += 6


n = 2
s = "n={n},\\quad{n}<{p}<{n2}\\\\\n"
out = ""
while n < 1381:
    n2 = 2*n
    p = n2-1
    while not isPrime(p):
        p -= 1
    print(p)
    out += s.format(n=n, p=p, n2=n2)
    n = p

print(out)