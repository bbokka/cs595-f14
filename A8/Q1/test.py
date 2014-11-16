#!/usr/bin/env python

import sys

def main():
    # Create a dictionary
    movie_id_ratings = {}
    movie_id_name    = {}

    readData = open('u.data', 'r')
    readItem = open('u.item','r')
    for line in readData:
        split_input_line = line.strip().split('\t')
        movie_id     =  split_input_line[1]
        movie_rating =  float(split_input_line[2])
       
        try:            
            movie_id_ratings[movie_id].append(movie_rating)
        except KeyError:
            movie_id_ratings[movie_id] = list()
            movie_id_ratings[movie_id].append(movie_rating)

        #print 'movie id', movie_id ,'movie rating', movie_rating      
    for each_line in readItem:
        split_each_line = each_line.strip().split('|')
        
        movie_item_id   = split_each_line[0]
        movie_name      = split_each_line[1]
        
        movie = movie_name.split('(')
        print 'movie id', movie_item_id , 'movie name', movie[0]

    for key in movie_id_ratings: 
        print
        print "key", key
        print "values", movie_id_ratings[key]
        print "length", len(movie_id_ratings[key]),
        print "sum", sum(movie_id_ratings[key])     
        print "Average_ratings",
        print sum(movie_id_ratings[key])/len(movie_id_ratings[key])

    # for key in movie_id_avg:        
    #     print 'key',key ,'value',movie_id_avg[key]
for key in users:       
        print 'key',key ,'value',users[key]



# Calculating the average.
    for key in users: 
        avg = sum(users[key])/len(users[key])
        movie_userid_avg[key] = [float(avg)] 
    
    for key in users:       
        print 'key',key ,'value',users[key]

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)




        try:
            users[data_user_id].append(data_movie_rating)
        except:
            pass
    readData.close()

    # Calculating the average.
    for key in users: 
        print users[key]  



        try:
            users[key].append(avg)
        except KeyError:
            pass

    for key in users:       
        print 'key',key ,'value',users[key]  