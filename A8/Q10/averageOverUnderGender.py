#!/usr/bin/env python


# program to get the highest average ratings by women under and over 40.
import sys
import operator
def main():
    # Take the arguments from the command line
    numOfArgs=len(sys.argv)
    if numOfArgs<3 or numOfArgs>3:

        print'Usage: averageOverUnderGender.py <F or M> <under or over>'
        print'e.g. : averageOverUnderGender.py F over'
        sys.exit(1)
    gender           = sys.argv[1]
    gender_under_over= sys.argv[2]

    # Create a dictionary
    movie_userid_avg = {}
    movie_id_ratings = {}    
    movie_userid_avg = {}  
    users            = {}    
    count            = 1

    # Read the files
    readData = open('/home/bbokka/cs594/A8/u.data', 'r')
    readItem = open('/home/bbokka/cs594/A8/u.item','r')
    readUser = open('/home/bbokka/cs594/A8/u.user','r')
    
    # Reading u.user file to get the male or female
    for line in readUser:
        split_input_line = line.strip().split('|')
        user_id_from_user= split_input_line[0]
        user_age         = int(split_input_line[1])
        user_gender      = split_input_line[2] 

        if gender_under_over == 'over' :
            if(gender.upper() == user_gender and user_age > 40):
                users[user_id_from_user] = [user_age]
        
        if gender_under_over == 'under' :
            if(gender.upper() == user_gender and user_age < 40):
                users[user_id_from_user] = [user_age]
        
    readUser.close()   

    # reading the u.data file for item and ratings.
    for line in readData:
        split_input_line  = line.strip().split('\t')
        user_id_from_data = split_input_line[0]
        movie_id_from_data=  split_input_line[1]
        movie_rating      =  float(split_input_line[2])
       
        if user_id_from_data in users:
            try:            
                movie_id_ratings[movie_id_from_data].append(movie_rating)
            except KeyError:
                movie_id_ratings[movie_id_from_data] = list()
                movie_id_ratings[movie_id_from_data].append(movie_rating)
    readData.close()

    # Calculating the average.
    for key in movie_id_ratings: 
        avg = sum(movie_id_ratings[key])/len(movie_id_ratings[key])
        movie_userid_avg[key] = [float(avg)]     

    # Reading the u.item file for movie name.
    for each_line in readItem:
        split_each_line  = each_line.strip().split('|')       
        
        movie_item_id    = split_each_line[0]
        movie_name_split = split_each_line[1].split('(1')
        movie_name       = movie_name_split[0] 

        try:
            movie_userid_avg[movie_item_id].append(movie_name)
        except KeyError:
            pass    
    readItem.close()
    print '*' * 55
    print "Movies rated highest on average by women"
    print "*" * 55 
    print "Movie Name\t\t\t\t\t","Avg Rating" 
    print "-" * 55
    # sorting the movies from highest to lowest based on the average value.
    for key, value in sorted(movie_userid_avg.items(), key=lambda e: e[1], reverse=True):
        if (count <=5 ):       
            print '{:<50}{:<0.1f} '  .format(value[1],value[0])
            count += 1
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)