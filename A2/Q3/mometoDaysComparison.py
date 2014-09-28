#!/usr/bin/env python
import sys

def extract_momento(carbonURL) :
    try :        
        f = open('A2_momento.txt', 'r')
        for line in f.readlines() :
            momentoURL      = line.strip().split()
            momento_Count   = momentoURL[0]
            momento_url     = momentoURL[1]
            for url in carbonURL :
                if momento_url == url and momento_url >0:
                    return momento_Count
                
    except IOError :
            pass  


#Main Function
def main():  
    try :
        carbonURL = []
        f = open('carbonDateDays.txt', 'r')
        for line in f.readlines() :
            daysURL = line.strip().split()
            days    = daysURL[0]
            url     = daysURL[1]
            carbonURL.append(daysURL[1])
        #print carbonURL
        momento = extract_momento(carbonURL)
        # saveFile= open('carbonDateDays.txt','a')
        # saveFile.write("{:<2} {} " .format(momento,days))
        # saveFile.write('\n')
        # saveFile.close()            
        print momento , days 
    except IOError :
            pass  
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
