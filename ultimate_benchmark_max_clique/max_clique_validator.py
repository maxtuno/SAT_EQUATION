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

    jj = [2, 1109, 879, 1555, 2216, 1663, 3864, 3684, 2641, 907, 1923, 523, 618, 393, 3048, 1303, 1151, 3888, 764, 1858, 1718, 1448, 1977, 3817, 2128, 1590, 2267, 3505, 2561, 2404, 3777, 219, 2520, 2193, 2601, 1220, 1482, 2441, 2914, 3100, 818, 678, 497, 3187, 1909, 2801, 3583, 67, 1344, 1742, 349, 3300, 2926, 2009, 2970, 1785, 265, 1808, 1622, 2332, 455, 300, 989, 3952, 3201, 2096, 3144, 3977, 1035, 2797, 3731, 1079, 2546, 3267, 3649, 701, 3457, 120, 3635, 1395, 1255, 2370, 2753, 124, ]

    mm = {}

    # http://www.nlsde.buaa.edu.cn/~kexu/benchmarks/graph-benchmarks.htm
    uu = load('/Users/mx/Documents/Mars/Clion/Parallel/bin/frb100-40.clq')

    uu = jj
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
