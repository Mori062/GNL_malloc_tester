#!/bin/bash

cp ../get_next_line.c .
cp ../get_next_line_utils.c .

sed -i 's/malloc/fmalloc/g' get_next_line.c
sed -i 's/malloc/fmalloc/g' get_next_line_utils.c

for i in $(seq 0 50)
do
    cc -Wall -Werror -Wextra get_next_line_bonus.c get_next_line_utils_bonus.c test.c -D N=$i -o gnl
    ./gnl > /dev/null 2>&1
    if [ $? != 0 ]
    then
        echo "\x1b[31m malloc KO \x1b[0m"
    else
        echo "\x1b[32m malloc OK \x1b[0m"
    fi
    i=$((i+1))
    sleep 0.2
    rm ./gnl
done