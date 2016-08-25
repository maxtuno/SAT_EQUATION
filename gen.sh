#!/usr/bin/env bash
# pip install cnfgen
# <k> <n> <m>
# Note: <k> = <n>
# Need Edit Comments
# k = n % m = 2^m => unsatisfiable
cnfgen randkcnf 11 11 2048 > cnf_polynomial_unsat.abs
cnfgen randkcnf 11 11 2047 > cnf_polynomial_sat.abs