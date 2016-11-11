cmake_minimum_required(VERSION 3.5)
project(mssp)

set(CMAKE_BUILD_TYPE Release)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/lib)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14 -Os")

find_package(Boost REQUIRED COMPONENTS)
include_directories({Boost_INCLUDE_DIRS})

set(SOURCE_FILES main.cpp)
add_executable(mssp ${SOURCE_FILES})
