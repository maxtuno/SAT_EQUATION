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


def sat_equation_satisfiability(cnf, n, m):
    """
    P = NP
    """
    sat = 0
    for j in range(m):
        for i in range(n):
            sat += int(cnf[j][n - 1 - i] > 0)
    return sat != (m // 2) * n or 2 ** (m.bit_length() - 1) != m


if __name__ == '__main__':

    import sys
    import csv
    import time

    ini = time.time()

    with open(sys.argv[1]) as abs_file:
        spam_reader = csv.reader(abs_file, delimiter=' ')
        n, m = map(int, next(spam_reader))
        cnf = []
        for row in spam_reader:
            cnf += [eval(', '.join(row))[:-1]]

    print('is satisfiable? {}'.format(sat_equation_satisfiability(cnf, n, m)))

    end = time.time()

    print('\ntime: {} (s)'.format(end - ini))
