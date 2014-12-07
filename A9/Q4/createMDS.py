#!/usr/bin/env python

import clusters

def main():

    blognames,words,data=clusters.readfile('blogdata.txt') 
    coords=clusters.scaledown(data)
    clusters.draw2d(coords,blognames,jpeg='blogs2d.jpg') 
   

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)