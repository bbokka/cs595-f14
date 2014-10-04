#!/bin/bash

if  [ $# -ne 1 ]
then
    echo "usage findKeyword.sh <folder name> "
    echo "e.g., findKeyword  <html> "
    exit
fi

plain="/home/bbokka/cs594/Assignment/programs/plain_content"

dir=`readlink -f "$1"`
for file in `ls $dir`
do
	filename=$plain/"$file"
    var=`grep -c "food" "$filename"`
    var1=`wc -w $filename`
    echo "$var  $file " #>> word_count.txt   
done