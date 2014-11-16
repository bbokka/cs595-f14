#!/usr/bin/env python

import sys
import recommendations

def main():
    count = 'Top Gun (1986)'
    resultsOfloadMovieLens         = recommendations.loadMovieLens()
    resultsOfcalculateSimilarItems = recommendations.calculateSimilarItems(resultsOfloadMovieLens,n=80)
    print "*" * 60
    print "Movies received ratings most like or least like Top Gun"    
    print "*" * 60      
    print "value\t\t\t\t\t","Movie Name" 
    print "-" * 60 
    
    for key, value in sorted(resultsOfcalculateSimilarItems.items(), key=lambda e: e[1], reverse=True):        
        variable = key
        if (count == variable):  
            for value , movie in value: 
                print  value , movie            
 
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)