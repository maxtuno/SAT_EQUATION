///////////////////////////////////////////////////////////////////////////////
//        copyright (c) 2012-2017 Oscar Riveros. all rights reserved.        //
//                           oscar.riveros@peqnp.com                         //
//                                                                           //
//    without any restriction, Oscar Riveros reserved rights, patents and    //
//  commercialization of this knowledge or derived directly from this work.  //
///////////////////////////////////////////////////////////////////////////////

#include <cmath>
#include <iostream>
#include <numeric>
#include <random>
#include <boost/progress.hpp>
#include <boost/numeric/ublas/io.hpp>
#include <boost/numeric/ublas/vector.hpp>
#include <boost/multiprecision/cpp_int.hpp>

namespace mp = boost::multiprecision;
namespace ublas = boost::numeric::ublas;

typedef mp::cpp_int Z;

boost::progress_timer timer;

int size;
int dimension;

template<typename T>
std::vector<ublas::vector<T>> phi(std::vector<ublas::vector<T>> &universe, Z n) {
    std::vector<ublas::vector<T>> subset;
    for (auto i = 0; i < universe.size(); i++) {
        if (n % 2 == 0) { subset.push_back(universe[i]); }
        n /= 2;
    }
    return subset;
}

template<typename T>
double functor(std::vector<ublas::vector<T>> subset, ublas::vector<T> target) {
    return ublas::norm_2(std::accumulate(subset.begin(), subset.end(), ublas::vector<T>(dimension, T(0)), std::plus<ublas::vector<T>>()) - target);
}

template<typename T>
std::vector<ublas::vector<T>> abstract_binary_search(std::vector<ublas::vector<T>> universe, ublas::vector<T> target) {
    Z k = 0;
    Z l = (Z(1) << universe.size());
    double global = std::numeric_limits<double>::max();
    while (l - k != 1) {
        begin:
        Z i = k;
        Z j = l;
        while (j - i != 1) {
            Z n = (i + j) / 2;
            auto subset = phi<T>(universe, (k + n) % l);
            double local = functor<double>(subset, target);
            if (local > global) {
                i = n;
            } else if (local < global) {
                j = n;
                global = local;
                std::cout << global << " => " << timer.elapsed() << " (s)" << std::endl;
                if (!global) { return subset; }
                k = 0;
                goto begin;
            } else { break; }
        }
        k++;
    }
    return std::vector<ublas::vector<T>>();
}

int main(int argc, char *argv[]) {

    size = std::atoll(argv[1]);
    dimension = std::atoll(argv[2]);

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<double> dis(-size, size);

    std::cout << "universe     : [";
    std::vector<ublas::vector<double>> universe(size);
    for (auto &vector : universe) {
        vector.resize(dimension);
        for (auto &element : vector) {
            element = dis(gen);
        }
        std::cout << vector << ", ";
    }
    std::cout << "]\n" << std::endl;

    ublas::vector<double> target(dimension);
    for (auto i = 0; i < size; i++) {
        if (i % 2) {
            if (!i) { target = universe[i]; }
            else { target += universe[i]; }
        }
    }

    std::sort(universe.begin(), universe.end(), [&target](auto x, auto y) { return ublas::norm_2(target - x) < ublas::norm_2(target - y) ;} );

    std::cout << "target       : " << target << "\n" << std::endl;

    auto subset = abstract_binary_search<double>(universe, target);

    std::cout << "\nsum subset   : " << std::accumulate(subset.begin(), subset.end(), ublas::vector<double>(dimension, 0), std::plus<ublas::vector<double>>()) << "\n" << std::endl;

    std::cout << "subset       : [";
    for (auto &vector : subset) {
        std::cout << vector << ", ";
    }
    std::cout << "]\n" << std::endl;
    
    return EXIT_SUCCESS;
}
