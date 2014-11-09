#!/usr/bin/env python

import sys
from bs4 import BeautifulSoup

#Main Function
def main():
    cou =33
    htmlfile = open('karate.GraphML', 'r')
    datafile = open('karateData.json', 'w')
    soup     = BeautifulSoup(htmlfile)
    #print soup.prettify()
    datafile.write('{\n "directed": false,\n "graph": [ \n  [ \n  "name",\n  "Zachary\'s karate Club" \n  ]\n ],\n')
    # start of nodes
    datafile.write(' "nodes": [\n' )
    for node in soup.find_all('node'):
        node_attrs = dict(node.attrs)
        id_number  = node_attrs[u'id']
        data_faction, data_name   = node.find_all('data')
        
        data_faction_value = data_faction.contents
        data_name_value    = data_name.contents

        id_number_split = id_number.split('n');       
        count           = id_number_split[1]
        # write to a a file
        datafile.write('  {\n')
        datafile.write('   "id": ')      
        datafile.write( id_number_split[1])
        datafile.write(',\n')

        datafile.write('   "faction": ')      
        datafile.write(data_faction_value[0])
        datafile.write(',\n')

        datafile.write('   "name": "')      
        datafile.write(data_name_value[0])
        datafile.write('"\n ')
         
        if count != 33:
            datafile.write(' },\n')             
        else :
            datafile.write(' }\n ],')            
        
     # end of nodes 
#-------------------------------------------------------------------------------------------------------------------------------
    # start of links
    datafile.write('\n "links": [\n' )
    for edge in soup.find_all('edge'):
        edge_attrs  = dict(edge.attrs)        
        edge_source = edge_attrs[u'source']
        edge_target = edge_attrs[u'target']

        edge_source_split = edge_source.split('n')
        edge_target_split = edge_target.split('n')

        data_weight       = edge.find('data')
        data_weight_value = data_weight.contents 

        datafile.write('  {\n')
        datafile.write('   "source": ')      
        datafile.write(edge_source_split[1])
        datafile.write(',\n')

        datafile.write('   "target": ')      
        datafile.write(edge_target_split[1])
        datafile.write(',\n')

        datafile.write('   "weight": "')      
        datafile.write(data_weight_value[0])
        datafile.write('"\n ')

        #print edge_source_split[1]
        if edge_source_split[1] == 32:
            datafile.write(' }\n ],\n "multigraph": false\n } ')            
        else:
             datafile.write(' },\n')

    # end of links

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
