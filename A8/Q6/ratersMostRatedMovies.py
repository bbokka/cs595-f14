#!/usr/bin/env python

import sys

def main():
    # Create a dictionary
    movie_userid_ratings = {}
    movie_userid_len     = {}
    count                = 1
    # Read the input files.
    readData = open('/home/bbokka/cs594/A8/u.data', 'r')
     # reading the u.data file for item and ratings.
    for line in readData:
        split_input_line  = line.strip().split('\t')
        user_id_from_data = split_input_line[0]        
        movie_rating      =  float(split_input_line[2])       
        
        try:            
            movie_userid_ratings[user_id_from_data].append(movie_rating)
        except KeyError:
            movie_userid_ratings[user_id_from_data] = list()
            movie_userid_ratings[user_id_from_data].append(movie_rating)
    readData.close()
    # Calculating the number of movies each user rated.
    for key in movie_userid_ratings: 
        length = len(movie_userid_ratings[key])
        movie_userid_len[key] = int(length)   

    
    print '*' * 60 
    print "Top 5 raters rated movies."
    print "*" * 60 
    print "User id\t\t","Number of movies rated" 
    print "-" * 60
    # sorting the movies from highest to lowest based on the number of 
    # ratings for each movie.
    for key, value in sorted(movie_userid_len.items(), key=lambda e: e[1], reverse=True):
        if (count <= 5): 
            print '{:<20}{} '  .format(key,value)
            count += 1

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)