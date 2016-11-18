#include <cmath>
#include <cstdlib>
#include <iostream>
#include <thread>
#include <fstream>
#include <map>
#include <vector>
#include <mutex>

void functor(std::ifstream &data_stream, std::map<std::string, unsigned> &kv, std::mutex &stream_mutex) {
    std::string stream;
    while (!data_stream.eof()) {
        if (stream_mutex.try_lock()) {
            data_stream >> stream;
            kv[stream]++;
            stream_mutex.unlock();
        }
    }
};

int main(int argc, char *argv[]) {

    auto size = std::atoi(argv[1]);
    std::ifstream data_stream(argv[2]);

    std::map<std::string, unsigned> kv;

    std::mutex stream_mutex;
    std::vector<std::thread> threads(size);

    std::chrono::time_point<std::chrono::system_clock> start, end;
    start = std::chrono::system_clock::now();

    for (auto &t : threads) { t = std::thread(functor, std::ref(data_stream), std::ref(kv), std::ref(stream_mutex)); }
    for (auto &t : threads) { t.join(); }

    for (auto &e : kv) {
        std::cout << e.first << " => " << e.second << std::endl;
    }

    end = std::chrono::system_clock::now();

    std::chrono::duration<double> elapsed_seconds = end - start;
    std::time_t end_time = std::chrono::system_clock::to_time_t(end);

    std::cout << "\ntime : " << elapsed_seconds.count() << " (s)" << std::endl;

    return EXIT_SUCCESS;
}