#!/usr/bin/env python

import sys
import requests
import urllib2

def main():
    saveFile = open('blogLinksLists.txt', 'r')
    writeFile = open('pagesBlog.txt', 'w')
    add = "feeds/posts/default"
    for line in saveFile.readlines():
        print line
        
    saveFile.close()
    writeFile.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)