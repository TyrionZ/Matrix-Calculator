import sys
import copy
from termcolor import colored as cl
import rational
import matrix
import os

def parseNumber(s):
    if '/' in s:
        ss = s.split('/')
        return rational.number(int(ss[0]), int(ss[1]))
    else:
        return rational.number(int(s))

def readMatrix(f = sys.stdin):
    m = 0
    e = []
    while True:
        line = f.readline().strip('\n').split()
        if (len(line) == 1 and line[0] == 'end'):
            return matrix.matrix(len(e), m, e) 
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
def save():
    f = open(os.path.expanduser('~') + '/.matrix.bak', 'w')
    for p in dic:
        x = dic[p]
        f.write(p + '\n')
        for i in range(x.n):
            for j in range(x.m):
                f.write(str(x.e[i][j]) + ' ')
            f.write('\n')
        f.write('end\n')
    f.close()
    

def load(s = '/.matrix.bak'):
    f = open(os.path.expanduser('~') + s, 'r')
    while True:
        line = f.readline()
        if line == '':
            return 
        if line == '\n':
            continue 
        
        dic[line.strip('\n')] = readMatrix(f)
    f.close()
    
def clear():
    global dic
    dic = {}


def execute(line):
    try:
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
            elif (line[0] == ':clear'):
                clear()
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
            elif (line[3] == '-sg'):
                res = dic[line[2]].simplify()
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
            elif (line[3] == 'U'):
                res = dic[line[2]].union(dic[line[4]])
            elif (line[3] == 'I'):
                res = dic[line[2]].intersect(dic[line[4]])
            dic[line[0]] = res
    except Exception as e:
        raise e


def main():
    load()
    while True:
        sys.stdout.write(cl('>>>', 'blue') + ' ')
        line = sys.stdin.readline().strip('\n').split()
        if (len(line) == 0):
            continue
        if (line[0] == ':quit'):
            return 

        try:
            execute(line)
            save()
        except Exception as e:
            print e


if __name__ == '__main__':
    main()

