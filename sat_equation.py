"""
///////////////////////////////////////////////////////////////////////////////
//        copyright (c) 2012-2017 Oscar Riveros. all rights reserved.        //
//                           oscar.riveros@peqnp.com                         //
//                                                                           //
//    without any restriction, Oscar Riveros reserved rights, patents and    //
//  commercialization of this knowledge or derived directly from this work.  //
///////////////////////////////////////////////////////////////////////////////
"""

"""
FUNDAMENTAL LAW OF BINARY THEORIES
UNIVERSAL NUMBER THEORY EQUATION OF SAT
https://www.academia.edu/27914083/FUNDAMENTAL_LAW_OF_BINARY_THEORIES_-_UNIVERSAL_NUMBER_THEORY_EQUATION_OF_SAT
http://twitter.com/maxtuno
"""


def bits(n, p):
    s = []
    while n:
        s = [n % 2 == 0] + s
        n //= 2
    s += (p - len(s)) * [False]
    return s


def sat_equation(cnf, n, m):
    sat = 0
    for j in range(m):
        v = 0
        for i in range(n):
            v += int(cnf[j][n - 1 - i] > 0) * 2 ** i
        sat += 2 ** v
    return sat


if __name__ == '__main__':

    import sys
    import csv
    import time

    ini = time.time()

    with open(sys.argv[1]) as csvfile:
        spam_reader = csv.reader(csvfile, delimiter=' ')
        n, m = map(int, next(spam_reader))
        cnf = []
        for row in spam_reader:
            cnf += [eval(', '.join(row))[:-1]]

    print(bits(sat_equation(cnf, n, m), 2 ** n))

    end = time.time()

    print('\ntime: {} (s)'.format(end - ini))
