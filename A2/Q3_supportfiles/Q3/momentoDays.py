#!/usr/bin/env python
import sys    
#Main Function
def main():  
    try :
        # declaring a dictionary
        url_dict = {}
        # decalring s list
        mom_days = []
        # open the file 
        f = open('carbonDateDays.txt', 'r')
        # read all the files 
        for line in f.readlines() :
            # strip and split 
            daysURL = line.strip().split()
            days    = daysURL[0]
            url     = daysURL[1]
            # assigning the key and value to dictionary
            url_dict[url] = [ int(days) ]
        f.close()
        f = open('momentoUri.txt', 'r')        
        for line in f.readlines() :
            momento      = line.strip().split()

            if len(momento) == 2:
                try:
                    momento_count   = momento[0]
                    momento_url     = momento[1]
                    # appending the momento coutn to url== mometo_url , now it has days and moneto count
                    url_dict[ momento_url ].append( int( momento_count ) )
                except KeyError :
                    pass
        # close the file          
        f.close()        
    except IOError :
            pass  
    try :
        for i,meme in url_dict.iteritems():
            if meme[1] >0 :
                # print 'days',meme[0]
                # print 'momento',meme[0]
                saveFile= open('momentoDays.txt','a')
                saveFile.write("{:<20} {} " .format(meme[0],meme[1]))
                saveFile.write('\n')
                saveFile.close()
    except ValueError :
        pass
    except IndexError :
        pass  
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)