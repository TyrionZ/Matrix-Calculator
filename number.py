def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)

def __init__(self, p = 0, q = 1):
    if q < 0:
        q = -q 
        p = -p
    g = gcd(abs(q), abs(p))
    self.p = p / g
    self.q = q / g

def __add__(self, other):
    return number(self.p * other.q + self.q * other.p, self.q * other.q)

def __sub__(self, other):
    return self + number(-other.p, other.q)

def __mul__(self, other):
    return number(self.p * other.p, self.q * other.q)

def __div__(self, other):
    return self * number(other.q, other.p)

def __cmp__(self, other):
    return abs(self.p * other.q) < abs(self.q * other.p)


