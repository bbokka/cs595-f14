#!/bin/bash

if  [ $# -ne 1 ]
then
    echo "usage <extractHtml.sh> <filename> "
    echo "e.g., extractHtml.sh  uniqueUri.txt "
    exit
fi
md5uri="md5Uri.txt"
filename=`readlink -f $1`

for line in `cat $filename`
do
    md5=$line
    hash="$(echo " $md5 "|md5sum | cut -f1 -d' ' )"
    echo "$line  $hash" >> $md5uri
    curl -A "Mozilla/4.0" --connect-timeout 30 $line  -o "$hash.htm"
done
