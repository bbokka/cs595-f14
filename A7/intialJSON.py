#!/usr/bin/env python

import sys
import json
import networkx as nx
from networkx.readwrite import json_graph

def main():
    # Load the karate.GraphML and store that into a g
    g =nx.karate_club_graph()
    data = json_graph.node_link_data(g)

    with open ('graph.json' , 'w') as f:
        json.dump(data, f, indent=1)
    
       
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)