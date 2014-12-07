#!/bin/bash

if  [ $# -ne 1 ]
then
    echo "usage <extractAtomLinks.sh> <filename> "
    echo "e.g., extractHtml.sh  blogLinksLists.txt"
    exit
fi

md5link="blogAtomLinks.txt"
filename=`readlink -f $1`

for line in `cat $filename`
do
    blogLink=$line
    hash="$(echo " $blogLink "|md5sum | cut -f1 -d' ' )"
    echo "$line  $hash" >> $md5link
    curl $line  -o /home/bbokka/cs594/A9/Q1/atom/"$hash.htm"
done