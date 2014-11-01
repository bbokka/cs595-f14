#!/usr/bin/env python

import sys
from igraph import *

def main():
    # Load the karate.GraphML and store that into a g
    g =load('karate.GraphML')
    # label the nodes (Key-value pairs)
    g.vs["label"] = g.vs["name"]
    #print len(g.clusters())
    # setting up the layout for the graph
    layout = g.layout("kk")
    # using plot() plot the graph and save that to pdf
    plot(g, 'graph.pdf', layout = layout)
    # break the single cluster into two cluster based on the betweeness
    # this can work for any number of split based on condition < 4 < 5 :
    while len(g.clusters()) < 3 :
        # get the betweeness and store
        ebs = g.edge_betweenness()
        # among all the betweness for  each node take the maximum select max
        max_eb = max(ebs)
        # get the node which has the maximum betweeness
        max_idx = max(xrange(len(ebs)), key = ebs.__getitem__) 
        # delete the edges with max betweeness
        g.delete_edges(max_idx)
        # loop untill single cluster forms two clusters
    layout = g.layout("kk")
    # plot the graph with two clusters
    plot(g, 'graph.pdf' , layout = layout)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
