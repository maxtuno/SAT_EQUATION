"""
/*
 *        copyright (c) 2012-2017 Oscar Riveros. all rights reserved.
 *                           oscar.riveros@peqnp.com
 *
 *    without any restriction, Oscar Riveros reserved rights, patents and
 *  commercialization of this knowledge or derived directly from this work.
*/

https://twitter.com/maxtuno

data => http://snap.stanford.edu/data/egonets-Facebook.html
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

    uu = load('facebook_combined.txt')

    uu = [1917, 1912, 2206, 2266, 2123, 2078, 2218, 2464, 2073, 2507, 2220, 2340, 2240, 2142, 2059, 2410, 2586, 2090, 2604, 1938, 2118, 2229, 1962, 2150, 2309, 2088, 2244, 2590, 1943, 2275, 2624, 2104, 2172, 2184, 2131, 2356, 2201, 2188, 2428, 2064, 2103, 1983, 1946, 2601, 2602, 2414, 2607, 1993, 2331, 2139, 2290, 2560, 2655, 2124, 2030, 2564, 2542, 1984, 2108, 2578, 2482, 2308, 2326, 2121, 2611, 2395, 2460, 2526, 2520, ]

    gg = []
    for i in uu:
        for j in uu:
            if mm.get((i, j)):
                gg.append((i, j))

    G = nx.Graph(gg)

    print(G.degree(uu))
    print(set(G.degree(uu).values()), len(uu))
