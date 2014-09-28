#!/usr/bin/env python
import re
import sys
import time
from TwitterSearch import *

#Main Function
def main():
    try:
        # create a TwitterSearchOrder object
        tso = TwitterSearchOrder()
        # search key word 
        tso.setKeywords(['noodles']) 
        # we want to see German tweets only
        tso.setLanguage('en') 
        # look for 100 tweets per page
        tso.setCount(100) 
        # and don't give us all those entity information(is the html)
        tso.setIncludeEntities(False)         
        # keys to interact with the twitter API
        # my keys
        ts = TwitterSearch(
            consumer_key = 'fpTauqKqCRj4Gp8m9jb9WCilk',
            consumer_secret = 'OrDd7NssqrvLgOXnzuDkGcS8UbTNoY1jFYJF0HS6daxELfyI2k',
            access_token = '2822384568-jleRlhWap2Y7SMDW9y9tXkji95GHYDJPHK2IZ0b',
            access_token_secret = 'eVWGqNuLEk7xG1t47vLSkwBhJ6cQyNbeiZGShdRZXKF2A'
         )        
        for tweet in ts.searchTweetsIterable(tso): 
            # for a tweet points to user->entities->url->urls->(urls,expandes_url,)
            try :
                for sea in tweet['user']['entities']['url']['urls']:
                    # sea points to (urls,expandes_url...)
                    data = sea['expanded_url']
                    # if there is some data then write it to file
                    if data:
                        #print data
                        saveFile= open('extractedUri.txt','a')
                        saveFile.write(data)
                        saveFile.write('\n')
                        saveFile.close()
            # spent :( a night to resolve this error 
            # not all tweets has expanded url so there is a key value excpetion we have to catch it .                         
            except KeyError :
                print 'error'
    # catch all the search exceptions if you dnt find a tweet         
    except TwitterSearchException as e: 
        print(e)    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)