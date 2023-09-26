#!/bin/bash

cp ../get_next_line.c .
cp ../get_next_line_utils.c .
cp ../get_next_line.h .

python3 sed.py
python3 insert.py

error_count=0

for i in $(seq 0 50)
do
    cc -Wall -Werror -Wextra get_next_line.c get_next_line_utils.c test.c -D N=$i -o gnl
    ./gnl > /dev/null 2>&1
    if [ $? != 0 ]
    then
        echo "\x1b[31m [$i] malloc KO \x1b[0m"
        error_count=$((error_count+1))
    else
        echo "\x1b[32m [$i] malloc OK \x1b[0m"
    fi
    i=$((i+1))
    sleep 0.05
    rm ./gnl
done
if [ $error_count != 0 ]
then
    echo "\x1b[31m $error_count malloc errors \x1b[0m"
else
    echo "\x1b[32m No malloc errors!\x1b[0m"
fi
