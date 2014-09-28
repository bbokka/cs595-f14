#!/usr/bin/env python
import re
import sys
import time
import requests
import urllib2
    
#Main Function
def main():
    #open the file to read
    f = open('finalUniqueUri.txt', 'r')
    #regular expression to find the momento 
    momento        = re.compile(r'rel.*?=.*?"memento".*?')
    #regular expresion to find the timemap
    time_map_match = re.compile(r'<[^>]+>;rel\w*?=\w*?"timemap".*?')
    # read all the lines from the file 
    for line in f.readlines() :
        try :
            # add the url to the momento org to get the mometo(how may time the webpage has been modified)
            momento_url    = "http://mementoweb.org/timemap/link/" + line
            # get the response by opening the url
            response       = urllib2.urlopen(url=momento_url,timeout=10)
            # getting the  complete time map response
            time_map       = response.read()
            # count the number of momento            
            count_momento  = len(momento.findall(time_map))
            # get the timemap string           
            count_time_map_exist = time_map_match.findall(time_map)
            # while there is a timemap in the response (get all the count of momento as sometime the momento may be separte link)
            while len(count_time_map_exist) == 1 :
                # stripping out the url from the string_url extracted
                url             = count_time_map_exist[0]
                url_string      = url.strip('<')
                stripped_url    = url_string.split('>')
                momento_url_1   = stripped_url[0]               
                # for the url extracted which has more momento loop it utill we get all
                response_1      = urllib2.urlopen(url=momento_url_1,timeout=10)
                time_map_1      = response_1.read()               
                count_momento   = len(momento.findall(time_map_1)) + count_momento                
                count_time_map_exist = time_map_match.findall(time_map_1)                       

            saveFile= open('A2_momento.txt','a')
            saveFile.write("{:<20} {} " .format(count_momento,line))            
            saveFile.close()          
             
        except urllib2.HTTPError:
            #some url will not have timemap then make the timemap none
            time_map = None
            count_momento = 0
            saveFile= open('momentoUri.txt','a')
            #the way you write two or more elements to a file and format it to 20 spaces
            saveFile.write("{:<20} {} " .format(count_momento,line))            
            saveFile.close()            
        #catch the file errors like file caanot be opended
        except IOError :
            pass  
        except urllib2.URLError :
            pass  
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)