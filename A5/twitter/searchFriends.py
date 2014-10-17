#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

import tweepy
import unicodedata
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


consumer_key        = 'fpTauqKqCRj4Gp8m9jb9WCilk'
consumer_secret     = 'OrDd7NssqrvLgOXnzuDkGcS8UbTNoY1jFYJF0HS6daxELfyI2k'
access_token        = '2822384568-jleRlhWap2Y7SMDW9y9tXkji95GHYDJPHK2IZ0b'
access_token_secret = 'eVWGqNuLEk7xG1t47vLSkwBhJ6cQyNbeiZGShdRZXKF2A'


#Main Function
def main () :
	saveFile  = open('friendsCount.txt','w')	
	# getting access to the twitter api 
	auth      = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api       = tweepy.API(auth)
	user      = api.get_user('phonedude_mln')
	userName  = user.screen_name
	userFriendsCount = user.friends_count
	print userFriendsCount , userName
	saveFile.write("{:<10} {} " .format(userFriendsCount ,userName ))
	for friend in user.friends(count = 1000):
		count = friend.friends_count
		name  = friend.screen_name
		print count , name
		saveFile.write('\n')
		saveFile.write("{:<10} {} " .format(count ,name ))
        saveFile.write('\n')
        saveFile.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)

