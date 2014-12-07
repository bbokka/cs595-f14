#!/usr/bin/env python

import sys
from bs4 import BeautifulSoup

#Main Function
def main():
    # In python everything is a string you have to typecast the variables
    x = open('blogAtomLinks.txt', 'r')
    links = []

    for lines in x:
        md5link = lines.strip().split(" ")
        splitLink = md5link[2]
        links.append(splitLink)

    count = 0
    for line in links: 
        try: 
            count += 1  
            print line    
            y = open("/home/bbokka/cs594/A9/Q1/atom/"+line+".htm", 'r')
            soup     = BeautifulSoup(y)
            for link in soup.find_all('link'):
                link_atribute = link.attrs
                try :
                    id_number     = link_atribute['type']
                    if str(id_number) == ""
                    # here id_number = [u'alternate'] then do id_number[0] to get alternate
                    # if id_number == "alternate":
                    #     print id_number
                except KeyError:
                    pass                              

        except IOError:
            #print line
            pass




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)