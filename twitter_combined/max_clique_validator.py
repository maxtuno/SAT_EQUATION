"""
/*
 *        copyright (c) 2012-2017 Oscar Riveros. all rights reserved.
 *                           oscar.riveros@peqnp.com
 *
 *    without any restriction, Oscar Riveros reserved rights, patents and
 *  commercialization of this knowledge or derived directly from this work.
*/

https://twitter.com/maxtuno

data => http://snap.stanford.edu/data/egonets-Twitter.html
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

    uu = load('twitter_combined.txt')

    uu = [18848018, 256497288, 270231980, 271658840, 273452154, 286481552, 287906361, 290176149, 290929161, 291245327, 292030309, 292608038, 292915903, 293802222, 294290268, 294361452, 295062437, 295355360, 296171243, 297042642, 297229855, 297358566, 298376225, 299105597, 299243917, 300007014, 300385517, 300461530, 301282103, 301529877, 301721565, 301726492, 301869137, 307121607, 309012614, 312217057, 320140485, 321096972, 325116715, 325954622, 338614678, 343051634, 349872060, 349932090, 351641666, 354139446, 355743081, 357227113, 357740963, 360094552, 368829926, 370352650, 372499406, 374833275, 379644023, 388622544, 395873820, 397464131, 399527237, 399644859, 399651919, 466311355, 523832656, 554402185, 555800132, ]

    gg = []
    for i in uu:
        for j in uu:
            if mm.get((i, j)):
                gg.append((i, j))

    G = nx.Graph(gg)

    print(G.degree(uu))
    print(set(G.degree(uu).values()), len(uu))
