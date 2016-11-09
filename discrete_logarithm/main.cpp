///////////////////////////////////////////////////////////////////////////////
//        copyright (c) 2012-2017 Oscar Riveros. all rights reserved.        //
//                           oscar.riveros@peqnp.com                         //
//                                                                           //
//    without any restriction, Oscar Riveros reserved rights, patents and    //
//  commercialization of this knowledge or derived directly from this work.  //
///////////////////////////////////////////////////////////////////////////////

#include <cmath>
#include <iostream>
#include <boost/progress.hpp>
#include <boost/multiprecision/cpp_int.hpp>

namespace mp = boost::multiprecision;

typedef mp::cpp_int Z;

boost::progress_timer timer;

Z e;
Z m;

Z functor(Z h) {
    return mp::powm(h, e, m);
}

int bits(Z n) {
    auto s = 0;
    while (n) {
        s += static_cast<int>(n % 2 == 0);
        n /= 2;
    }
    return s;
}

Z abstract_binary_search(Z secret) {
    Z k = 0;
    Z l = m;
    Z global = m;
    while (l - k != 1) {
        Z i = k;
        Z j = l;
        while (j - i != 1) {
            Z n = (i + j) / 2;
            Z key = functor((n + k) % l);
            if (key < secret) {
                Z local = bits(mp::abs(key - secret));
                if (local < global) {
                    global = local;
                    std::cout << global << " => " << timer.elapsed() << " (s)" << std::endl;
                }
                i = n;
            } else if (key > secret) {
                j = n;
            } else { return (n + k) % l; }
        }
        k++;
    }
    return 0;
}

int main(int argc, char *argv[]) {

    e = Z(argv[1]);
    m = Z(argv[2]);

    Z secret = Z(argv[3]);

    if (secret > m) { exit(EXIT_FAILURE); }

    std::cout << "secret          => " << secret << "\n" << std::endl;

    Z key = abstract_binary_search(functor(secret));

    std::cout << "\n" << "key             => " << key << "\n" << std::endl;

    return EXIT_SUCCESS;
}