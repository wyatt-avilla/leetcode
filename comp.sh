#!/bin/bash

if [ $# != 1 ] && [ $# != 2 ]; then
    echo "bad number of args..."
    exit 1
fi

gcc -Wall -Wextra -g -O0 "$1" # compile...

if [ ! -f ./a.out ]; then
    echo "fix the error q_q"
    exit 1
fi


if [ "$2" == "-v" ]; then #valgrind
    echo "-----------------------------------------"
    ./a.out
    echo "-----------------------------------------"
    valgrind --leak-check=full --show-reachable=yes -s --show-leak-kinds=all --error-exitcode=1 --track-origins=yes ./a.out > /dev/null
else
    ./a.out
fi

rm ./a.out