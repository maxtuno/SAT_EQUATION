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
        spam_reader = csv.reader(msp_file, delimiter=' ')
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

    # data => http://networkrepository.com/soc-google-plus.php
    uu = load('soc-google-plus.txt')

    uu =  [151197, 64420, 145647, 40718, 92118, 41061, 155890, 18190, 119748, 208659, 160556, 203266, 179094, 22672, 54349, 120411, 109154, 65211, 59305, 144684, 208638, 50032, 172039, 200153, 151408, 2314, 119610, 30804, 104600, 62163, 110598, 35748, 187156, 94279, 40733, 22550, 88212, 79829, 15339, 27987, 46395, 46738, 38689, 27573, 71961, 23503, 170473, 106658, 195155, 39375, 187535, 90590, 124093, 109243, 210648, 54257, 103760, 206482, 109349, 207367, 209488, 167627, 45848, 101564, 16093, ]

    gg = []
    for i in uu:
        for j in uu:
            if mm.get((i, j)):
                gg.append((i, j))

    G = nx.Graph(gg)

    print(G.degree(uu))
    print(set(G.degree(uu).values()), len(uu))
