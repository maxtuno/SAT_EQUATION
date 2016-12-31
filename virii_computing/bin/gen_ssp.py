if __name__ == '__main__':

    import random

    size = 100
    uu = [random.randint(1, 2 ** 10 - 1) for _ in range(100)]

    instance = open('universe.txt', 'w')

    print(sum(random.sample(uu, k=len(uu) // 2)), file=instance)
    for e in uu:
        print(e, file=instance)

    instance.close()
