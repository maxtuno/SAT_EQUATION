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

    uu = [1, 1094, 872, 1528, 2202, 3848, 1679, 3709, 541, 3072, 891, 3898, 1990, 794, 1459, 2256, 1586, 1945, 2666, 390, 629, 1306, 2152, 1862, 501, 2330, 3516, 2905, 2415, 2565, 3227, 3792, 3725, 288, 2536, 1696, 115, 3954, 951, 2726, 1001, 3554, 2864, 3670, 1365, 2762, 2934, 2169, 188, 2361, 1428, 3251, 824, 3435, 708, 1136, 3308, 3452, 2040, 3021, 3629, 1503, 2825, 991, 254, 3571, 642, 74, 1746, 1616, 3968, 587, 1822, 1253, 240, 1357, 340, 3823, 2116, 2966, 3119, 1240, 468, ]
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
