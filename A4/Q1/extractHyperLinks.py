#!/usr/bin/env python

import os
import md5
import sys
import time
import socket
import urllib2
import unicodedata
from bs4 import BeautifulSoup

LIMIT = 100

#Main Function
def main():
    # open the 100 links file
    uniqueLinks = open('A2FinalOutput.txt', 'r')
    writeFile   = open('md5Links.txt','w')
       
    counter = 0
    for url in uniqueLinks.readlines() :  
        hashmd5    = md5.new(url).hexdigest()  
        filename    = 'links/' + hashmd5 + '.link'
        try : 
            request     = urllib2.Request(url)
            response    = urllib2.urlopen(url,timeout=30)           
            html_content= response.read()

            # get the html content using beautiful soup
            soup        = BeautifulSoup(html_content)
            links       = soup.find_all('a')
                        
            writeFile.write("{:<20} {}" .format(hashmd5,url))            
            counter += 1      
            
            saveFile= open(filename,'w')

            for tag in links:                    
                try :
                    link  = tag.get('href',None)
                    if link != None and link.startswith( "http" ):                    
                        
                        saveFile.write(link) 
                        saveFile.write('\n')           
                    
                except UnicodeEncodeError:
                    pass
            saveFile.close() 

        except urllib2.HTTPError :            
            pass
        except urllib2.URLError :            
            pass
        except socket.timeout :            
            pass
        print filename , counter
        print "-" * 50
        # get only the 100 urls data
        if counter >= LIMIT:
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)