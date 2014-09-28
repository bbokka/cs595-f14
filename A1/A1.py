#!/usr/bin/env python

import sys
import time
import requests
from bs4 import BeautifulSoup

#Main Function
def main():

    numOfArgs=len(sys.argv)

    if numOfArgs<4 or numOfArgs>4:

        print'Usage: A1.py <university> <sec> < URI>'
        print'e.g.: A1.py "old dominion" 60 http://sports.yahoo.com'
        sys.exit(1)

    print 'Number of arguments:', len(sys.argv), 'arguments.'
    univ = str(sys.argv[1])
    sec = int(sys.argv[2])
    uri = str(sys.argv[3])
    print 'Team Name: ' ,univ
    print 'Time to Sleep: ' ,sec
    print 'URI: ' ,uri

    response = requests.get(uri)      
    soup = BeautifulSoup(response.content)#gives you the html content of that page
    tables = soup.findChildren('table')#finds all the children of type table
    print "-" * 72
    #print tables[1].prettify()
    score_table = tables[1]#storing the results of the second table in score_table variable as our intersting stuff is in table
    # when you extract data from web and use beautiful soup it is stored in the form of array nothing but list in python


    while True:
    
        for row in score_table('tr', {'class' : 'game link' }):

            if univ.lower() in str(row).lower() :
                td_team_home = row('td', {'class' : 'home' }) 
                span_home    = td_team_home[0]('em')[0].contents[0]#the td_team_home is treated as a list so you have to get the contents of it

                td_team_away = row('td', {'class' : 'away' })
                span_away    = td_team_away[0]('em')[0].contents[0]    

                td_score     = row('td', {'class' : 'score' })
                span_home_score    = td_score[0]('span')[1].contents[0]
                span_away_score    = td_score[0]('span')[0].contents[0]

                print "*" * 8
                print span_home
                print span_home_score
                print

                print span_away
                print span_away_score
                print

                print 'Press ctrl+c to exit getting the scores'

                time.sleep(sec) # delays for 60 seconds
                print "*" * 8
                print "-" * 72

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
