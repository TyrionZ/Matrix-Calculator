import sys
import copy
from termcolor import colored as cl

# other useful functions
def swap(a, b):
    t = a
    a = b
    b = t

def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)

# rational number
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
        if abs(self.p * other.q) < abs(self.q * other.p):
            return -1
        elif abs(self.p * other.q) == abs(self.q * other.p):
            return 0
        else:
            return 1

    def __str__(self):
        if self.q == 1:
            return str(self.p)
        else:
            return str(self.p) + '/' + str(self.q)
   
# matrix
class matrix:
    def __init__(self, n = 0, m = 0, e = []): 
        self.n = n
        self.m = m
        self.e = e
    
    def show(self):
        for i in range(self.n):
            for j in range(self.m):
                print str(self.e[i][j]) + ' ',
            print '' 

    def __add__(self, other):
        if self.n != other.n or self.m != other.m:
            print "Error: The two matrices are of different size."
            return 
        
        r = copy.deepcopy(self)
        for i in range(r.n):
            for j in range(r.m):
                r.e[i][j] += other.e[i][j]

        return r

    def __sub__(self, other):
        if self.n != other.n or self.m != other.m:
            print "Error: The two matrices are of different size."
            return 
        
        r = copy.deepcopy(self)
        for i in range(r.n):
            for j in range(r.m):
                r.e[i][j] -= other.e[i][j]

        return r

    def __mul__(self, other):
        if self.m != other.n:
            print "Error: The first matrix's number of cloumns isn't equal to the second matrix's number of rows."
            return 

        e = []

        for i in range(self.n):
            row = []
            for j in range(other.m):
                count = number(0)
                for k in range(self.m):
                    count += self.e[i][k] * other.e[k][j]
                row += [count]
            e += [row]

        return matrix(self.n, other.m, e)

    # combine two matrices with the same number of rows.
    def __div__(self, other):
        if (self.n != other.n):
            print "Error: The two matrices are of different number of rows."
            return 
        
        r = copy.deepcopy(self)
        r.m += other.m
        for i in range(r.n):
            r.e[i] += copy.deepcopy(other.e[i])

        return r

    # combine two matrices with the same number of cloumns.
    def __mod__(self, other):
        if (self.m != other.m):
            print "Error: The two matrices are of different number of cloumns."
            return 
        
        r = copy.deepcopy(self)
        r.n += other.n
        for i in range(other.n):
            r.e += [copy.deepcopy(other.e[i])]

        return r
   
    def column(self, x):
        if (x >= self.m):
            print "Error: Invaild column number."
            return 

        vector = []
        for i in range(self.n):
            vector += [copy.deepcopy(self.e[i][x])]
        return matrix(self.n, 1, [vector])

    def row(self, x):
        if (x >= self.n):
            print "Error: Invaild row number."
            return 

        return matrix(1, self.m, [copy.deepcopy(self.e[x])])

    def transposition(self):
        e = []
        for i in range(self.m):
            row = []
            for j in range(self.n):
                row += [copy.deepcopy(self.e[j][i])]
            e += [row]
        return matrix(self.m, self.n, e)
    
    def guass(self):
        c = copy.deepcopy(self)
        e = c.e
        n = 0
        for i in range(c.m):
            pivot = -1
            for j in range(n, c.n):
                if (e[j][i] != number(0)):
                    if (pivot == -1 or e[j][i] < e[pivot][i]):
                        pivot = j
            
            if (pivot == -1):
                continue 
            
            c.e[n], c.e[pivot] = c.e[pivot], c.e[n]
            for j in range(n + 1, c.n):
                for k in range(i, c.m)[::-1]:
                    e[j][k] -= e[j][i] / e[n][i] * e[n][k]
            n += 1
        c.n = n
        return c

    def value(x):
        if (x.n != x.m):
            print "Error: The matrix isn't a determinant."
            return 
        
        x = x.guass()
        product = number(1)
        for i in range(x.n):
            product *= x.e[i][i]

        print product
    
    # output the rank of the given matrix and one of the maximal linearly independent groups of the row vectors.
    def rank(x):
        now = matrix(0, x.m)
        for i in range(x.n):
            tmp = now % x.row(i)
            if tmp.guass().n == tmp.n:
                now = tmp
        
        print now.n
        for i in range(now.n):
            row = []
            for j in range(now.m):
                row += [str(now.e[i][j])]
            print str(row).replace('\'', '')

    def solve(self):
        t = self.guass()
        if (t.n == t.m):
            print "It seems that there is no solution to this equation."
            return 
        sol = [0 for i in range(t.m - 1)]
        isPivot = [False for i in  range(t.m - 1)]
        for x in range(t.n)[::-1]:
            pivot = -1
            for i in range(t.m - 1):
                if t.e[x][i] != number(0):
                    pivot = i
                    break 
            
            isPivot[pivot] = True
            sol[pivot] = t.e[x][t.m - 1] / t.e[x][pivot]
            for i in range(0, x):
                t.e[i][t.m - 1] -= sol[pivot] * t.e[i][pivot]
        
        for i in range(t.m - 1):
            sol[i] = str(sol[i])
        print str(sol).replace('\'', '')
        print '+'
        
        free = []
        for i in range(t.m - 1):
            if isPivot[i] == False:
                free += [i]
        freeCount = len(free)
        
        k = [[number(0) for i in range(t.m - 1)] for i in range(t.m - 1)]
        for x in range(t.n)[::-1]:
            pivot = -1
            for i in range(t.m - 1):
                if (pivot == -1):
                    if t.e[x][i] != number(0):
                        pivot = i
                else:
                    if isPivot[i]:
                        for j in range(t.m - 1):
                            k[pivot][j] -= k[i][j] * t.e[x][i] / t.e[x][pivot]
                    else: 
                        k[pivot][i] -= t.e[x][i] / t.e[x][pivot]

        for x in range(freeCount):
            vector = []
            for i in range(t.m - 1):
                if i == free[x]:
                    vector += ['1']
                elif isPivot[i]:
                    vector += [str(k[i][free[x]])]
                else:
                    vector += ['0']
            print 'C' + str(x) + str(vector).replace('\'', '')
            if x == freeCount - 1:
                print 'C0...C' + str(x) + ' can be any integer.'
            else:
                print '+'


                

            
            

            
