#!/usr/bin/env python
import sys
import time
import requests
import urllib2

# Main Function
def main():
    # set is a datatype which has all unique values
    processed_urls = set()
    # open the file which has all the extracted url
    f = open('finalUniqueUri.txt', 'r')
    
    lines = [ line.strip() for line in f.readlines() ]
    extracted_data = set (lines)     
    
    # getting each lines from the list
    for url in extracted_data :
        try:
            response = requests.get(url=url, timeout=1)
            #print repr(response.headers)
            # get all the url with the 200 ok response so that they are unique
            if response.status_code == 200 :
                processed_urls.add(url)                
                #print response.status_code,url 
            else :#code for 300 400 to 500 
                #print response.status_code
                pass         
        except requests.exceptions.ConnectionError :
            pass
        except requests.exceptions.TooManyRedirects :
            pass
        except requests.exceptions.ReadTimeout :
            pass
    # get the all the links from set and store as a list 
    final_processed_url = list (processed_urls)
    # OUT of all the links i need only 1000 links slicing the list
    for extracted_url in final_processed_url[0:1000]:
        # open the file to append to add the data
        saveFile= open('A2_final_output.txt','a')
        saveFile.write(extracted_url)
        saveFile.write('\n')
        # close the file
        saveFile.close()        
            
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
