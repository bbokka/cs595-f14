#!/usr/bin/env python

import clusters

def main():

    blognames,words,data=clusters.readfile('blogdata.txt') 
    print "K value is 5"
    kclust=clusters.kcluster(data,k=5)
    print "K value is 10"
    kclust=clusters.kcluster(data,k=10)
    print "K value is 20"
    kclust=clusters.kcluster(data,k=20)
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)