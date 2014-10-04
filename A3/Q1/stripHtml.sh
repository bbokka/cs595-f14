#!/bin/bash

# to scrape the html from the files.
# checking the arguments
if  [ $# -ne 1 ]
then
    echo "usage stripHtml.sh <folder name> "
    echo "e.g., stripHtml  <html> "
    exit
fi

dir=`readlink -f "$1"`
for file in `ls $dir`
do
    echo "helo"
    plain=`basename "$file" .htm`
    lynx -dump -force_html $dir/$file > $plain.txt
done