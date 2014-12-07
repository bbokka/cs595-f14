#!/bin/bash

if  [ $# -ne 1 ]
then
    echo "usage <extractLinks.sh> <number of links> "
    echo "e.g.,extractLinks.sh 98 "
    exit
fi

numberOfLinks=$1

link1="http://f-measure.blogspot.com/"
link2="http://ws-dl.blogspot.com/"

echo "$link1" > blogLinksLists.txt
echo "$link2" >> blogLinksLists.txt

for (( count=1; count<=$numberOfLinks; count++ ))
do
   curl -I -L 'http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117' | grep Location | tail -n 1 | cut -d" " -f2 | cut -d"?" -f 1 >> blogLinksLists.txt
done