def parseNumber(s):
    if '/' in s:
        ss = s.split('/')
        return number(int(ss[0]), int(ss[1]))
    else:
        return number(int(s))

def readMatrix():
    m = 0
    e = []
    while True:
        line = sys.stdin.readline().strip('\n').split()
        if (len(line) == 1 and line[0] == 'end'):
            return matrix(len(e), m, e) 
        if m == 0:
            m = len(line)
        elif m != len(line):
            print("Error: The total of numbers isn't equal to the previous row, please re-enter the row.")
            continue 
        row = []
        for i in range(m):
            try:
                row += [parseNumber(line[i])]
            except:
                print("Error: Unable to recognize the numbers, please re-enter the row.")
        if len(row) == m:
            e += [row]

# execution division
dic = {}    
def execute(line):
    if (line[0][0] == ':'):
        if (line[0] == ':show'):
            dic[line[1]].show()
        elif (line[0] == ':read'):
            dic[line[1]] = readMatrix()
        elif (line[0] == ':value'):
            dic[line[1]].value()
        elif (line[0] == ':rank'):
            dic[line[1]].rank()
        elif (line[0] == ':solve'):
            dic[line[1]].solve()
        else:
            print "Can't recognize the instruction."
    elif (len(line)  < 3 or line[1] != '='):
        print "Can't recognize the instruction."
    else:
        if (len(line) == 3):
            res = copy.deepcopy(dic[line[2]])
        elif (line[3] == '-t'):
            res = dic[line[2]].transposition()
        elif (line[3] == '-g'):
            res = dic[line[2]].guass()
        elif (len(line) < 5):
            print "Can't recognize the instruction."
            return 
        elif (line[3] == '+'):
            res = dic[line[2]] + dic[line[4]]
        elif (line[3] == '-'):
            res = dic[line[2]] - dic[line[4]]
        elif (line[3] == '*'):
            res = dic[line[2]] * dic[line[4]]
        elif (line[3] == '/'):
            res = dic[line[2]] / dic[line[4]]
        elif (line[3] == '%'):
            res = dic[line[2]] % dic[line[4]]
        
        try:
            dic[line[0]] = res
        except:
            pass

def main():
    while True:
        sys.stdout.write(cl('>>>', 'blue') + ' ')
        line = sys.stdin.readline().strip('\n').split()
        if (len(line) == 0):
            continue
        if (line[0] == ':quit'):
            return 

        try:
            execute(line)
        except Exception, e:
            print e

if __name__ == '__main__':
    main()

