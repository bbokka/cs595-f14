#!/usr/bin/env python
from datetime import datetime

    
#Main Function
def main():  
    try :  
        # current date
        now = datetime.now()
        # open the carbondate file whoch has all the dates when th eurl is created
        f = open('carbonDateTwitter.txt', 'r')
        # read all the lines(date,url)
        for line in f.readlines() :
            # split the line and strip all the spaces
            dateUrl=line.strip().split()
            # get the lenght after split
            len_date_url = len(dateUrl)
            # to get rid of lines (\r\n) since i did extract links from windows we had empty sets of data
            if len_date_url == 0:
                pass
            # if you just have date and url in each line
            elif len_date_url == 2 :
                date = dateUrl[0]
                url = dateUrl[1]

                try :
                    # using strip time function to convert the string date format to actual date type
                    date_object = datetime.strptime(date,"%Y-%m-%dT%H:%M:%S")
                    # get the number of days by subtracting the till date and past date
                    days = (now - date_object).total_seconds() / ( 3600.0 * 24 )
                    # convert that to int type
                    number_days = int(days)
                    # write it to file
                    saveFile= open('carbonDateDays.txt','a')
                    saveFile.write("{:<20} {} " .format(number_days,url))
                    saveFile.write('\n')
                    saveFile.close()      
                # catch any exception generated from         
                except :
                    date_object = datetime.strptime(date,"%Y-%m-%dT%H:%M:%S")            
    except IOError :
            pass  
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
