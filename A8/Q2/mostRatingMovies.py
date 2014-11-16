#!/usr/bin/env python

import sys

def main():
    # Create a dictionary
    movie_id_ratings    = {}    
    movie_id_avg        = {}      
    count = 1
    # Read the input files.
    readData = open('/home/bbokka/cs594/A8/u.data', 'r')
    readItem = open('/home/bbokka/cs594/A8/u.item','r')
    # reading the u.data file for item and ratings.
    for line in readData:
        split_input_line = line.strip().split('\t')
        movie_id         =  split_input_line[1]
        movie_rating     =  int(split_input_line[2])       
        try:            
            movie_id_ratings[movie_id].append(movie_rating)
        except KeyError:
            movie_id_ratings[movie_id] = list()
            movie_id_ratings[movie_id].append(movie_rating)
    readData.close()
    # Calculating the average.
    for key in movie_id_ratings: 
        length = len(movie_id_ratings[key])
        movie_id_avg[key] = [int(length)]     

    # Reading the u.item file for movie name.
    for each_line in readItem:
        split_each_line  = each_line.strip().split('|')     
        movie_item_id    = split_each_line[0]
        movie_name_split = split_each_line[1].split('(1')
        movie_name       = movie_name_split[0]                

        movie_id_avg[movie_item_id].append(movie_name)    
    readItem.close()
    print '*' * 60 
    print "Top 5 movies received the most ratings"
    print "*" * 60 
    print "Movie Name\t\t\t\t\t","Number of ratings" 
    print "-" * 60
    # sorting the movies from highest to lowest based on the average value.
    for key, value in sorted(movie_id_avg.items(), key=lambda e: e[1], reverse=True):
        if (count <= 5): 
            print '{:<50}{} '  .format(value[1],value[0])
            count += 1

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)