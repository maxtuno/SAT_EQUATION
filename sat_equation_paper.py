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
    s = (p - len(s)) * [True] + s
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
    cnf = [(1, -2, 3), (1, -2, -3), (-1, 2, -3)]

    n = 3
    m = len(cnf)

    print(bits(sat_equation(cnf, n, m), 2 ** n))

    print("""
    (a|~b|c)&(a|~b|~c)&(~a|b|~c)
    a      b      c      value
    False  False  False  True
    False  False  True   True
    False  True   False  False
    False  True   True   False
    True   False  False  True
    True   False  True   False
    True   True   False  True
    True   True   True   True
    """)

    cnf = (1, 2, 3, -4), (1, 2, -3, -4), (1, -2, 3, -4), (1, -2, -3, -4), (-1, 2, 3, -4), (-1, 2, -3, 4), (-1, -2, 3, 4), (-1, -2, -3, 4)

    n = 4
    m = len(cnf)

    print(bits(sat_equation(cnf, n, m), 2 ** n))

    print("""
    (a|b|c|~d)&(a|b|~c|~d)&(a|~b|c|~d)&(a|~b|~c|~d)&(~a|b|c|~d)&(~a|b|~c|d)&(~a|~b|c|d)&(~a|~b|~c|d)
    a      b      c      d      value
    False  False  False  False  True
    False  False  False  True   False
    False  False  True   False  True
    False  False  True   True   False
    False  True   False  False  True
    False  True   False  True   False
    False  True   True   False  True
    False  True   True   True   False
    True   False  False  False  True
    True   False  False  True   False
    True   False  True   False  False
    True   False  True   True   True
    True   True   False  False  False
    True   True   False  True   True
    True   True   True   False  False
    True   True   True   True   True
    """)
