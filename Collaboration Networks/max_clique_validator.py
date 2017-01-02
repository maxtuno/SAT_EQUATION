"""
/*
 *        copyright (c) 2012-2017 Oscar Riveros. all rights reserved.
 *                           oscar.riveros@peqnp.com
 *
 *    without any restriction, Oscar Riveros reserved rights, patents and
 *  commercialization of this knowledge or derived directly from this work.
*/

https://twitter.com/maxtuno
"""

def load(file_name):
    global mm
    with open(file_name) as msp_file:
        spam_reader = csv.reader(msp_file, delimiter='\t')
        uu = []
        for row in spam_reader:
            mm[int(row[0]), int(row[1])] = True
            mm[int(row[1]), int(row[0])] = True
            if int(row[0]) not in uu:
                uu.append(int(row[0]))
            if int(row[1]) not in uu:
                uu.append(int(row[1]))
    return uu


if __name__ == '__main__':

    import csv
    import networkx as nx

    mm = {}

    uu = load('CA-HepTh.txt')

    uu = [55443, 53450, 51840, 51294, 47542, 46344, 42819, 40435, 38500, 38055, 37963, 26398, 25092, 24711, 23825, 19470, 18433, 15618, 5339, 11078, 10431, 6543, 6517, 6055, 361, 32833, 48098, 6254, 39085, 49074, 49958, ]

    gg = []
    for i in uu:
        for j in uu:
            if mm.get((i, j)):
                gg.append((i, j))

    G = nx.Graph(gg)

    print(G.degree(uu))
    print(set(G.degree(uu).values()), len(uu))
