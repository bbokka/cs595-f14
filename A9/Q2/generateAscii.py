#!/usr/bin/env python

import sys
import clusters

def main():

    # returns blog titles, words in blog (10%-50% boundaries), list of frequency info
    blognames,words,data=clusters.readfile('blogdata.txt') 

    # returns a tree of foo.id, foo.left, foo.right
    clust=clusters.hcluster(data)

    # walks tree and prints ascii approximation of a dendogram; distance measure is Pearson's r
    clusters.printclust(clust,labels=blognames) 

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)