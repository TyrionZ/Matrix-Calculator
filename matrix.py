def __init__(self, n = 0, m = 0, e = []): 
    self.n = n
    self.m = m
    self.e = e

def show(self):
    for i in range(self.n):
        for j in range(self.m):
            if (self.e[i][j].q == 1):
                print self.e[i][j].p,
            else:
                print str(self.e[i][j].p) + '/' + str(self.e[i][j].q),
            print ' ',
        print '' 

