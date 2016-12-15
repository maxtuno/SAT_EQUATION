def load(file_name):
    global mm
    with open(file_name) as msp_file:
        spam_reader = csv.reader(msp_file, delimiter=' ')
        uu = []
        for row in spam_reader:
            if row[0] == 'e':
                mm[int(row[1]), int(row[2])] = 1
                mm[int(row[2]), int(row[1])] = 1
                if int(row[1]) not in uu:
                    uu.append(int(row[1]))
                if int(row[2]) not in uu:
                    uu.append(int(row[2]))
    return uu


if __name__ == '__main__':

    import csv
    import matplotlib.pyplot as plt
    import networkx as nx

    mm = {}

    # http://www.nlsde.buaa.edu.cn/~kexu/benchmarks/graph-benchmarks.htm
    uu = load('/Users/mx/Documents/Mars/Clion/sql_peqnp/bin/frb100-40.clq')

    uu = [2747, 1094, 879, 1651, 1555, 2611, 2216, 46, 3867, 535, 1895, 3713, 1945, 907, 3049, 3827, 1151, 765, 3898, 1515, 1452, 362, 603, 674, 1289, 2671, 1753, 1857, 481, 26, 220, 3115, 1818, 347, 446, 144, 2992, 277, 1627, 2523, 2801, 3339, 840, 2031, 1595, 2359, 401, 1719, 1420, 2889, 2410, 2047, 1988, 2941, 176, 3513, 3440, 1220, 3550, 2777, 2135, 301, 2484, 737, 3654, 3579, 598, 87, 1041, 3441, 712, 3011, 2085, 3748, 1387, 2367, 1279, 3286, 985, 3279, 2865, 2599, ]
    gg = []
    for i in uu:
        for j in uu:
            if mm.get((i, j)):
                gg.append((i, j))

    plt.figure(figsize=(20, 20))
    G = nx.Graph(gg)

    print(G.degree(uu))
    print(set(G.degree(uu).values()), len(uu))

    nx.draw(G)
    plt.savefig('graph_g.png')
    plt.clf()
