#!/usr/bin/env python

import sys
import time
import socket
import urllib2
import unicodedata
from bs4 import BeautifulSoup

 


def main():
    saveFile = open('blogLinksLists.txt', 'r')
    writeFile = open('pagesBlog.txt', 'w')
    #add = "feeds/posts/default"
    for url in saveFile.readlines():
        try : 
            response    = urllib2.urlopen(url,timeout=30)           
            html_content= response.read()
            # get the html content using beautiful soup
            soup        = BeautifulSoup(html_content)

            try:
                links       = soup.find('link',rel='next',href = True)['href']
                print links
            except TypeError:
                pass
            except KeyError:
                pass   

        except urllib2.HTTPError :            
            pass
        except urllib2.URLError :            
            pass
        except socket.timeout :            
            pass 
        
            


    saveFile.close()
    writeFile.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)