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
    sat = (m * n) // 2
    for j in range(m):
        for i in range(len(cnf[j])):
            sat -= int(cnf[j][i] > 0)
    return sat != 0 or 2 ** (m.bit_length() - 1) != m


if __name__ == '__main__':

    import sys
    import csv
    import time

    ini = time.time()

    with open(sys.argv[1]) as abs_file:
        spam_reader = csv.reader(abs_file, delimiter=' ')
        cnf = []
        n, m = 0, 0
        for spam in list(spam_reader):
            if spam[0] == 'p':
                _, _, n, m = spam
                n, m = int(n), int(m)
            if spam[0] != 'p' and spam[0] != 'c':
                cnf += [list(map(int, spam))[:-1]]

    print('is satisfiable? {}'.format(sat_equation_satisfiability(cnf, n, m)))

    end = time.time()

    print('\ntime: {} (s)'.format(end - ini))
