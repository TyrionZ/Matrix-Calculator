import rational
import copy

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
                count = rational.number(0)
                for k in range(self.m):
                    count += self.e[i][k] * other.e[k][j]
                row += [count]
            e += [row]

        return matrix(self.n, other.m, e)

    # combine two matrices with the same number of rows.
    def __div__(self, other):
        if (self.n != other.n):
            print "Error: The two matrices are of different rational.number of rows."
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
                if (e[j][i] != rational.number(0)):
                    if (pivot == -1 or e[j][i] < e[pivot][i]):
                        pivot = j
            
            if (pivot == -1):
                continue 
            
            e[n], e[pivot] = e[pivot], e[n]
            for j in range(n + 1, c.n):
                for k in range(i, c.m)[::-1]:
                    e[j][k] -= e[j][i] / e[n][i] * e[n][k]
            n += 1
        c.n = n
        return c
    
    def simplify(self):
        c = self.guass() 
        e = c.e
        for i in range(c.n):
            pivot = -1
            for j in range(c.m):
                if e[i][j] != rational.number(0):
                    pivot = j
                    break

            for j in range(c.m)[::-1]:
                e[i][j] /= e[i][pivot]

            for j in range(i):
                for k in range(pivot, c.m)[::-1]:
                    e[j][k] -= e[i][k] * e[j][pivot] / e[i][pivot]

        return c

    def value(x):
        if (x.n != x.m):
            print "Error: The matrix isn't a determinant."
            return 
        
        x = x.guass()
        product = rational.number(1)
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
                if t.e[x][i] != rational.number(0):
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
        
        k = [[rational.number(0) for i in range(t.m - 1)] for i in range(t.m - 1)]
        for x in range(t.n)[::-1]:
            pivot = -1
            for i in range(t.m - 1):
                if (pivot == -1):
                    if t.e[x][i] != rational.number(0):
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
