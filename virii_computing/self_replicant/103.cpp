/*
 *        copyright (c) 2012-2017 Oscar Riveros. all rights reserved.
 *                           oscar.riveros@peqnp.com
 *
 *    without any restriction, Oscar Riveros reserved rights, patents and
 *  commercialization of this knowledge or derived directly from this work.
 */

#include <chrono>
#include <sstream>
#include <fstream>
#include <iostream>
#include <cmath>
#include <ctime>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>

typedef boost::multiprecision::cpp_int Z;

int phi(std::vector<int> uu, Z n) {
    auto s = 0;
    auto i = 0;
    while (n) {
        if (n % 2) { s += uu.at(i); }
        n /= 2;
        i++;
    }
    return s;
};

int main(int argc, char *argv[]) {

    auto now = std::chrono::high_resolution_clock::now();

    std::string root_name = argv[0];
    std::ifstream root(root_name);

    std::ifstream instance("universe.txt");

    int target;
    int element;
    instance >> target;
    std::vector<int> uu;
    while (instance.good()) {
        instance >> element;
        uu.push_back(element);
    }

    std::sort(uu.begin(), uu.end());

    Z i, j;
    if (argc == 1) {
        std::srand(std::time(NULL));
        i = std::rand();
        j = i + (Z(1) << (uu.size() - 1));
    } else {
        i = Z(argv[1]);
        j = Z(argv[2]);
    }

    Z n = (i + j) / 2;
    auto subset_sum = phi(uu, n);
    if (subset_sum < target) { i = n; } else if (subset_sum > target) { j = n; }

    std::cout << subset_sum << " " << n << std::endl;

    std::stringstream leaf_name;
    leaf_name << n + 1;
    leaf_name << ".virii";

    std::ofstream leaf(leaf_name.str());
    leaf << root.rdbuf();
    leaf.close();

    if (subset_sum == target) {

        std::cout << "EUREKA!!!" << std::endl;

        std::ofstream solution("solution.txt");
        auto i = 0;
        solution << subset_sum << " [";
        while (n) {
            if (n % 2) { solution << uu.at(i) << ", "; }
            n /= 2;
            i++;
        }
        solution << "]" << std::endl;
        solution.close();

        std::system("pkill *.virii");
        std::system("rm -R *.virii");

        return EXIT_SUCCESS;
    } else {

        std::stringstream cmd;
        cmd << "chmod 777 " << leaf_name.str() << " && ./" << leaf_name.str() << " " << i << " " << j;

        return std::system(cmd.str().c_str());
    }
}
