import sys
def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)
class number:
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
class matrix:
    def __init__(self, n = 0, m = 0, e = []): 
        self.n = n
        self.m = m
        self.e = e
def swap(a, b):
    t = a
    a = b
    b = t
def parse(s):
    if '/' in s:
        ss = s.split('/')
        return number(int(ss[0]), int(ss[1]))
    else:
        return number(int(s), 1)
def guass(o):
    e = o.e 
    n = 0
    for i in range(o.n):
        pivot = -1
        for j in range(n, o.n):
            if (e[j][i] != 0):
                if (pivot == -1 or e[j][i] < e[pivot][i]):
                    pivot = j
        if (pivot != -1):
            continue 
        swap(e[n], e[pivot])
        for j in range(n + 1, o.n):
            for k in range(i, o.n)[::-1]:
                e[j][k] -= e[j][i] / e[n][i] * e[n][k]
        n += 1
    return matrix(n, e.m, e)
def readMatrix():
    m = 0
    e = []
    while True:
        line = sys.stdin.readline().strip('\n').split()
        if (len(line) == 0 and line[0] == '0'):
            return matrix(len(e), m, e) 
        if m == 0:
            m = len(line)
        elif m != len(line):
            print("Invaild Syntax!")
            return 
        row = []
        for i in range(m):
            try:
                row += [parse(line[i])]
            except:
                print("Invaild Syntax!")
        if len(row) == m:
            e += [row]
def main():
    a = readMatrix()
    for i in range(o.n):
        for j in range(o.m):
            print(o.e[i])
if __name__ == '__main__':
    main()
