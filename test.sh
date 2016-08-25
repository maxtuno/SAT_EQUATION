#!/usr/bin/env bash

for i in {1..16}
do
    echo "\n"$(( $i )) "------------------------------------------------------------"

    cnfgen randkcnf $i $i $(( RANDOM % (2 ** $i - 1 + 1) + 1 )) > cnf_polynomial_sat.abs
    echo "\nSAT"
    python3 sat_equation_polynomial_satisfiability_abs.py cnf_polynomial_sat.abs

    echo "\nUNSAT"
    cnfgen randkcnf $i $i $(( 2 ** $i )) > cnf_polynomial_unsat.abs
    python3 sat_equation_polynomial_satisfiability_abs.py cnf_polynomial_unsat.abs
done