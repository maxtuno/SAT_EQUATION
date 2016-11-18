#!/usr/bin/env bash
g++-6 -std=c++17 -march=native -Os -fopenmp -D_GLIBCXX_PARALLEL -o word_count main.cpp