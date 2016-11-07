"""
///////////////////////////////////////////////////////////////////////////////
//        copyright (c) 2012-2017 Oscar Riveros. all rights reserved.        //
//                           oscar.riveros@peqnp.com                         //
//                                                                           //
//    without any restriction, Oscar Riveros reserved rights, patents and    //
//  commercialization of this knowledge or derived directly from this work.  //
///////////////////////////////////////////////////////////////////////////////
"""

import csv


def load(file_name):
    subsets = []
    with open(file_name) as msp_file:
        spam_reader = csv.reader(msp_file, delimiter=' ')
        _, _, bits, _ = next(spam_reader)
        universe = list(range(1, int(bits) + 1))
        for row in spam_reader:
            subsets.append(list(map(int, row[1:])))
    return universe, subsets


def main(file_name):
    universe, subsets = load(file_name)
    cover = []
    for subset in subsets:
        cover += subset
    if len(cover) - len(set(cover)) == 0:
        print('OK!, all subsets are disjoint...')
    else:
        print(':(')


if __name__ == '__main__':
    main('msc.sol')
