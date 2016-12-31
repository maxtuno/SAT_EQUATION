cmake_minimum_required(VERSION 3.6)
project(self_replicant)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/../bin)

set(CMAKE_CXX_FLAGS "-march=native -std=c++14 -Os")
set(CMAKE_CXX_COMPILER /opt/llvm/bin/clang++)

set(SOURCE_FILES 103.cpp)

add_executable(virii ${SOURCE_FILES})
